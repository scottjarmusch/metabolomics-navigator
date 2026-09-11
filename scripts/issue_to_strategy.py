#!/usr/bin/env python
from __future__ import annotations

import argparse, json, os, re
from datetime import date
from pathlib import Path
import yaml

from common import ROOT, STRATEGIES_DIR, load_tools, load_vocab, reverse_label_maps, slugify
from contributors import parse_attribution
from issue_to_tool import parse_sections, clean, selected, map_values

LABELS={
 'name':'Strategy or method name',
 'publication':'Publication DOI or URL',
 'summary':'What problem does this strategy solve?',
 'platforms':'Main analytical platform',
 'objective':'Main scientific objective',
 'tools':'Tools or resources used',
 'role':'What is your relationship to this work?',
 'sample_types':'Sample types',
 'biological_contexts':'Biological context',
 'organisms':'Specific organisms',
 'analysis_types':'Analysis type',
 'components':'Strategy components',
 'submitter_name':'Contributor name',
 'submitter_orcid':'ORCID iD',
 'notes':'Anything else we should know?',
}

def split_tools(text):
    out=[]
    for line in clean(text).splitlines():
        line=re.sub(r'^[-*]\s+','',line.strip())
        out.extend(x.strip() for x in re.split(r'[,;]',line) if x.strip())
    return list(dict.fromkeys(out))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--event',required=True); args=ap.parse_args()
    event=json.loads(Path(args.event).read_text(encoding='utf-8')); issue=event['issue']
    sections=parse_sections(issue.get('body',''))
    def value(k): return clean(sections.get(LABELS[k],''))
    vocab=load_vocab(); reverse=reverse_label_maps(vocab)
    name=value('name')
    if not name: raise ValueError('Strategy name is missing')
    slug=slugify(name); path=STRATEGIES_DIR/f'{slug}.yml'
    if path.exists(): raise ValueError(f'An entry already exists at {path}. Suggest an update instead.')
    summary=value('summary')
    if len(summary)>700: summary=summary[:697].rstrip()+'...'
    date_created=issue.get('created_at',str(date.today()))[:10]
    platforms=map_values(selected(value('platforms')),reverse['platforms'],'platform')
    objective=map_values([value('objective')],reverse['strategy_objectives'],'strategy objective')[0]
    role=map_values([value('role')],reverse['strategy_submission_roles'],'submitter role')[0]
    analysis=map_values(selected(value('analysis_types')),reverse['analysis_types'],'analysis type') if value('analysis_types') else []
    sample_types=map_values(selected(value('sample_types')),reverse['sample_types'],'sample type') if value('sample_types') else []
    biological_contexts=map_values(selected(value('biological_contexts')),reverse['biological_contexts'],'biological context') if value('biological_contexts') else []
    organisms=split_tools(value('organisms')) if value('organisms') else []
    components=map_values(selected(value('components')),reverse['strategy_components'],'strategy component') if value('components') else []
    if not components: components=['data_acquisition']

    pub_text=value('publication'); publication={}
    doi=re.search(r'10\.\d{4,9}/\S+',pub_text,re.I)
    if doi: publication['doi']=doi.group(0).rstrip('.,;)')
    if re.match(r'https?://',pub_text): publication['url']=pub_text
    if not publication and pub_text: publication['citation']=pub_text

    # Link tool names to existing catalogue entries when possible.
    tool_records=load_tools(); lookup={}
    for t in tool_records:
        lookup[(t.get('name') or '').casefold()]=t['slug']
        lookup[t['slug'].casefold()]=t['slug']
        if t.get('acronym'): lookup[t['acronym'].casefold()]=t['slug']
        for alias in t.get('aliases',[]): lookup[alias.casefold()]=t['slug']
    tools=[]
    for item in split_tools(value('tools')):
        matched=lookup.get(item.casefold())
        tools.append({'slug':matched} if matched else {'name':item})

    attribution=parse_attribution(sections)
    submitter_name=attribution['submitter_name']; submitter_orcid=attribution.get('submitter_orcid')
    provenance={'submitted_by':role,'source_issue':issue['html_url'],'author_verified':False}
    provenance.update(attribution)
    if submitter_name: provenance['submitter_name']=submitter_name
    if submitter_orcid: provenance['submitter_orcid']=submitter_orcid
    if value('notes'): provenance['notes']=value('notes')[:1000]

    record={
      '$schema':'../../schemas/strategy.schema.json','slug':slug,'name':name,'summary':summary,
      'publication':publication,'purpose':{'primary':objective,'secondary':[]},'platforms':platforms,
      'analysis_types':analysis,'sample_types':sample_types,'biological_contexts':biological_contexts,'organisms':organisms,'components':components,'workflow_steps':[],
      'tools':tools,'resources':{},'scope':{},'related_strategies':[],'provenance':provenance,
      'status':{'entry':'stub','review':'unreviewed','created_at':date_created,'updated_at':date_created,'last_verified':date_created}
    }
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(yaml.safe_dump(record,sort_keys=False,allow_unicode=True,width=1000),encoding='utf-8')
    output=os.getenv('GITHUB_OUTPUT')
    if output:
        with open(output,'a',encoding='utf-8') as h:
            h.write(f'path={path.relative_to(ROOT).as_posix()}\nslug={slug}\nname={name}\ntype=strategy\n')
    print(path.relative_to(ROOT))

if __name__=='__main__': main()
