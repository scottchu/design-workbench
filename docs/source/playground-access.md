# Playground request admission

Role: normative source for a bounded reconstruction experiment.
Status: current behavior captured for compatibility; not a new access-policy
design or a claim of complete Playground specification.
Source version: 1.

## Why

Permit the Playground's declared local addresses and one optionally configured
private address, while rejecting unrecognized request hosts and mismatched browser
origins. This policy does not authenticate users, configure networking or establish
that a private address is reachable.

## How

The configuration and request are explicit inputs. Validate configuration before
examining request headers, derive the expected origin from the Host header, then
decide whether the supplied Origin is compatible. Forwarding headers do not
participate. Preserve the following rule identities through interpretation and
generation; report missing or contradictory rules rather than inventing behavior.

### C1 — Configuration input and empty setting

The public function `privateOrigin(value = '')` accepts a string. An omitted or
empty string returns `null`, representing no private origin. Values outside the
string input domain are not part of this contract.

### C2 — URL parsing

Parse a nonempty setting with the runtime's WHATWG `URL` constructor, without a
base URL. A parse failure throws the constructor's native error. Do not catch or
convert it into a normal rejection value.

### C3 — Allowed private origin

A parsed URL is accepted only when every condition holds:

- Protocol is exactly `https:`.
- Parsed hostname ends with the literal suffix `.ts.net`.
- Parsed username and password are both empty.
- Parsed pathname is exactly `/`; parsed search and hash are both empty.
- The original input string equals the parsed URL's serialized `origin` exactly.

The last comparison rejects noncanonical spelling, an explicit default HTTPS
port, a trailing slash and other spellings that parsing would normalize. It also
rejects a bare trailing `?` or `#` even when the parsed search/hash is empty.
Apply the URL constructor's port semantics; do not add a separate DNS, Tailscale
membership or port policy. The suffix predicate is literal, not a network check.

If parsing succeeds but any condition fails, throw an `Error` whose message is
`WORKBENCH_ALLOWED_ORIGIN must be one exact HTTPS ts.net origin`.
On success return the parsed `URL` object, not a string or a Boolean.

### R1 — Request API and evaluation order

The public function `allowedRequest(headers, configuredOrigin = '')` accepts a
standard `Headers` object and a string configuration. First evaluate
`privateOrigin(configuredOrigin)`. Propagate any error, even for an otherwise
valid local request. Header names and values use the standard `Headers.get`
semantics; there is no additional application-level trimming or normalization.

### R2 — Host to expected origin

Read `headers.get('host')`. Compare its value exactly against these local hosts:

| Host | Expected origin |
| --- | --- |
| `127.0.0.1:4179` | `http://127.0.0.1:4179` |
| `localhost:4179` | `http://localhost:4179` |
| `[::1]:4179` | `http://[::1]:4179` |

For any other host, use the configured private URL's serialized `origin` only if
that URL exists and the header equals its parsed `host` exactly, including any
nondefault port. Otherwise return `false`. Local host selection takes precedence.
Do not infer default ports, lowercase a header, parse it as another URL, consult
`Forwarded`/`X-Forwarded-Host`, or consult any other header.

### R3 — Origin decision

After selecting an expected origin, read `headers.get('origin')`. Return `true`
if it is absent (`null`), the empty string, or exactly equal to the expected
origin. Otherwise return `false`. The literal string `null`, multiple origins,
alternative local aliases, different schemes and trailing slashes are not equal.
An empty Origin is intentionally treated like absence for current compatibility.

### E1 — Execution boundary

Both functions are synchronous and perform no I/O, environment lookup, network
request, logging, persistent mutation or service lifecycle operation. They return
only the values above or throw the specified errors. Valid `Headers` and string
inputs are the declared domain. This module alone does not emit HTTP responses,
set response headers, implement authorization or serve pages.

## What to generate

Target parameters: JavaScript ECMAScript module, Node.js 26.7.0, standard `URL`
and `Headers`, no packages. Export exactly the two named public functions above
from `access.mjs`. Internal names and algorithm spelling may differ.

Before generating code, write `model.json` containing three explicitly derived
views, each traceable to these rule IDs:

1. `ast`: structured declarations for purpose, inputs, outputs, predicates,
   ordered operations and errors. This is an agent-authored interpretation of
   this document, not the output of an implemented Markdown parser.
2. `ontology`: types and meanings, including configuration, parsed private origin,
   request headers, selected expected origin, admission decision and errors. Keep
   declared configuration distinct from observed network reachability.
3. `composition`: typed objects and arrows for parsing/validation, host selection
   and origin comparison, with branch/error propagation and explicit composition
   order. State identity and associativity obligations for composable arrows and
   any claimed equivalence to the public API. This is a finite composition model;
   do not claim a proved categorical semantics or generic category compiler.

Include `unresolved` for source gaps and `assumptions` for any additional choices.
Do not silently resolve a gap that changes observable behavior. Implementation
choices with no declared observable effect may be recorded as such.

Acceptance target: behavior equivalence on this declared domain, including return
types and error propagation. Tests are evidence over sampled inputs, not a proof
for every possible string. Byte-identical code generation, full Playground
reconstruction and runtime deployment are outside this experiment.
