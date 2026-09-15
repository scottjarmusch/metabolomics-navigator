"""Deterministic metadata for the static catalogue's rendered routes."""
from urllib.parse import urlsplit


def page_metadata(template, route, context, absolute_url):
    site = context['site']
    brand = site['title']
    title, description = brand, site['description']
    record = context.get('tool') or context.get('strategy')
    if record:
        title, description = record['name'], record['summary']
    elif template == 'guide.html':
        title, description = context['group']['title'], context['group']['introduction']
    elif context.get('page'):
        title = context['page']['title']
        description = context['page']['description']
    defaults = {
        'tools.html': ('Metabolomics Tools', 'Search and filter MS-based metabolomics tools by scientific function, platform, interface and access model.'),
        'strategies.html': ('Analytical Strategies', 'Explore published, transferable MS-based metabolomics strategies and the tools used to implement them.'),
        'submit.html': ('Contribute', 'Suggest a metabolomics tool or analytical strategy, improve an entry, and meet the community contributors.'),
        'browse.html': ('Browse categories', 'Browse metabolomics tools and analytical strategies by scientific function, platform and biological context.'),
        'about.html': ('About', 'Learn about Metabolomics Navigator, its MS-based scope, community contributions and editorial approach.'),
        'ask.html': ('Ask Navigator · Beta', 'Preview the planned guided metabolomics workflow builder, grounded in the Navigator catalogue.'),
        '404.html': ('Page not found', 'This page could not be found. Explore the Metabolomics Navigator catalogue.'),
    }
    title, description = defaults.get(template, (title, description))
    title = f'{title} | {brand}'
    if template == 'home.html':
        title = site['homepage_title']
        description = site['homepage_description']
    canonical = absolute_url(route)
    parsed = urlsplit(canonical)
    if parsed.scheme not in ('https', 'http') or not parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError(f'Invalid absolute canonical URL: {canonical}')
    data = None
    if template == 'home.html':
        data = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'WebSite', '@id': canonical+'#website', 'name': brand,
             'url': canonical, 'description': description, 'inLanguage': 'en',
             'about': {'@id': canonical+'#project'}},
            {'@type': 'CreativeWork', '@id': canonical+'#project', 'name': brand,
             'url': canonical, 'description': description,
             'sameAs': context['repository_url'], 'isPartOf': {'@id': canonical+'#website'},
             'about': [{'@type': 'Thing', 'name': 'Metabolomics'},
                       {'@type': 'Thing', 'name': 'Mass spectrometry'}]},
        ]}
    return {'title': title, 'description': description,
            'canonical': None if template == '404.html' else canonical,
            'robots': 'noindex,follow' if template == '404.html' else 'index,follow',
            'structured_data': data}
