import { env } from '$env/dynamic/private';
import { allowedRequest } from '$lib/server/access.js';

export async function handle({ event, resolve }) {
  if (!allowedRequest(event.request.headers, env.WORKBENCH_ALLOWED_ORIGIN)) {
    return new Response('Unconfigured host or cross-origin request', { status:403 });
  }
  const response = await resolve(event);
  response.headers.set('Cross-Origin-Opener-Policy','same-origin');
  response.headers.set('Cross-Origin-Embedder-Policy','require-corp');
  response.headers.set('Cross-Origin-Resource-Policy','same-origin');
  return response;
}
