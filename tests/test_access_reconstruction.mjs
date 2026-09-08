// Independent acceptance harness. The reconstruction builder does not read this.
import test from 'node:test';
import assert from 'node:assert/strict';
import * as original from '../apps/playground/src/lib/server/access.js';
import * as candidate from '../fixtures/reconstruction/access/access.mjs';

const privateAddress = 'https://example.test-tailnet.ts.net:8454';
const privateHost = 'example.test-tailnet.ts.net:8454';
const policyError = 'WORKBENCH_ALLOWED_ORIGIN must be one exact HTTPS ts.net origin';

function headers(host, origin, extras = {}) {
  const value = new Headers(extras);
  if (host !== null) value.set('host', host);
  if (origin !== null) value.set('origin', origin);
  return value;
}

// These examples express the declared contract without using the existing
// implementation as the expected-value oracle.
const configurations = [
  ['empty disables private access', '', null],
  ['private port', privateAddress, privateAddress],
  ['default HTTPS port is implicit', 'https://example.ts.net', 'https://example.ts.net'],
  ['literal suffix does not validate DNS membership', 'https://.ts.net', 'https://.ts.net'],
  ['HTTP', 'http://example.ts.net', 'policy'],
  ['public domain', 'https://example.com', 'policy'],
  ['suffix apex', 'https://ts.net', 'policy'],
  ['suffix impostor', 'https://example.ts.net.evil.test', 'policy'],
  ['trailing hostname dot', 'https://example.ts.net.', 'policy'],
  ['uppercase hostname', 'https://EXAMPLE.ts.net', 'policy'],
  ['uppercase scheme', 'HTTPS://example.ts.net', 'policy'],
  ['explicit default port', 'https://example.ts.net:443', 'policy'],
  ['trailing slash', 'https://example.ts.net/', 'policy'],
  ['path', 'https://example.ts.net/x', 'policy'],
  ['credentials', 'https://user:pass@example.ts.net', 'policy'],
  ['query', 'https://example.ts.net?q=1', 'policy'],
  ['fragment', 'https://example.ts.net#x', 'policy'],
  ['empty query delimiter', 'https://example.ts.net?', 'policy'],
  ['empty fragment delimiter', 'https://example.ts.net#', 'policy'],
  ['leading space', ' https://example.ts.net', 'policy'],
  ['relative URL parse failure', '/relative', 'parse'],
  ['invalid port parse failure', 'https://example.ts.net:65536', 'parse'],
];

const requests = [
  ['IPv4 without Origin', '127.0.0.1:4179', null, '', true],
  ['localhost exact Origin', 'localhost:4179', 'http://localhost:4179', '', true],
  ['IPv6 exact Origin', '[::1]:4179', 'http://[::1]:4179', '', true],
  ['empty Origin', 'localhost:4179', '', '', true],
  ['literal null Origin', 'localhost:4179', 'null', '', false],
  ['alias is a different origin', 'localhost:4179', 'http://127.0.0.1:4179', '', false],
  ['wrong local scheme', 'localhost:4179', 'https://localhost:4179', '', false],
  ['origin trailing slash', 'localhost:4179', 'http://localhost:4179/', '', false],
  ['missing Host', null, null, '', false],
  ['empty Host', '', null, '', false],
  ['wrong local port', 'localhost:4180', null, '', false],
  ['missing local port', 'localhost', null, '', false],
  ['Host case remains exact', 'LOCALHOST:4179', null, '', false],
  ['private disabled', privateHost, null, '', false],
  ['private without Origin', privateHost, null, privateAddress, true],
  ['private matching Origin', privateHost, privateAddress, privateAddress, true],
  ['private empty Origin', privateHost, '', privateAddress, true],
  ['private wrong Origin', privateHost, 'https://evil.test', privateAddress, false],
  ['private wrong port', 'example.test-tailnet.ts.net:443', null, privateAddress, false],
  ['private host case remains exact', 'EXAMPLE.test-tailnet.ts.net:8454', null, privateAddress, false],
  ['private config preserves local route', '127.0.0.1:4179', null, privateAddress, true],
  ['private Origin on local Host', '127.0.0.1:4179', privateAddress, privateAddress, false],
  ['local Origin on private Host', privateHost, 'http://localhost:4179', privateAddress, false],
  ['default private port Host', 'example.ts.net', 'https://example.ts.net', 'https://example.ts.net', true],
  ['explicit default port Host mismatches', 'example.ts.net:443', null, 'https://example.ts.net', false],
  ['multiple origins', 'localhost:4179', 'http://localhost:4179 https://evil.test', '', false],
];

for (const [implementationName, api] of [['original', original], ['candidate', candidate]]) {
  test(`${implementationName}: C1 omitted setting`, () => {
    assert.equal(api.privateOrigin(), null);
    assert.equal(api.allowedRequest(headers('localhost:4179', null)), true);
  });
  for (const [name, setting, expected] of configurations) {
    test(`${implementationName}: C1-C3 ${name}`, () => {
      if (expected === 'parse') {
        assert.throws(() => api.privateOrigin(setting), { name: 'TypeError' });
      } else if (expected === 'policy') {
        assert.throws(() => api.privateOrigin(setting), { name: 'Error', message: policyError });
      } else {
        const result = api.privateOrigin(setting);
        if (expected === null) assert.equal(result, null);
        else {
          assert.ok(result instanceof URL);
          assert.equal(result.origin, expected);
        }
      }
    });
  }
  for (const [name, host, origin, setting, expected] of requests) {
    test(`${implementationName}: R2-R3 ${name}`, () => {
      assert.equal(api.allowedRequest(headers(host, origin), setting), expected);
    });
  }
  test(`${implementationName}: R1 invalid configuration precedes local admission`, () => {
    assert.throws(() => api.allowedRequest(headers('localhost:4179', null), 'https://evil.test'),
      { name: 'Error', message: policyError });
    assert.throws(() => api.allowedRequest(headers('localhost:4179', null), '/relative'),
      { name: 'TypeError' });
  });
  test(`${implementationName}: R2 forwarding headers cannot substitute Host`, () => {
    assert.equal(api.allowedRequest(headers('evil.test', null, {
      'x-forwarded-host': privateHost, forwarded: `host=${privateHost};proto=https`
    }), privateAddress), false);
    assert.equal(api.allowedRequest(headers('localhost:4179', null, {
      'x-forwarded-host': 'evil.test'
    })), true);
  });
  test(`${implementationName}: R1 standard Headers semantics`, () => {
    const h = new Headers({ HOST: ' localhost:4179 ', ORIGIN: ' http://localhost:4179 ' });
    assert.equal(api.allowedRequest(h), true);
    h.append('host', 'evil.test');
    assert.equal(api.allowedRequest(h), false);
  });
}

function outcome(operation) {
  try { return { returned: operation() }; }
  catch (error) { return { thrown: { name: error.name, message: error.message } }; }
}

test('sampled compatibility: 22 configurations × 18 hosts × 13 origins = 5148 requests', () => {
  const hosts = [null, '', 'localhost:4179', '127.0.0.1:4179', '[::1]:4179',
    'localhost', 'localhost:443', 'LOCALHOST:4179', privateHost,
    'example.test-tailnet.ts.net', 'example.test-tailnet.ts.net:443',
    'example.ts.net', 'example.ts.net:443', '.ts.net', 'evil.test',
    'http://localhost:4179', 'localhost:4179, evil.test', 'localhost:04179'];
  const origins = [null, '', 'null', 'http://localhost:4179', 'http://127.0.0.1:4179',
    'http://[::1]:4179', privateAddress, 'https://example.ts.net', 'https://.ts.net',
    'https://evil.test', 'http://localhost:4179/', 'HTTP://localhost:4179',
    'http://localhost:4179, https://evil.test'];
  let count = 0;
  for (const [, setting] of configurations) for (const host of hosts) for (const origin of origins) {
    assert.deepEqual(
      outcome(() => candidate.allowedRequest(headers(host, origin), setting)),
      outcome(() => original.allowedRequest(headers(host, origin), setting)),
      JSON.stringify({ setting, host, origin })
    );
    count += 1;
  }
  assert.equal(count, 5148);
});

test('generated module exposes only the declared API', () => {
  assert.deepEqual(Object.keys(candidate).sort(), ['allowedRequest', 'privateOrigin']);
});
