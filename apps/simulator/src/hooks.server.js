export async function handle({ event, resolve }) {
  if (!['127.0.0.1','localhost','[::1]'].includes(event.url.hostname)) return new Response('Loopback only', { status:403 });
  const origin = event.request.headers.get('origin');
  if (origin && origin !== event.url.origin) return new Response('Cross-origin request refused', { status:403 });
  const response = await resolve(event);
  response.headers.set('Cross-Origin-Opener-Policy','same-origin');
  response.headers.set('Cross-Origin-Embedder-Policy','require-corp');
  response.headers.set('Cross-Origin-Resource-Policy','same-origin');
  return response;
}
