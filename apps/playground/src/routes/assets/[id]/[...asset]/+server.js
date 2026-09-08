import { error } from '@sveltejs/kit';
import { loadRegistry, readAsset } from '$lib/server/registry.js';
export async function GET({ params }) {
  try { const sim = (await loadRegistry()).find(s => s.id === params.id); if (!sim) error(404, 'Simulator not registered');
    const asset = await readAsset(sim, params.asset);
    return new Response(asset.bytes, { headers: { 'Content-Type': asset.mime, 'ETag': '"' + asset.hash + '"', 'Cache-Control': 'no-store', 'X-Content-Type-Options':'nosniff', 'Content-Security-Policy': "default-src 'self' blob:; script-src 'self' 'unsafe-inline' 'wasm-unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' blob: data:; worker-src 'self' blob:; connect-src 'self' blob:; frame-ancestors 'self'" } });
  } catch { error(404, 'Registered asset unavailable or changed'); }
}
