import unittest,tempfile,shutil
from pathlib import Path
from validate_skill import validate,validate_output,B
ROOT=Path(__file__).resolve().parents[1]
class Tests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.r=Path(t.name)/'repo';shutil.copytree(ROOT,self.r)
 def change(self,p,a,b):
  q=self.r/p;q.write_text(q.read_text().replace(a,b,1))
 def test_valid(self):self.assertEqual(validate(self.r),[])
 def test_name(self):
  self.change(B/'SKILL.md','name: cinema-ai','name: other');self.assertTrue(validate(self.r))
 def test_missing_reference(self):
  (self.r/B/'references/quality-rules.md').unlink();self.assertTrue(validate(self.r))
 def test_missing_original_prompt(self):
  self.change(B/'prompts/image-analysis.md','Analyze the provided image','Abridged');self.assertTrue(validate(self.r))
 def test_missing_translation(self):
  self.change('examples/manual-product.md','📘 Tradução (PT):','Removed:');self.assertTrue(validate(self.r))
 def test_banned_word(self):
  self.change('examples/portrait-complete.md','Slowly push','epic Slowly push');self.assertTrue(validate(self.r))
 def test_missing_second_option(self):
  self.change('examples/portrait-complete.md','🎬 Opção 2 (EN):','Removed:');self.assertTrue(validate(self.r))
 def test_missing_case(self):
  self.change('tests/acceptance-tests.md','## T18 —','## Removed —');self.assertTrue(validate(self.r))
 def test_missing_source(self):
  (self.r/'docs/SOURCE_SPECIFICATION.md').unlink();self.assertTrue(validate(self.r))
 def test_case_insensitive_banned(self):
  t=(ROOT/'examples/portrait-complete.md').read_text().replace('Slowly push','MASTERPIECE Slowly push');self.assertFalse(validate_output(t))
if __name__=='__main__':unittest.main()
