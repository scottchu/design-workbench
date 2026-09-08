# Experimental reconstruction outputs

These are designated generic developer fixtures. They are derived from the
frozen [request-admission source](../../../docs/source/playground-access.md),
not maintained production modules or additional policy authorities.

- `model.json`: builder-authored AST, ontology and finite typed composition views.
- `access.mjs`: subsequently generated candidate; the running Playground does
  not import it and the plugin packager does not include it.

The builder received only the specification and procedural/output instructions,
not existing code or acceptance tests. Read the
[experiment evidence](../../../docs/iterations/2026-09-08-docs-reconstruction/HANDOFF.md)
and its receipt for identities and limits. Do not patch these outputs to change
policy: revise the owning source and conduct a new identified generation.

Run the independent comparison from the repository root:

```sh
node --test tests/test_access_reconstruction.mjs
```

This rechecks the recorded candidate. It does not regenerate it; a repeat
generation currently requires another agent interpretation of the declared
source. There is no deterministic compiler command in this experiment.
