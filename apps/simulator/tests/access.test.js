import test from 'node:test';
import assert from 'node:assert/strict';
import { allowedRequest, privateOrigin } from '../src/lib/server/access.js';

const remote = 'https://example.test-tailnet.ts.net:8454';
function headers(host, origin) {
  const h = new Headers({ host });
  if (origin) h.set('origin', origin);
  return h;
}
test('local access needs no Tailscale configuration', () => {
  assert.ok(allowedRequest(headers('127.0.0.1:4179')));
  assert.ok(allowedRequest(headers('localhost:4179', 'http://localhost:4179')));
  assert.ok(!allowedRequest(headers('example.test-tailnet.ts.net:8454')));
  assert.ok(!allowedRequest(headers('evil.test:4179')));
});
test('only the configured private host and exact browser origin are accepted', () => {
  assert.ok(allowedRequest(headers('example.test-tailnet.ts.net:8454', remote), remote));
  assert.ok(allowedRequest(headers('127.0.0.1:4179'), remote));
  assert.ok(!allowedRequest(headers('example.test-tailnet.ts.net:443'), remote));
  assert.ok(!allowedRequest(headers('example.test-tailnet.ts.net:8454', 'https://evil.test'), remote));
  assert.ok(!allowedRequest(headers('127.0.0.1:4179', remote), remote));
  const h = headers('evil.test'); h.set('x-forwarded-host', 'example.test-tailnet.ts.net:8454');
  assert.ok(!allowedRequest(h, remote));
});
test('configuration rejects public origins and ambiguous URL components', () => {
  for (const value of ['https://example.com', 'http://example.ts.net',
    'https://example.ts.net/path', 'https://user@example.ts.net',
    'https://example.ts.net?query=1', 'https://example.ts.net/#hash', 'https://example.ts.net/']) {
    assert.throws(() => privateOrigin(value));
  }
});
