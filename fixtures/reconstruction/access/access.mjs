// Agent-authored implementation of docs/source/playground-access.md, version 1.
// C1-C3: configuration is validated independently of request admission.
export function privateOrigin(value = '') {
  if (value === '') return null;
  const url = new URL(value);
  if (
    url.protocol !== 'https:' ||
    !url.hostname.endsWith('.ts.net') ||
    url.username !== '' ||
    url.password !== '' ||
    url.pathname !== '/' ||
    url.search !== '' ||
    url.hash !== '' ||
    value !== url.origin
  ) {
    throw new Error('WORKBENCH_ALLOWED_ORIGIN must be one exact HTTPS ts.net origin');
  }
  return url;
}

// R1-R3: configuration first, exact Host selection, then Origin compatibility.
export function allowedRequest(headers, configuredOrigin = '') {
  const configured = privateOrigin(configuredOrigin);
  const host = headers.get('host');
  let expected;
  if (host === '127.0.0.1:4179') {
    expected = 'http://127.0.0.1:4179';
  } else if (host === 'localhost:4179') {
    expected = 'http://localhost:4179';
  } else if (host === '[::1]:4179') {
    expected = 'http://[::1]:4179';
  } else if (configured !== null && host === configured.host) {
    expected = configured.origin;
  } else {
    return false;
  }
  const origin = headers.get('origin');
  return origin === null || origin === '' || origin === expected;
}
