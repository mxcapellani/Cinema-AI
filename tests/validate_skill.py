from pathlib import Path
import re,sys,yaml
B=Path('.agents/skills/cinema-ai')
NAMES=['image-analysis','automatic-camera','character-performance','prompt-generation','creative-camera']
LABELS=['Prompt A — Análise visual','Prompt B — Seleção automática de câmera','Prompt C — Atuação de personagens','Prompt D — Construção do prompt final','Prompt E — Modo criativo']
def validate_output(t,count=2):
 en=re.findall(r'^🎬 Opção (\d+) \(EN\): (.+)$',t,re.M);pt=re.findall(r'^📘 Tradução \(PT\): (.+)$',t,re.M)
 return [i for i,p in en]==[str(i) for i in range(1,count+1)] and len(pt)==count and all(len(p)>40 and not re.search(r'\b(epic|masterpiece|HD)\b',p,re.I) for i,p in en)
def validate(root):
 root=Path(root);e=[]
 for p in ('README.md','LICENSE','docs/SOURCE_SPECIFICATION.md','tests/acceptance-tests.md',str(B/'SKILL.md')):
  if not (root/p).is_file() or not (root/p).read_text().strip():e.append('missing '+p)
 if e:return e
 text=(root/B/'SKILL.md').read_text()
 try:
  assert text.startswith('---\n');d=yaml.safe_load(text.split('---',2)[1]);assert d['name']=='cinema-ai' and isinstance(d['description'],str) and len(d['description'])>60
 except Exception:e.append('invalid YAML')
 source=(root/'docs/SOURCE_SPECIFICATION.md').read_text()
 for i,n in enumerate(NAMES):
  end=source.index(LABELS[i+1]) if i<4 else source.index('4. Catálogo de movimentos de câmera')
  original=source[source.index(LABELS[i]):end].strip()
  p=root/B/f'prompts/{n}.md'
  if not p.exists() or original not in p.read_text() or original not in text:e.append('auxiliary prompt differs '+n)
 for p in root.rglob('*.md'):
  for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
   if '://' in link or link.startswith('#'):continue
   target=(p.parent/link.split('#')[0]).resolve()
   if not target.is_relative_to(root.resolve()) or not target.exists():e.append('bad link '+link)
 for n in ('portrait-complete','manual-product','landscape-complete'):
  p=root/f'examples/{n}.md'
  if not p.exists() or not validate_output(p.read_text()):e.append('bad output '+n)
 for i in range(1,19):
  if f'## T{i:02d} —' not in (root/'tests/acceptance-tests.md').read_text():e.append('missing case')
 return e
if __name__=='__main__':
 e=validate(Path(__file__).resolve().parents[1]);print('\n'.join(e) if e else 'PASS: package, YAML, links, original A–E and output examples');sys.exit(bool(e))
