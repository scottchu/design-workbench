# Docs-only reconstruction result

Role: derived evidence. Scope: the [bounded pilot](BRIEF.md), building on PR6's
product/source definition. The user's stronger target is captured in
[product intent](../../product.md#source-sufficiency-target).

## What was reconstructed

Playground request admission: two synchronous functions that validate an optional
private origin and decide whether request Host/Origin headers match the configured
policy. The original module remains in production. No service or installation
was operated.

The primary agent inspected the existing implementation and tests, then wrote
[source version 1](../../source/playground-access.md). It was frozen before fresh
builder `/root/reconstruct_access` received it. The builder reported reading only
that product source, then its own generated files during checks. It received no
existing implementation, tests or parent conversation. Read restrictions were
procedural on a shared filesystem, not enforced by an isolated filesystem.

The builder wrote [model.json](../../../fixtures/reconstruction/access/model.json)
first, followed by [access.mjs](../../../fixtures/reconstruction/access/access.mjs).
The primary agent copied both byte-for-byte into designated experimental fixtures.
There was one frozen source version and one candidate generation, with no
post-test candidate repair. Exact identities are in [RECEIPT.json](RECEIPT.json).

## What the intermediate views contributed

- AST: made public inputs, defaults, predicates, operation order and errors
  separately inspectable and traceable to seven source rule IDs.
- Ontology: distinguished declared configuration from network reachability,
  expected origin from supplied Origin, and rejection from a configuration error.
- Typed composition: exposed configuration-before-header-read ordering, early
  Host rejection and error propagation. It records identity/associativity as
  obligations, with no formal proof or generic category compiler.

These views were authored by the same builder that generated the code. This run
does not measure whether they improve generation over direct prose-to-code, and
does not demonstrate that a generator consumes the JSON mechanically. Their
demonstrated role here is an inspectable interpretation, not an executable IR.

## Source gaps exposed by capture

The old general docs were not a complete reconstruction input. This specification
adds exact exports and return types, empty/default behavior, native parse versus
policy errors, evaluation order, all three local aliases, Headers normalization
boundaries, and treatment of empty versus literal `null` Origin. The literal
`.ts.net` suffix check is captured as existing behavior, not proof of DNS validity
or Tailscale membership. These details were obtained from implementation evidence
before the source freeze; no assertion is made that the old docs alone sufficed.

No behavior-changing source gap was reported by the builder within the declared
string configuration and standard Headers domain. Other argument types and the
rest of the HTTP hook/server are outside the reconstructed contract.

## Validation

- `node --test tests/test_access_reconstruction.mjs`: 106 passed, zero failed.
  Independent expected-value cases run against both original and candidate.
  A separate differential matrix compares 22 configurations × 18 hosts × 13
  origins: 5,148 request outcomes, including error names/messages.
  Of these, 936 use valid/empty configuration; 4,212 repeat configuration-error
  outcomes across headers. The total is a sample count, not distinct path coverage.
- Builder reported Node v26.7.0 syntax and candidate-only smoke checks passed.
- Inline `uv run python` verification confirmed source freeze SHA256 unchanged,
  three model views present, all seven rule IDs represented and no unresolved
  model entries. This structural check is not semantic proof.
- `uv run python scripts/check_registry.py`: 12 capabilities, two mapped recipes,
  references and policy hashes passed; no recipe executed.
- [Independent review](REVIEW.md): no blocking findings; the reviewer reran all
  106 tests and inspected source/model/code branches. Acceptance is limited to
  the exploratory fixture and declared domain, with the limitations below.
- `git diff --check` and inline local-link/receipt readback passed. Five recorded
  source, generated-output and acceptance-input hashes match their actual files.

## What this establishes and what remains

This is evidence that one carefully completed document specification supported
one independent reconstruction with sampled compatibility. It does not establish
whole-product reconstruction, exhaustive behavioral equivalence, byte-identical
regeneration or a functioning docs → AST → ontology/category compiler. No
versioned compiler was implemented and model/harness identity was not captured
sufficiently for exact generation replay.

The product still needs specifications for remaining software/skill behavior,
package composition, dependencies, external inputs and acceptance boundaries.
Do not discard existing code, tests or project records based on this pilot.

Next bounded action: review and integrate this pilot after its PR6 base, then
choose whether to test a second capability or implement an executable interpreter
for the small source/model vocabulary. Either is new scoped work; this experiment
does not start a general compiler or change the running Playground.
