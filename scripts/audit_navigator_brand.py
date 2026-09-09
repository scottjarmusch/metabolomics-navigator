"""Audit retired product branding without rewriting external scientific names."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
OLD=''.join(map(chr,[97,116,108,97,115]))
SKIP={'.git','dist','.venv','venv','node_modules','__pycache__'}
def audit():
 errors=[]
 for p in ROOT.rglob('*'):
  if not p.is_file() or any(x in SKIP for x in p.parts):continue
  try:text=p.read_text(encoding='utf-8')
  except UnicodeDecodeError:continue
  for n,line in enumerate(text.splitlines(),1):
   if OLD not in line.lower():continue
   clean=re.sub(r'https?://[^\s<>\"\)]+','',line.lower())
   for prefix in ['natural products ','natural-products-','natural product ','dreams ','a lipidome ','the lipidome ']:clean=clean.replace(prefix+OLD,'')
   if OLD in clean:errors.append(f'{p.relative_to(ROOT)}:{n}: {line.strip()}')
 if errors:raise SystemExit('\n'.join(errors))
 print('Navigator brand terminology audit passed.')
if __name__=='__main__':audit()
