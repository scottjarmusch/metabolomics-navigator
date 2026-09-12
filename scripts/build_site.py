#!/usr/bin/env python
from __future__ import annotations

import argparse, hashlib, html, json, os, shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlencode

from jinja2 import Environment, FileSystemLoader, select_autoescape

from contributors import build_contributors
from seo import page_metadata

from common import (
    ROOT, counts_for, date_display, derive_base_path, label_maps,
    load_strategies, load_tools, load_vocab, record_date, validator,
)

OUT=ROOT/'dist'


INVERSE_TOOL_RELATIONSHIPS={
    'alternative':'alternative',
    'complementary':'complementary',
    'integration':'integration',
    'part_of':'contains',
    'contains':'part_of',
    'successor':'predecessor',
    'predecessor':'successor',
}

def build_relationship_index(tools,tool_by_slug,labels):
    """Return explicit + safely inferred inverse relationships for each tool.

    Explicit declarations always win over inferred duplicates. Relationships
    without a semantically safe inverse (dependency, hosted_by, uses, other)
    remain one-directional.
    """
    graph={tool['slug']:{} for tool in tools}

    def add(source,target,relationship,note='',inferred=False):
        if source not in graph or target not in tool_by_slug or source==target:
            return
        key=target
        current=graph[source].get(key)
        item={
            'tool':tool_by_slug[target],
            'relationship':relationship,
            'relationship_label':labels['tool_relationships'].get(relationship,'Related to'),
            'note':note or '',
            'inferred':inferred,
        }
        if current is None or (current.get('inferred') and not inferred):
            graph[source][key]=item

    # Explicit relationships first.
    for tool in tools:
        source=tool['slug']
        for rel in tool.get('related_tools',[]):
            add(source,rel['slug'],rel.get('relationship','other'),rel.get('note',''),False)

    # Add only safe inverses, without overwriting an explicit reverse relation.
    for tool in tools:
        source=tool['slug']
        for rel in tool.get('related_tools',[]):
            inverse=INVERSE_TOOL_RELATIONSHIPS.get(rel.get('relationship','other'))
            if inverse:
                add(rel['slug'],source,inverse,'',True)

    def sort_key(item):
        # Explicit first, then relationship label and tool name for stable pages.
        return (item.get('inferred',False),item['relationship_label'].casefold(),item['tool']['name'].casefold())
    return {slug:sorted(items.values(),key=sort_key) for slug,items in graph.items()}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--base-path',default=None)
    parser.add_argument('--strict',action='store_true')
    args=parser.parse_args()

    vocab=load_vocab(); labels=label_maps(vocab)
    tools_raw=clean_and_validate(load_tools(),'tool')
    strategies_raw=clean_and_validate(load_strategies(),'strategy')
    site=load_yaml(ROOT/'config/site.yml')

    github_repository=os.getenv('GITHUB_REPOSITORY','')
    repository_url=os.getenv('PUBLIC_REPOSITORY_URL',site['repository_url']).rstrip('/')
    if github_repository and 'OWNER' in repository_url:
        repository_url=f'https://github.com/{github_repository}'
    base_path=derive_base_path(args.base_path)
    site_url=os.getenv('SITE_URL','').rstrip('/')
    if not site_url and github_repository:
        owner,_=github_repository.split('/',1); site_url=f'https://{owner.lower()}.github.io'
    if not site_url: site_url=site['site_url'].rstrip('/')
    generated_at=datetime.now(timezone.utc).strftime('%d %B %Y')

    def url(path=''):
        path=str(path).lstrip('/')
        if not path: return f'{base_path}/' if base_path else '/'
        return f'{base_path}/{path}' if base_path else f'/{path}'
    def absolute_url(path=''):
        local=url(path); return f'{site_url}{local}' if site_url else local

    env=Environment(loader=FileSystemLoader(ROOT/'templates'),autoescape=select_autoescape(['html','xml']))
    env.globals.update(url=url,absolute_url=absolute_url)

    tools=sorted([enrich_tool(r,labels) for r in tools_raw],key=lambda x:x['name'].casefold())
    tool_by_slug={t['slug']:t for t in tools}
    strategies=sorted([enrich_strategy(r,labels,tool_by_slug) for r in strategies_raw],key=lambda x:x['name'].casefold())
    strategy_by_slug={p['slug']:p for p in strategies}

    # Bidirectional knowledge graph: tools know which strategies use them.
    for tool in tools: tool['strategies_using']=[]
    for strategy in strategies:
        seen=set()
        for item in strategy.get('tools',[]):
            if item.get('slug'): seen.add(item['slug'])
        for step in strategy.get('workflow_steps',[]): seen.update(step.get('tool_slugs',[]))
        for slug in seen:
            if slug in tool_by_slug: tool_by_slug[slug]['strategies_using'].append(strategy)

    # Tool relationships are stored once and rendered bidirectionally where the
    # relationship has an unambiguous inverse. This keeps the catalogue graph
    # consistent without forcing editors to maintain duplicate declarations.
    relationship_index=build_relationship_index(tools,tool_by_slug,labels)

    workflow_owners=load_yaml(ROOT/'config/tool-workflows.yml')
    for tool in tools: tool['reference_workflows']=[]
    for workflow_slug,owner in workflow_owners.items():
        record=load_yaml(ROOT/'content/tool-workflows'/f'{workflow_slug}.yml')
        tool_by_slug[owner]['reference_workflows'].append(record)

    prepare_output()
    copy_public_files()
    asset_version=hashlib.sha256(b''.join((ROOT/'assets'/name).read_bytes() for name in ('site.css','product-refresh.css','site.js','catalogue.js'))).hexdigest()[:12]
    context={'site':site,'repository_url':repository_url,'generated_at':generated_at,'asset_version':asset_version,'contributors':build_contributors([*tools_raw,*strategies_raw])}

    # Homepage
    function_counts={item['id']:sum(item['id'] in {t['functions']['primary'], *t['functions'].get('secondary',[])} for t in tools_raw) for item in vocab['functions']}
    featured_ids=['preprocessing','quality_control','annotation_identification','spectral_analysis','molecular_networking','statistics','pathway_interpretation','reference_data_search']
    icons={'preprocessing':'⌁','quality_control':'✓','annotation_identification':'◇','spectral_analysis':'∿','molecular_networking':'⌘','statistics':'∑','pathway_interpretation':'↗','reference_data_search':'⌕'}
    functions_by_id={x['id']:x for x in vocab['functions']}
    featured=[{**functions_by_id[i],'count':function_counts[i],'icon':icons[i]} for i in featured_ids]
    recent_tools=sorted(tools,key=lambda x:(x['created_at'],x['name']),reverse=True)[:4]
    recent_strategies=sorted(strategies,key=lambda x:(x['created_at'],x['name']),reverse=True)[:4]
    stats={'tools':len(tools),'strategies':len(strategies),'functions':len(vocab['functions']),
           'verified':sum(bool(t['provenance'].get('developer_verified')) for t in tools)+sum(bool(p['provenance'].get('author_verified')) for p in strategies)}
    guide_sections=load_yaml(ROOT/'config/guide.yml')
    for section in guide_sections:
        missing=set(section['slugs'])-set(tool_by_slug)
        if missing: raise SystemExit(f'Guide section {section["id"]} references unknown tools: {sorted(missing)}')
        section['tools']=[tool_by_slug[slug] for slug in section['slugs']]
    render(env,'home.html',OUT/'index.html',**context,active='home',stats=stats,guide_sections=guide_sections)
    for group in guide_sections:
        render(env,'guide.html',OUT/f"guide/{group['id']}/index.html",**context,active='guide',stats=stats,group=group,guide_sections=guide_sections)

    # Tool catalogue
    tool_filters=[
      make_filter('function','Scientific function','functions',vocab['functions'],function_counts),
      make_filter('platforms','Analytical platform','platforms',vocab['platforms'],counts_for(tools_raw,'platforms')),
      make_filter('interfaces','Interface','interfaces',vocab['interfaces'],counts_for(tools_raw,'interfaces')),
      make_filter('access','Access model','access models',vocab['access_models'],counts_for(tools_raw,'access.model')),
      make_filter('resource-types','Resource type','resource types',vocab['resource_types'],counts_for(tools_raw,'resource_types')),
    ]
    render(env,'tools.html',OUT/'tools/index.html',**context,active='tools',tools=tools,filters=tool_filters)

    for tool in tools:
        explicit=relationship_index.get(tool['slug'],[])
        if explicit:
            related=explicit
        else:
            related=[{'tool':x,'relationship':'alternative','relationship_label':'Similar function','note':'','inferred':True} for x in tools if x['slug']!=tool['slug'] and x['functions']['primary']==tool['functions']['primary']][:4]
        update_query=urlencode({'template':'update-tool.yml','title':f"[Tool update]: {tool['name']}"})
        update_url=f"{repository_url}/issues/new?{update_query}"
        source_url=f"{repository_url}/blob/main/content/tools/{quote(tool['slug'])}.yml"
        render(env,'tool.html',OUT/f"tools/{tool['slug']}/index.html",**context,active='tools',tool=tool,related_tools=related,strategies_using=tool['strategies_using'],update_url=update_url,source_url=source_url)

    # Strategy catalogue
    objective_counts=counts_for(strategies_raw,'purpose.primary')
    strategy_filters=[
      make_filter('objective','Scientific objective','objectives',vocab['strategy_objectives'],objective_counts),
      make_filter('platforms','Analytical platform','platforms',vocab['platforms'],counts_for(strategies_raw,'platforms')),
      make_filter('analysis-types','Analysis type','analysis types',vocab['analysis_types'],counts_for(strategies_raw,'analysis_types')),
      make_filter('components','Strategy component','components',vocab['strategy_components'],counts_for(strategies_raw,'components')),
      make_filter('sample-types','Sample type','sample types',vocab['sample_types'],counts_for(strategies_raw,'sample_types')),
      make_filter('biological-contexts','Biological context','contexts',vocab['biological_contexts'],counts_for(strategies_raw,'biological_contexts')),
    ]
    render(env,'strategies.html',OUT/'strategies/index.html',**context,active='strategies',strategies=strategies,filters=strategy_filters)
    for strategy in strategies:
        related=[strategy_by_slug[s] for s in strategy.get('related_strategies',[]) if s in strategy_by_slug]
        update_query=urlencode({'template':'update-strategy.yml','title':f"[Strategy update]: {strategy['name']}"})
        update_url=f"{repository_url}/issues/new?{update_query}"
        source_url=f"{repository_url}/blob/main/content/strategies/{quote(strategy['slug'])}.yml"
        render(env,'strategy.html',OUT/f"strategies/{strategy['slug']}/index.html",**context,active='strategies',strategy=strategy,related_strategies=related,update_url=update_url,source_url=source_url)

    # Browse combines both content types.
    sections=[
      browse_section('Tool functions','Broad tasks performed by software, databases, services, and other tools.','tools/','function',vocab['functions'],function_counts),
      browse_section('Tool platforms','Analytical technologies supported by tools.','tools/','platforms',vocab['platforms'],counts_for(tools_raw,'platforms')),
      browse_section('Strategy objectives','Scientific questions and transferable strategies represented by strategies.','strategies/','objective',vocab['strategy_objectives'],objective_counts),
      browse_section('Strategy components','Experimental and computational stages included in strategies.','strategies/','components',vocab['strategy_components'],counts_for(strategies_raw,'components')),
      browse_section('Strategy sample types','Sample matrices represented by published strategies.','strategies/','sample-types',vocab['sample_types'],counts_for(strategies_raw,'sample_types')),
      browse_section('Strategy biological contexts','Broad biological systems and study contexts represented by strategies.','strategies/','biological-contexts',vocab['biological_contexts'],counts_for(strategies_raw,'biological_contexts')),
    ]
    render(env,'browse.html',OUT/'browse/index.html',**context,active='browse',sections=sections)

    # Contribution landing page.
    tool_submit=f"{repository_url}/issues/new?{urlencode({'template':'submit-tool.yml','title':'[Tool submission]: '})}"
    strategy_submit=f"{repository_url}/issues/new?{urlencode({'template':'submit-strategy.yml','title':'[Strategy submission]: '})}"
    tool_update=f"{repository_url}/issues/new?{urlencode({'template':'update-tool.yml','title':'[Tool update]: '})}"
    strategy_update=f"{repository_url}/issues/new?{urlencode({'template':'update-strategy.yml','title':'[Strategy update]: '})}"
    render(env,'submit.html',OUT/'submit/index.html',**context,active='submit',tool_submission_url=tool_submit,strategy_submission_url=strategy_submit,tool_update_url=tool_update,strategy_update_url=strategy_update)

    pages=static_pages(repository_url,url)
    pages.pop('contribute')
    pages['privacy']={'title':'Privacy','description':'How community contribution information is handled.'}
    render(env,'submit.html',OUT/'contribute/index.html',**context,active='contribute',tool_submission_url=tool_submit,strategy_submission_url=strategy_submit,tool_update_url=tool_update,strategy_update_url=strategy_update)
    for slug,page in pages.items():
        template=f'{slug}.html' if slug in ('about','ask','privacy') else 'static.html'
        render(env,template,OUT/f'{slug}/index.html',**context,active=slug,page=page)
    render(env,'404.html',OUT/'404.html',**context,active='')

    write_json(OUT/'tool-data.json',tools_raw); write_json(OUT/'strategy-data.json',strategies_raw)
    write_json(OUT/'catalogue-data.json',{'tools':tools_raw,'strategies':strategies_raw})
    write_sitemap(OUT,tools,strategies,absolute_url,guide_sections)
    (OUT/'robots.txt').write_text(f"User-agent: *\nAllow: /\nSitemap: {absolute_url('sitemap.xml')}\n",encoding='utf-8')
    print(f"Built {len(tools)} tool pages and {len(strategies)} strategy pages in {OUT} with base path '{base_path or '/'}'.")


def clean_and_validate(records,kind):
    check=validator(kind); clean=[]
    for record in records:
        path=record['_path']; item={k:v for k,v in record.items() if k!='_path'}
        if list(check.iter_errors(item)):
            raise SystemExit(f'Cannot build: {path} failed {kind} schema validation. Run scripts/validate_catalogue.py.')
        clean.append(item)
    return clean


def prepare_output():
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(parents=True)


def copy_public_files():
    shutil.copytree(ROOT/'assets',OUT/'assets')
    (OUT/'schemas').mkdir(); shutil.copy2(ROOT/'schemas/tool.schema.json',OUT/'schemas/tool.schema.json'); shutil.copy2(ROOT/'schemas/strategy.schema.json',OUT/'schemas/strategy.schema.json')
    (OUT/'data').mkdir(); shutil.copy2(ROOT/'data/controlled-vocabulary.yml',OUT/'data/controlled-vocabulary.yml')
    (OUT/'.nojekyll').write_text('',encoding='utf-8')


def load_yaml(path):
    import yaml
    return yaml.safe_load(path.read_text(encoding='utf-8'))


def make_filter(key,label,all_label,options,counts):
    return {'key':key,'label':label,'all_label':all_label,'options':[{**x,'count':counts[x['id']]} for x in options if counts[x['id']]>0]}


def browse_section(title,description,path,param,items,counts):
    return {'title':title,'description':description,'path':path,'param':param,'items':[{**x,'count':counts[x['id']]} for x in items if counts[x['id']]>0]}


def list_labels(items,mapping): return [mapping.get(x,x) for x in items]


def enrich_tool(record,labels):
    t=dict(record); status=t.get('status',{}); maintenance=t.get('maintenance',{}); data=t.get('data') or {}; access=t.get('access',{}); provenance=t.get('provenance',{}); acquisition=t.get('acquisition') or {}
    t['created_at']=record_date(t,'created_at'); t['updated_at']=record_date(t,'updated_at'); t['updated_display']=date_display(t['updated_at']); t['verified_display']=date_display(status.get('last_verified'))
    t['primary_function_label']=labels['functions'].get(t['functions']['primary'],t['functions']['primary'])
    t['secondary_function_labels']=list_labels(t['functions'].get('secondary',[]),labels['functions'])
    t['capability_labels']=list_labels(t['functions'].get('capabilities',[]),labels['capabilities'])
    t['resource_type_labels']=list_labels(t['resource_types'],labels['resource_types']); t['platform_labels']=list_labels(t['platforms'],labels['platforms']); t['interface_labels']=list_labels(t['interfaces'],labels['interfaces']); t['analysis_type_labels']=list_labels(t.get('analysis_types',[]),labels['analysis_types'])
    t['access_label']=labels['access_models'].get(access['model'],access['model']); t['maintenance_label']=labels['maintenance_statuses'].get(maintenance.get('status','unclear'),'Not assessed'); t['entry_status_label']=labels['entry_statuses'].get(status['entry'],status['entry'])
    t['input_type_labels']=list_labels(data.get('input_types',[]),labels['common_data_types']); t['output_type_labels']=list_labels(data.get('output_types',[]),labels['common_data_types']); t['input_format_labels']=list_labels(data.get('input_formats',[]),labels['common_data_formats'])+data.get('other_input_formats',[]); t['output_format_labels']=list_labels(data.get('output_formats',[]),labels['common_data_formats'])+data.get('other_output_formats',[])
    t['ms_level_labels']=list_labels(acquisition.get('ms_levels',[]),labels['ms_levels']); t['acquisition_strategy_labels']=list_labels(acquisition.get('strategies',[]),labels['acquisition_strategies']); t['ion_mobility_label']=labels['ion_mobility_support'].get(acquisition.get('ion_mobility',''),'')
    technical=t.get('technical') or {}; t['operating_system_labels']=list_labels(technical.get('operating_systems',[]),labels['operating_systems']); t['release_display']=date_display(maintenance.get('latest_release_date')); t['maintenance_checked_display']=date_display(maintenance.get('last_checked'))
    role=provenance.get('submitted_by','other'); submitted={'developer':'Developer submitted','maintainer':'Maintainer submitted','user':'Community submitted','curator':'Curator submitted','other':'Community submitted'}.get(role,'Community submitted')
    provenance_badges=[submitted]
    if provenance.get('developer_verified'): provenance_badges.append('Developer verified')
    if status.get('review')=='editorially_reviewed': provenance_badges.append('Editorially reviewed')
    t['provenance_label']=submitted; t['provenance_badges']=provenance_badges
    t['card_badges']=(t['capability_labels'][:2]+t['platform_labels'][:1]+t['interface_labels'][:1])[:4]
    t['page_badges']=(t['platform_labels']+t['analysis_type_labels']+t['interface_labels']+[t['access_label']])[:10]
    link_names={'primary':'Primary access','homepage':'Homepage','web_app':'Web application','repository':'Source repository','documentation':'Documentation','download':'Download','tutorial':'Tutorial','issue_tracker':'Issue tracker','biotools':'bio.tools record','workflowhub':'WorkflowHub record'}
    seen=set(); t['display_links']=[]
    for key,href in t['links'].items():
        if href in seen: continue
        seen.add(href); t['display_links'].append((link_names.get(key,key.replace('_',' ').title()),href))
    search=[t['name'],t.get('acronym',''),*t.get('aliases',[]),t['summary'],t['primary_function_label'],*t['secondary_function_labels'],*t['capability_labels'],*t['platform_labels'],*t['interface_labels'],*t['analysis_type_labels'],t['access_label'],*t['input_format_labels'],*t['output_format_labels'],*t['ms_level_labels'],*t['acquisition_strategy_labels']]
    t['search_text']=' '.join(map(str,search)).lower(); return t


def enrich_strategy(record,labels,tool_by_slug):
    p=dict(record); status=p.get('status',{}); acquisition=p.get('acquisition') or {}; resources=p.get('resources') or {}
    p['created_at']=record_date(p,'created_at'); p['updated_at']=record_date(p,'updated_at'); p['updated_display']=date_display(p['updated_at']); p['verified_display']=date_display(status.get('last_verified'))
    p['objective_label']=labels['strategy_objectives'].get(p['purpose']['primary'],p['purpose']['primary']); p['secondary_objective_labels']=list_labels(p['purpose'].get('secondary',[]),labels['strategy_objectives'])
    p['platform_labels']=list_labels(p['platforms'],labels['platforms']); p['analysis_type_labels']=list_labels(p.get('analysis_types',[]),labels['analysis_types']); p['component_labels']=list_labels(p.get('components',[]),labels['strategy_components']); p['sample_type_labels']=list_labels(p.get('sample_types',[]),labels['sample_types']); p['biological_context_labels']=list_labels(p.get('biological_contexts',[]),labels['biological_contexts'])
    p['ms_level_labels']=list_labels(acquisition.get('ms_levels',[]),labels['ms_levels']); p['acquisition_strategy_labels']=list_labels(acquisition.get('strategies',[]),labels['acquisition_strategies']); p['ion_mobility_label']=labels['ion_mobility_support'].get(acquisition.get('ion_mobility',''),'')
    p['resolved_tools']=[]
    for item in p.get('tools',[]):
        x=dict(item)
        if x.get('slug') in tool_by_slug: x['tool']=tool_by_slug[x['slug']]
        p['resolved_tools'].append(x)
    steps=[]
    for step in p.get('workflow_steps',[]):
        x=dict(step); x['tools']=[tool_by_slug[s] for s in step.get('tool_slugs',[]) if s in tool_by_slug]; steps.append(x)
    p['workflow_steps_enriched']=steps
    role=p.get('provenance',{}).get('submitted_by','other'); submitted={'author':'Author submitted','user':'Community submitted','curator':'Curator submitted','other':'Community submitted'}.get(role,'Community submitted')
    badges=[submitted]
    if p.get('provenance',{}).get('author_verified'): badges.append('Author verified')
    if status.get('review')=='editorially_reviewed': badges.append('Editorially reviewed')
    p['provenance_badges']=badges
    p['page_badges']=(p['platform_labels']+p['analysis_type_labels']+[p['objective_label']])[:8]
    p['availability_labels']=[]
    for key,label in [('raw_data_available','Raw data available'),('processed_data_available','Processed data available'),('code_available','Code available'),('method_available','Published method available')]:
        if resources.get(key): p['availability_labels'].append(label)
    search=[p['name'],p['summary'],p['objective_label'],*p['secondary_objective_labels'],*p['platform_labels'],*p['analysis_type_labels'],*p['component_labels'],*p['sample_type_labels'],*p['biological_context_labels'],*p.get('organisms',[]),*p['ms_level_labels'],*p['acquisition_strategy_labels'],*[x.get('name') or (x.get('tool') or {}).get('name','') for x in p['resolved_tools']]]
    p['search_text']=' '.join(map(str,search)).lower(); return p


def render(env,template,destination,**context):
    route=destination.relative_to(OUT).as_posix()
    if route.endswith('index.html'): route=route[:-len('index.html')]
    context['seo']=page_metadata(template,route,context,env.globals['absolute_url'])
    destination.parent.mkdir(parents=True,exist_ok=True); destination.write_text(env.get_template(template).render(**context),encoding='utf-8')


def write_json(path,data):
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False,default=str)+'\n',encoding='utf-8')


def static_pages(repository_url,url):
    about=''  # Content lives in templates/about.html.
    contribute=f'''<h2>Submit a missing resource</h2><p>Researchers can add either a tool or a published strategy through short forms. Automation converts each submission into a structured draft pull request for editorial review.</p><p><a class="button primary" href="{url('submit/')}">Choose a submission form</a></p><h2>Improve existing pages</h2><p>Every tool and strategy page links to an update form. Corrections, capabilities, versions, workflow details, data availability, and verification are welcome.</p><h2>Review model</h2><p>Developer or author provenance and editorial review are displayed separately. Neither implies independent benchmarking or a performance ranking.</p><div class="callout"><strong>Neutrality:</strong> describe documented capabilities, scope, requirements, and considerations. Avoid promotional language and unsupported “best tool” claims.</div><p><a href="{repository_url}/blob/main/CONTRIBUTING.md">Read the full contribution guide</a>.</p>'''
    governance=f'''<h2>Editorial model</h2><p>New tools and strategies enter through pull requests. Editors check scope, controlled categories, factual presentation, links, and conflicts of interest before publication.</p><h2>Analytical Strategy inclusion</h2><p>A methodological contribution and transferability are mandatory. A Strategy should normally also meet at least two of these three criteria: distinctive integration of evidence, added capability beyond routine software use, and enough detail for another laboratory to implement it.</p><blockquote>If the biological findings were removed, would the methodological idea still be worth teaching to another metabolomics researcher?</blockquote><p>Ordinary application papers are excluded. Routine software workflows belong in Tool capabilities.</p><h2>Verification</h2><p><strong>Developer verified</strong> means a developer or official maintainer confirmed the current tool entry. <strong>Author verified</strong> means an author of the underlying strategy publication confirmed the entry. <strong>Editorially reviewed</strong> means a Navigator editor checked scope, links, categorization, provenance, and neutral presentation. Verification is not endorsement or independent benchmarking.</p><h2>Claims and evidence</h2><p>Factual metadata and documented scope may come from developers or authors. Comparative claims such as greater accuracy, sensitivity, or speed require an appropriate independent citation; unsupported promotional claims are excluded.</p><h2 id="publication-selection">Publication selection</h2><p>Core publications introduce the named resource, substantially update it, or describe methods implemented within it. Application studies and papers introducing separate resources are excluded. Distinct component papers belong on their own tool or strategy pages. An official parent-platform citation is labelled when it covers a component. Software and documentation citations are shown separately, and preprints are identified.</p><h2>Archiving</h2><p>Unavailable or superseded tools are normally retained with an archived status so older publications remain interpretable. Strategy pages remain tied to their source publication while Navigator notes can be updated as resources change.</p><p><a href="{repository_url}/blob/main/GOVERNANCE.md">Read the repository governance file</a>.</p>'''
    ask=''  # Visual preview lives in templates/ask.html.
    return {'about':{'title':'About the catalogue','eyebrow':'Project','description':'A community-maintained map of metabolomics tools and transferable strategies.','body':about},'contribute':{'title':'Contribute','eyebrow':'Community','description':'Add a tool, submit a strategy, or improve an existing entry.','body':contribute,'active':'contribute'},'governance':{'title':'Governance and review','eyebrow':'Trust and transparency','description':'How entries are reviewed, attributed, verified, corrected, and archived.','body':governance},'ask':{'title':'Ask Navigator','eyebrow':'Coming next','description':'A guided way to move from your data to compatible metabolomics resources.','body':ask,'active':'ask'}}


def write_sitemap(out,tools,strategies,absolute_url,guide_sections):
    paths=['','ask/','tools/','strategies/','browse/','submit/','about/','contribute/','governance/','privacy/']+[f"tools/{x['slug']}/" for x in tools]+[f"strategies/{x['slug']}/" for x in strategies]
    paths += [f"guide/{group['id']}/" for group in guide_sections]
    xml=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path in paths: xml.append(f'  <url><loc>{html.escape(absolute_url(path))}</loc></url>')
    xml.append('</urlset>'); (out/'sitemap.xml').write_text('\n'.join(xml)+'\n',encoding='utf-8')

if __name__=='__main__': main()
