"""Add the built Education preview to an existing alpha snapshot, preserving Ask."""
import argparse
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('target', type=Path)
args = parser.parse_args()
target = args.target.resolve()
assert (target / 'ask/index.html').is_file(), 'Expected an existing alpha snapshot'
assert 'Disallow: /' in (target / 'robots.txt').read_text(), 'Expected noindex alpha'
base = '/metabolomics-navigator-alpha/'
page = (ROOT / 'dist/education/index.html').read_text(encoding='utf-8')
assert base in page
page = page.replace('content="index,follow"', 'content="noindex,follow"')
version = hashlib.sha256((ROOT/'assets/site.js').read_bytes() + (ROOT/'assets/product-refresh.css').read_bytes()).hexdigest()[:12]
page = page.replace('</head>', f'<link rel="stylesheet" href="{base}assets/education-alpha.css?v={version}">\n</head>')
page = page.replace('</body>', f'<script src="{base}assets/education-alpha.js?v={version}" defer></script>\n</body>')
page = re.sub(r'(<body[^>]*>)', r'\1<aside style="padding:12px;text-align:center;background:#f2e9cc;color:#183f42">Alpha review snapshot Â· Not the live site Â· <a href="https://scottjarmusch.github.io/metabolomics-navigator/">Visit the live Navigator</a></aside>', page, count=1)
(target / 'education').mkdir(exist_ok=True)
(target / 'education/index.html').write_text(page, encoding='utf-8')
css = (ROOT / 'assets/product-refresh.css').read_text(encoding='utf-8').split('/* Education alpha:', 1)[1]
(target / 'assets/education-alpha.css').write_text('/* Education alpha:' + css, encoding='utf-8')
js = (ROOT / 'assets/site.js').read_text(encoding='utf-8').split('const educationDirectory', 1)[1]
(target / 'assets/education-alpha.js').write_text('const educationDirectory' + js, encoding='utf-8')
# Only add navigation links to existing pages; do not replace their content or scripts.
for path in target.rglob('*.html'):
    raw = path.read_bytes()
    text = raw.decode('utf-8')
    if f'href="{base}education/"' in text:
        continue
    pattern = rf'(<a href="{base}strategies/"[^>]*>Strategies</a>)'
    active = ' aria-current="page"' if path == target / 'education/index.html' else ''
    text = re.sub(pattern, rf'\1\n        <a href="{base}education/"{active}>Education <small>Alpha</small></a>', text)
    if text != raw.decode('utf-8'):
        path.write_bytes(text.encode('utf-8'))
print('Staged Education and navigation only; existing Ask content and assets preserved.')
