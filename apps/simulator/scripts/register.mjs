import { readFile, writeFile, readdir, realpath, mkdir, lstat, rename } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { digest, confined, loadRegistry } from '../src/lib/server/registry.js';
const args = new Map();
for (let i=2;i<process.argv.length;i+=2) { if (!process.argv[i].startsWith('--') || !process.argv[i+1]) throw new Error('Expected --name value pairs'); args.set(process.argv[i].slice(2),process.argv[i+1]); }
for (const key of ['id','title','asset-root','source-root','source-entry']) if (!args.has(key)) throw new Error('Required --'+key);
const config = path.resolve(args.get('config') || '.workbench/simulators.json');
const assetRoot=await realpath(args.get('asset-root')), sourceRoot=await realpath(args.get('source-root'));
const sourceFile=await confined(sourceRoot,args.get('source-entry'));
const assets={};
async function scan(dir) { for (const item of await readdir(dir,{withFileTypes:true})) { const full=path.join(dir,item.name); if ((await lstat(full)).isSymbolicLink()) throw new Error('Register only real built files, no symlinks'); if(item.isDirectory()) await scan(full); else if(item.isFile()) assets[path.relative(assetRoot,full).split(path.sep).join('/')]=digest(await readFile(full)); } }
await scan(assetRoot);
const sim={id:args.get('id'),title:args.get('title'),description:args.get('description')||'',assetRoot,entrypoint:args.get('entrypoint')||'index.html',assets,source:{root:sourceRoot,entrypoint:args.get('source-entry'),revision:execFileSync('git',['rev-parse','HEAD'],{cwd:sourceRoot,encoding:'utf8'}).trim(),sha256:digest(await readFile(sourceFile))}};
let raw={version:1,allowedRoots:[],simulators:[]};try{raw=JSON.parse(await readFile(config,'utf8'));}catch(e){if(e.code!=='ENOENT')throw e;}
if(raw.simulators.some(s=>s.id===sim.id))throw new Error('ID exists; preserve or intentionally edit the existing registration first');
raw.allowedRoots=[...new Set([...raw.allowedRoots,assetRoot])];raw.simulators.push(sim);
await mkdir(path.dirname(config),{recursive:true});
const candidate=config+'.candidate-'+process.pid;
await writeFile(candidate,JSON.stringify(raw,null,2)+'\n',{flag:'wx'});
const checked = await loadRegistry(candidate);
const added = checked.find(item => item.id === sim.id);
if (!added?.available) throw new Error('New registration unavailable: ' + added?.reason);
// Explicit local registration is the only write interface. No HTTP mutation route.
await rename(candidate, config);
console.log(JSON.stringify({id:sim.id,source:sim.source,assets:Object.keys(assets).length,config},null,2));
