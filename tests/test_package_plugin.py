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
        files=set(m.source_map(ROOT).values()) | {m.SCOPE,m.SERVICE_SCOPE,'scripts/package_plugin.py'}
        for name in files:
            dst=self.source/name;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/name,dst)
        self.out=self.base/'output/cad-workbench'
    def build(self):return m.build(self.source,self.out,'0'*40)
    def test_relocated_readback(self):
        self.build();new=self.base/'relocated/cad-workbench';new.parent.mkdir();shutil.move(self.out,new);m.validate_package(new)
    def test_simulator_source_transfer_excludes_generated_and_private_state(self):
        contaminants = ('apps/playground/build/index.js', 'apps/playground/.svelte-kit/generated.js',
                        'apps/playground/node_modules/private.js', '.workbench/simulators.json',
                        'apps/playground/src/.env', 'apps/playground/src/private.png')
        for name in contaminants:
            path=self.source/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text('private sentinel')
        self.build()
        for name in contaminants:self.assertFalse((self.out/name).exists(),name)
        for name in ('apps/playground/src/app.html','apps/playground/src/routes/+page.svelte',
                     'apps/playground/scripts/register.mjs','apps/playground/SERVICE.md',
                     'scripts/simulator_service.py','package.json','package-lock.json'):
            self.assertEqual((self.source/name).read_bytes(),(self.out/name).read_bytes(),name)
    def test_missing_simulator_service_blocks_package_before_output(self):
        (self.source/'scripts/simulator_service.py').unlink()
        with self.assertRaisesRegex(ValueError,'missing'):self.build()
        self.assertFalse(self.out.exists())
    def test_simulator_source_symlink_refused(self):
        (self.source/'apps/playground/src/escaped.js').symlink_to(self.source/'package.json')
        with self.assertRaisesRegex(ValueError,'symlink'):self.build()
        self.assertFalse(self.out.exists())
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
