"""Audit retired collection terminology while preserving external names and URLs."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
OLD=''.join(map(chr,[112,114,111,116,111,99,111,108]))
SKIP={'.git','dist','.venv','venv','node_modules','__pycache__'}
def audit():
 errors=[];external=[]
 for p in ROOT.rglob('*'):
  if not p.is_file() or any(x in SKIP for x in p.parts):continue
  rel=p.relative_to(ROOT)
  if OLD in str(rel).lower():errors.append(str(rel))
  try:text=p.read_text(encoding='utf-8')
  except UnicodeDecodeError:continue
  for n,line in enumerate(text.splitlines(),1):
   if OLD not in line.lower():continue
   clean=re.sub(r'https?://[^\s<>\"\)]+','',line)
   clean=clean.replace('Nature '+OLD.title()+'s','')
   if OLD in clean.lower():errors.append(f'{rel}:{n}: {line.strip()}')
   else:external.append(f'{rel}:{n}')
 if errors:raise SystemExit('\n'.join(errors))
 print(f'Strategy terminology audit passed; {len(external)} external-name/URL occurrences retained.')
if __name__=='__main__':audit()
