"""Credible failures: tampered policy, unknown recipe capability and escaped reference."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('registry_checker',ROOT/'scripts/check_registry.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        for folder in ('catalog','contracts','workflows','skills','templates','docs/iterations/2026-09-06-foundation','scripts'):
            shutil.copytree(ROOT/folder,self.root/folder,dirs_exist_ok=True)
        shutil.copy2(ROOT/'README.md',self.root/'README.md')
        for name in ('SERVICE.md', 'README.md'):
            target = self.root/'apps/simulator'/name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT/'apps/simulator'/name, target)
    def test_clean(self):self.assertEqual(module.check(self.root),[])
    def test_policy_tamper(self):
        p=self.root/'workflows/cad-fabrication.md';p.write_text(p.read_text()+'\nchanged\n')
        self.assertTrue(any('hash mismatch' in e for e in module.check(self.root)))
    def test_unknown_capability(self):
        p=self.root/'catalog/registry.json';data=json.loads(p.read_text());data['workflows'][0]['capabilities'].append('CAP-NOT-REAL');p.write_text(json.dumps(data))
        self.assertIn('unknown capability reference',module.check(self.root))
    def test_escape(self):
        p=self.root/'catalog/registry.json';data=json.loads(p.read_text());data['workflows'][0]['recipe']='../outside.md';p.write_text(json.dumps(data))
        self.assertTrue(any('escaping local path' in e for e in module.check(self.root)))
if __name__=='__main__':unittest.main()
