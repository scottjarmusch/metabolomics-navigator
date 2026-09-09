"""Check generated local links and fragments for root or GitHub Pages builds."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse
from common import derive_base_path

ROOT=Path(__file__).resolve().parents[1]/'dist'
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.ids=set(); self.links=[]; self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for attr in ('href','src'):
            if attr in attrs: self.links.append(attrs[attr])

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--base-path',default=None); args=parser.parse_args()
    base=derive_base_path(args.base_path).rstrip('/')
    pages={p:Page(p.read_text(encoding='utf-8')) for p in ROOT.rglob('*.html')}
    if not pages: raise SystemExit('No generated pages found. Build the site before checking links.')
    errors=[]; checked=0
    for path,page in pages.items():
        for link in page.links:
            u=urlsplit(link)
            if u.scheme or u.netloc: continue
            target=unquote(u.path)
            if target.startswith('/'):
                if base and not target.startswith(base+'/'):
                    errors.append(f'{path.relative_to(ROOT)}: outside base path: {link}'); continue
                dest=ROOT/target[len(base):].lstrip('/')
            else: dest=(path.parent/target) if target else path
            if dest.is_dir(): dest=dest/'index.html'
            dest=dest.resolve(); checked+=1
            if not dest.exists(): errors.append(f'{path.relative_to(ROOT)}: missing {link}')
            elif u.fragment and dest in pages and unquote(u.fragment) not in pages[dest].ids:
                errors.append(f'{path.relative_to(ROOT)}: missing fragment {link}')
    if errors: raise SystemExit('\n'.join(errors))
    print(f'Checked {checked} local links and fragments across {len(pages)} pages.')
if __name__=='__main__': main()
