import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, mkdir, writeFile, symlink, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { loadRegistry, readAsset, digest, relativeAsset, publicSimulator } from '../src/lib/server/registry.js';
async function fixture() {
  const root = await mkdtemp(path.join(os.tmpdir(), 'workbench-host-test-')), assets = path.join(root,'assets'); await mkdir(assets);
  await writeFile(path.join(root,'source.scad'),'cube(1);'); await writeFile(path.join(assets,'index.html'),'<html>real fixture</html>'); await writeFile(path.join(assets,'engine.wasm'),Buffer.from([0,97,115,109]));
  const sim = { id:'example', title:'Example', assetRoot:assets, entrypoint:'index.html', assets:{ 'index.html':digest('<html>real fixture</html>'), 'engine.wasm':digest(Buffer.from([0,97,115,109])) }, source:{ root, entrypoint:'source.scad', revision:'a'.repeat(40), sha256:digest('cube(1);') } };
  const config = path.join(root,'registry.json'), raw = { version:1, allowedRoots:[assets], simulators:[sim] };
  const save = () => writeFile(config,JSON.stringify(raw)); await save(); return { root, assets, config, raw, sim, save };
}
test('serves only registered exact bytes with correct WASM MIME and hash', async () => { const f=await fixture(); const [sim]=await loadRegistry(f.config); const a=await readAsset(sim,'engine.wasm'); assert.equal(a.mime,'application/wasm'); assert.equal(digest(a.bytes),sim.assets['engine.wasm']); });
test('rejects traversal, hidden, absolute, backslash and encoded paths', () => { for(const value of ['../secret','a/../secret','/etc/passwd','.env','a\\b','%2e%2e/secret','a//b']) assert.throws(()=>relativeAsset(value)); });
test('rejects unregistered roots and duplicate IDs', async () => { const f=await fixture(); f.raw.allowedRoots=[f.root]; await f.save(); assert.match((await loadRegistry(f.config))[0].reason,/Unregistered/); f.raw.allowedRoots=[f.assets]; f.raw.simulators.push(f.sim);await f.save();await assert.rejects(loadRegistry(f.config),/duplicate/); });
test('rejects symlink escapes even with matching registered hash', async () => { const f=await fixture(); await writeFile(path.join(f.root,'secret.js'),'secret');await symlink(path.join(f.root,'secret.js'),path.join(f.assets,'escape.js'));f.sim.assets['escape.js']=digest('secret'); await assert.rejects(readAsset(f.sim,'escape.js'),/escapes/); });
test('refuses changed source, changed output, and unlisted files', async () => { const f=await fixture();await writeFile(path.join(f.root,'source.scad'),'cube(2);');assert.match((await loadRegistry(f.config))[0].reason,/source changed/);await writeFile(path.join(f.assets,'index.html'),'changed');await assert.rejects(readAsset(f.sim,'index.html'),/artifact changed/);await assert.rejects(readAsset(f.sim,'secret.js'),/not registered/); });
test('refuses unsupported asset MIME and source symlink escape', async () => { const f=await fixture();await writeFile(path.join(f.assets,'secret.env'),'x');f.sim.assets['secret.env']=digest('x');await assert.rejects(readAsset(f.sim,'secret.env'),/Unsupported/); const other=await mkdtemp(path.join(os.tmpdir(),'outside-host-'));await writeFile(path.join(other,'source.scad'),'cube(1);');await symlink(path.join(other,'source.scad'),path.join(f.root,'escape.scad'));f.sim.source.entrypoint='escape.scad';await f.save();assert.match((await loadRegistry(f.config))[0].reason,/escapes/); });

test('source drift and missing roots isolate unavailable A while healthy B stays listed and readable', async () => {
  const a=await fixture(), b=await fixture(); b.sim.id='healthy';
  a.raw.simulators.push(b.sim);a.raw.allowedRoots.push(b.assets);await a.save();
  for (const breakA of [() => writeFile(path.join(a.root,'source.scad'),'changed'), () => rm(a.assets,{recursive:true})]) {
    await breakA(); const entries=await loadRegistry(a.config), list=entries.map(publicSimulator);
    assert.equal(list.length,2);assert.equal(list[0].available,false);assert.match(list[0].reason,/changed|missing/);assert.equal(list[1].available,true);
    await assert.rejects(readAsset(entries[0],'index.html'),/unavailable/);
    assert.equal((await readAsset(entries[1],'index.html')).bytes.toString(),'<html>real fixture</html>');
  }
});
test('CLI adds healthy C without rewriting stale A or blocking healthy B', async () => {
  const a=await fixture(), b=await fixture(), c=await fixture();b.sim.id='healthy';
  a.raw.simulators.push(b.sim);a.raw.allowedRoots.push(b.assets);await a.save();
  await writeFile(path.join(a.root,'source.scad'),'changed');
  const repo=path.resolve(import.meta.dirname,'../../..');
  const result=execFileSync(process.execPath,[path.join(repo,'apps/playground/scripts/register.mjs'),'--id','added','--title','Added','--asset-root',c.assets,'--source-root',repo,'--source-entry','apps/playground/src/app.html','--config',a.config],{encoding:'utf8'});
  assert.equal(JSON.parse(result).id,'added');
  const entries=await loadRegistry(a.config);assert.deepEqual(entries.map(s=>[s.id,s.available]),[['example',false],['healthy',true],['added',true]]);
  await assert.rejects(readAsset(entries[0],'index.html'),/unavailable/);
  assert.equal((await readAsset(entries[2],'index.html')).bytes.toString(),'<html>real fixture</html>');
});
