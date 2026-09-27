from pathlib import Path
import re,shutil,subprocess
root=Path('.').resolve();out=root/'dist';target=root.parent/'navigator-alpha-published'
remote=subprocess.check_output(['git','-C',str(target),'remote','get-url','origin'],text=True).strip()
assert remote=='https://github.com/scottjarmusch/metabolomics-navigator-alpha.git'
assert (out/'ask/index.html').exists()
assert 'What you need for this Strategy' in (out/'ask/index.html').read_text(encoding='utf-8')
for source in out.rglob('*'):
 if not source.is_file():continue
 dest=target/source.relative_to(out);dest.parent.mkdir(parents=True,exist_ok=True)
 if source.suffix=='.html':
  s=source.read_text(encoding='utf-8').replace('content="index,follow"','content="noindex,follow"')
  s=re.sub(r'(<body[^>]*>)',r'\1<aside style="padding:12px;text-align:center;background:#f2e9cc;color:#183f42">Alpha review snapshot · Not the live site · <a href="https://scottjarmusch.github.io/metabolomics-navigator/">Visit the live Navigator</a></aside>',s,count=1)
  dest.write_bytes(s.encode())
 else:shutil.copyfile(source,dest)
(target/'robots.txt').write_bytes(b'User-agent: *\nDisallow: /\n')
(target/'.nojekyll').touch()
(target/'README.md').write_bytes(b'# Metabolomics Navigator alpha preview\n\nStrategy-first Ask Navigator plus Education. 34 Strategies, 143 tools and 57 learning resources.\n\nAsk: https://scottjarmusch.github.io/metabolomics-navigator-alpha/ask/\n\nEducation: https://scottjarmusch.github.io/metabolomics-navigator-alpha/education/\n\nSource branch: codex/ask-education-alpha in scottjarmusch/metabolomics-navigator. Production unchanged.\n')
print('Refreshed separate alpha snapshot with noindex pages.')
