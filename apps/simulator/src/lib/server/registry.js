import { readFile, realpath, stat } from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';
export const digest = (bytes) => createHash('sha256').update(bytes).digest('hex');
const hashPattern = /^[a-f0-9]{64}$/;
const types = { '.html':'text/html; charset=utf-8', '.js':'text/javascript; charset=utf-8', '.mjs':'text/javascript; charset=utf-8', '.css':'text/css; charset=utf-8', '.json':'application/json', '.wasm':'application/wasm', '.svg':'image/svg+xml', '.png':'image/png', '.jpg':'image/jpeg', '.jpeg':'image/jpeg', '.webp':'image/webp', '.woff2':'font/woff2', '.stl':'model/stl', '.glb':'model/gltf-binary', '.scad':'text/plain; charset=utf-8' };
export function relativeAsset(name) {
  if (typeof name !== 'string' || !name || name.includes('\\') || name.includes('%') || name.includes('\0') || path.isAbsolute(name) || name.split('/').some(x => !x || x === '.' || x === '..' || x.startsWith('.'))) throw new Error('Invalid asset path');
  return name;
}
export async function confined(root, name) {
  relativeAsset(name);
  const base = await realpath(root), file = await realpath(path.join(base, name));
  if (!file.startsWith(base + path.sep) || !(await stat(file)).isFile()) throw new Error('Asset escapes registered root');
  return file;
}
export async function loadRegistry(configPath = process.env.WORKBENCH_SIMULATORS || path.resolve('../../.workbench/simulators.json')) {
  let raw;
  try { raw = JSON.parse(await readFile(configPath, 'utf8')); } catch (e) { if (e.code === 'ENOENT') return []; throw new Error('Cannot read simulator registration'); }
  if (raw.version !== 1 || !Array.isArray(raw.allowedRoots) || !Array.isArray(raw.simulators)) throw new Error('Invalid registration schema');
  if (raw.allowedRoots.some(p => typeof p !== 'string' || !path.isAbsolute(p))) throw new Error('Absolute allowlisted root required');
  const ids = new Set();
  // Identity ambiguity is global; filesystem availability belongs to one entry.
  for (const sim of raw.simulators) {
    if (!sim || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(sim.id) || ids.has(sim.id)) throw new Error('Invalid or duplicate simulator ID');
    ids.add(sim.id);
  }
  const roots = await Promise.allSettled(raw.allowedRoots.map(p => realpath(p)));
  const allowed = roots.filter(r => r.status === 'fulfilled').map(r => r.value);
  return Promise.all(raw.simulators.map(async sim => {
    try {
      if (typeof sim.title !== 'string' || !sim.title || !path.isAbsolute(sim.assetRoot) || !allowed.includes(await realpath(sim.assetRoot))) throw new Error('Unregistered asset root');
      if (!sim.assets || !Object.keys(sim.assets).length) throw new Error('Asset hashes required');
      for (const [name, hash] of Object.entries(sim.assets)) { relativeAsset(name); if (!hashPattern.test(hash)) throw new Error('Invalid artifact hash'); }
      if (!sim.assets[relativeAsset(sim.entrypoint)]) throw new Error('Entrypoint must be in asset manifest');
      if (!sim.source || !/^[a-f0-9]{40}$/.test(sim.source.revision) || !hashPattern.test(sim.source.sha256) || !path.isAbsolute(sim.source.root)) throw new Error('Source provenance required');
      const source = await confined(sim.source.root, sim.source.entrypoint);
      if (digest(await readFile(source)) !== sim.source.sha256) throw new Error('Registered source changed');
      return { ...sim, available: true };
    } catch (e) {
      const reason = e.code === 'ENOENT' ? 'Registered source or asset root is missing' : e.message;
      return { id: sim.id, title: typeof sim.title === 'string' ? sim.title : sim.id, available: false, reason };
    }
  }));
}

export async function readAsset(sim, name) {
  if (sim.available === false) throw new Error('Simulator unavailable: ' + sim.reason);
  relativeAsset(name);
  if (!Object.hasOwn(sim.assets, name)) throw new Error('Asset not registered');
  const mime = types[path.extname(name).toLowerCase()]; if (!mime) throw new Error('Unsupported asset type');
  const file = await confined(sim.assetRoot, name);
  if ((await stat(file)).size > 128 * 1024 * 1024) throw new Error('Asset too large');
  const bytes = await readFile(file); if (digest(bytes) !== sim.assets[name]) throw new Error('Registered artifact changed');
  return { bytes, mime, hash: sim.assets[name] };
}
export function publicSimulator(sim) { if (sim.available === false) return { id: sim.id, title: sim.title, available: false, reason: sim.reason }; return { available: true, id: sim.id, title: sim.title, description: sim.description || '', entrypoint: sim.entrypoint, source: { revision: sim.source.revision, entrypoint: sim.source.entrypoint, sha256: sim.source.sha256 }, artifact: sim.assets[sim.entrypoint] }; }
