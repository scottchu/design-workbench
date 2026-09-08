const localHosts = new Set(['127.0.0.1:4179', 'localhost:4179', '[::1]:4179']);

export function privateOrigin(value = '') {
  if (!value) return null;
  const url = new URL(value);
  if (url.protocol !== 'https:' || !url.hostname.endsWith('.ts.net') ||
      url.username || url.password || url.pathname !== '/' || url.search || url.hash ||
      value !== url.origin) {
    throw new Error('WORKBENCH_ALLOWED_ORIGIN must be one exact HTTPS ts.net origin');
  }
  return url;
}

export function allowedRequest(headers, configuredOrigin = '') {
  const remote = privateOrigin(configuredOrigin);
  const host = headers.get('host');
  const expected = localHosts.has(host) ? `http://${host}` :
    remote && host === remote.host ? remote.origin : null;
  if (!expected) return false;
  const origin = headers.get('origin');
  return !origin || origin === expected;
}
