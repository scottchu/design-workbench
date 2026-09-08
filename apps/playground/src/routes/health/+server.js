import { env } from '$env/dynamic/private';
import { json } from '@sveltejs/kit';

export function GET() {
  return json({ service: 'cad-workbench-simulator', instance: env.WORKBENCH_INSTANCE_ID || null },
    { headers: { 'Cache-Control': 'no-store' } });
}
