import json,pathlib,unittest,importlib.util,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
class DataTests(unittest.TestCase):
 def setUp(self):self.d=json.loads((ROOT/'data/observatory.json').read_text())
 def test_stable_ids_unique(self):
  ids=[x['id'] for group in ['sources','questions','signals','scenarios'] for x in self.d[group]];self.assertEqual(len(ids),len(set(ids)))
 def test_questions_have_distinct_options_and_evidence(self):
  sources={s['id'] for s in self.d['sources']}
  for q in self.d['questions']:
   self.assertGreaterEqual(len(q['options']),2);self.assertTrue(set(q['refs'])<=sources);self.assertTrue(q['refs'])
   self.assertEqual(len(q['options']),len({x['id'] for x in q['options']}))
   for key in ['known','unknown','judgment','change_if','next','scenario']:self.assertTrue(q[key])
   self.assertIn('示意',q['scenario'])
 def test_sources_have_boundaries(self):
  for s in self.d['sources']:
   self.assertTrue(s['url'].startswith('https://'));self.assertTrue(s['boundary']);self.assertRegex(s['checked'],r'^\d{4}-\d{2}-\d{2}$')
 def test_local_assets_exist(self):
  html=(ROOT/'website/index.html').read_text()
  for path in re.findall(r'(?:src|href)="\./([^"]+)"',html):self.assertTrue((ROOT/'website'/path).is_file(),path)
 def test_no_private_identifiers_or_trackers(self):
  data=(ROOT/'data/observatory.json').read_text()
  for value in ['hotmail.com','gmail.com','recloud.com','Authorization:','Bearer ','Sentinel_']:self.assertNotIn(value,data)
  self.assertNotIn('googletagmanager',(ROOT/'website/index.html').read_text())
 def test_generated_output_current(self):
  spec=importlib.util.spec_from_file_location('build',ROOT/'scripts/build.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
  for p,content in mod.products().items():self.assertEqual((ROOT/p).read_text(),content)
if __name__=='__main__':unittest.main()
