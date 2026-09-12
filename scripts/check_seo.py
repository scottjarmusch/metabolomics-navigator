"""Check generated SEO metadata and canonical/sitemap agreement without a browser."""
import argparse
import json
import os
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree
from common import ROOT, derive_base_path
from build_site import load_yaml


class Head(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []; self.titles = []; self.ld = []; self.capture = None; self.head = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        if tag == 'head': self.head = True
        if not self.head: return
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if tag == 'title': self.titles.append(''); self.capture = self.titles
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.ld.append(''); self.capture = self.ld

    def handle_endtag(self, tag):
        if tag in ('title', 'script'): self.capture = None
        if tag == 'head': self.head = False

    def handle_data(self, data):
        if self.capture is not None: self.capture[-1] += data

    def values(self, tag, key, value, field='content'):
        return [a.get(field, '') for t, a in self.tags if t == tag and a.get(key) == value]


def check(out, origin, base_path):
    base = origin.rstrip('/') + base_path + '/'
    sitemap = [e.text for e in ElementTree.parse(out/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    assert len(sitemap) == len(set(sitemap)), 'Duplicate sitemap URLs'
    canonical_urls = set()
    for file in out.rglob('*.html'):
        route = file.relative_to(out).as_posix()
        head = Head(file.read_text(encoding='utf-8'))
        def one(tag, key, value, field='content'):
            values = head.values(tag,key,value,field)
            assert len(values) == 1 and values[0].strip(), f'{route}: missing/duplicate {value}'
            return values[0]
        assert len(head.titles) == 1 and head.titles[0].strip(), f'{route}: title'
        description = one('meta','name','description')
        robots = one('meta','name','robots')
        if route == '404.html':
            assert robots == 'noindex,follow'
            assert not head.values('link','rel','canonical','href')
            continue
        expected = base + (route[:-10] if route.endswith('index.html') else route)
        canonical = one('link','rel','canonical','href')
        assert canonical == expected, f'{route}: {canonical} != {expected}'
        assert urlsplit(canonical).scheme in ('http','https') and urlsplit(canonical).netloc
        assert robots == 'index,follow', route
        assert canonical not in canonical_urls, f'Duplicate canonical {canonical}'
        canonical_urls.add(canonical)
        assert one('meta','property','og:url') == canonical
        assert one('meta','property','og:title') == head.titles[0]
        assert one('meta','property','og:description') == description
        assert one('meta','property','og:type') == 'website'
        assert one('meta','property','og:site_name') == 'Metabolomics Navigator'
        assert one('meta','name','twitter:card') == 'summary'
        assert one('meta','name','twitter:title') == head.titles[0]
        assert one('meta','name','twitter:description') == description
        for block in head.ld: json.loads(block)
        if route == 'index.html':
            assert len(head.ld) == 1
            data = json.loads(head.ld[0]); assert data['@context'] == 'https://schema.org'
            nodes = {item['@type']:item for item in data['@graph']}
            assert {'WebSite','CreativeWork'} <= nodes.keys()
            assert nodes['WebSite']['name'] == 'Metabolomics Navigator'
            assert nodes['WebSite']['url'] == canonical
            assert nodes['WebSite']['description'] == description
    assert canonical_urls == set(sitemap), 'Canonical pages differ from sitemap'
    robots = (out/'robots.txt').read_text(encoding='utf-8')
    assert 'Allow: /' in robots and 'Sitemap: '+base+'sitemap.xml' in robots
    print(f'SEO checks passed: {len(canonical_urls)} canonical pages, sitemap agreement, social metadata, JSON-LD and noindex 404.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(); parser.add_argument('--base-path'); parser.add_argument('--site-url')
    args = parser.parse_args()
    origin = args.site_url or os.getenv('SITE_URL')
    if not origin and os.getenv('GITHUB_REPOSITORY'):
        origin = 'https://' + os.environ['GITHUB_REPOSITORY'].split('/')[0].lower()+'.github.io'
    origin = origin or load_yaml(ROOT/'config/site.yml')['site_url']
    check(ROOT/'dist',origin,derive_base_path(args.base_path))
