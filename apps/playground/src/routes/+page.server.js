import { loadRegistry, publicSimulator } from '$lib/server/registry.js';
export async function load() { try { return { simulators: (await loadRegistry()).map(publicSimulator), problem: null }; } catch (e) { return { simulators: [], problem: e.message }; } }
