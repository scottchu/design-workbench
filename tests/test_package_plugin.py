"""Package boundary tests: relocation, tampering, missing dependencies and symlinks."""
import importlib.util
import shutil
import tempfile
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('package_plugin',ROOT/'scripts/package_plugin.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class PackageTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name).resolve();self.source=self.base/'source';self.source.mkdir()
        files=set(m.source_map(ROOT).values()) | {m.SCOPE,'scripts/package_plugin.py'}
        for name in files:
            dst=self.source/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/name,dst)
        self.out=self.base/'output/cad-workbench'
    def build(self):return m.build(self.source,self.out,'0'*40)
    def test_relocated_readback(self):
        self.build();new=self.base/'relocated/cad-workbench';new.parent.mkdir();shutil.move(self.out,new);m.validate_package(new)
    def test_tampered_output(self):
        self.build();(self.out/'skills/workbench-flow/SKILL.md').write_text('changed')
        with self.assertRaisesRegex(ValueError,'hash mismatch'):m.validate_package(self.out)
    def test_missing_support(self):
        (self.source/'fixtures/smoke/plate.py').unlink()
        with self.assertRaisesRegex(ValueError,'missing'):self.build()
        self.assertFalse(self.out.exists())
    def test_escaping_symlink(self):
        p=self.source/'skills/escape';p.symlink_to(self.base,target_is_directory=True)
        with self.assertRaisesRegex(ValueError,'symlink'):self.build()
        self.assertFalse(self.out.exists())
    def test_existing_output_preserved(self):
        self.build();before=m.digest(self.out/'PACKAGE_RECEIPT.json')
        with self.assertRaisesRegex(ValueError,'already exists'):self.build()
        self.assertEqual(before,m.digest(self.out/'PACKAGE_RECEIPT.json'))
if __name__=='__main__':unittest.main()
