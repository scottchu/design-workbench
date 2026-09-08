import { error } from '@sveltejs/kit';
import { loadRegistry, publicSimulator } from '$lib/server/registry.js';
export async function load({ params }) { const sim = (await loadRegistry()).find(s => s.id === params.id); if (!sim) error(404, 'Simulator not registered'); if (!sim.available) error(409, 'Simulator unavailable: ' + sim.reason); return { sim: publicSimulator(sim) }; }
