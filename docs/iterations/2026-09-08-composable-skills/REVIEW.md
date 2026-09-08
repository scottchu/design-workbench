# Independent acceptance review: focused simulator skills

Date: 2026-09-08. Reviewer namespace: `review_skills`. Implementation and review
were separate. Reviewed applicable AGENTS.md, README, decision 0003, iteration
brief, both new skills, runtime reference, workbench-flow routing, service contract,
registration contract, `scripts/simulator_service.py`, registration CLI and
`registry.js`. Only this review record and ignored generic fixtures were written.

## Findings and disposition

1. Initial page update instructions accepted `loadRegistry(...).available` as
   sufficient candidate verification. That loader checks source hash and asset-root
   metadata but does not read asset bytes. Reported to implementer; revised skill
   now requires every updated asset to pass `readAsset`, and explains this distinction
   for inspection. Forward test confirms changed HTML remains loader-available but
   fails `readAsset` with `Registered artifact changed`. Revised check catches it.
2. Runtime reference initially used `uv run python` even for status, whereas the
   server skill requires the selected root's existing absolute interpreter. Reported
   potential implicit environment synchronization and the existing status CLI's
   local lifecycle-lock writes. Status must not prepare dependencies or start/install
   a service; diagnostic lock bookkeeping is not service mutation. Final disposition
   is recorded below after implementation reread.

## Actual fixture execution

All paths below are relative to
`/Users/scottchu/Projects/personal/CAD-workbench-next` unless absolute.

Commands executed:

```sh
git check-ignore .workbench/review-composable/probe
node .workbench/review-composable/review.mjs > .workbench/review-composable/output.txt
```

Both exited 0. The first returned the ignored path. The second ran a review-only
Node harness preserved at the displayed path, using the existing registry exports
and actual registration subprocesses. Node resolved to
`/Users/scottchu/.asdf/installs/nodejs/26.7.0/bin/node`.

Harness setup created two separate generic Git repositories (`alpha`, `beta`), each
with committed `source.txt` and `build/index.html`, using `git init -q`,
`git add source.txt build/index.html`, and per-command local review identity:
`git -c 'user.name=Generic Review' -c user.email=review@example.invalid commit -qm 'Generic fixture v1'`.
No global Git configuration changed. Alpha's later v2 used the same add/commit
commands with commit message `Generic fixture v2`.

Each actual registration used the following argument form, with `ID` equal to
`alpha` or `beta`, and `BASE` equal to the absolute ignored
`.workbench/review-composable` directory:

```sh
node apps/simulator/scripts/register.mjs \
  --id ID --title ID --asset-root BASE/ID/build \
  --source-root BASE/ID --source-entry source.txt \
  --config BASE/registry.json
```

Alpha update invoked that CLI with the same arguments except
`--config BASE/update.candidate.json`. Exact expanded command arrays and CLI
outputs are in `output.txt`. The fixture made no lifecycle calls.

Results:

- Register alpha and beta: both source validation and actual HTML `readAsset`
  readbacks passed.
- Mutate alpha source: `loadRegistry` reported alpha unavailable with
  `Registered source changed`; reading alpha was rejected, beta remained readable.
- Commit alpha v2 source and HTML: capture original registry bytes in
  `update.recovery.json`, remove only alpha from a separate candidate, register
  its reviewed v2 build into that candidate, validate entries and every asset,
  compare beta's raw entry and allowed roots against original, compare registry
  bytes against capture, rename candidate atomically over fixture registry, read
  back and validate. All assertions passed.
- Change alpha HTML after registration: loader still returned available, while
  `readAsset` and the full candidate verifier rejected the changed artifact.
  Restore the registered bytes and verify successfully.
- Remove alpha: capture `remove.recovery.json`, create `remove.candidate.json`
  removing only alpha, validate beta and all its assets, preserve beta's exact
  entry and complete allowed-root array, compare original bytes, rename and
  read back. Alpha absent; beta remained available and readable. All passed.

Each operation used the single-writer isolated registry. The recovery files remain
ignored; successful candidate paths were consumed by rename. No concurrent-writer
behavior is claimed.

## Fixture identity

| Candidate | Git revision | Source SHA-256 |
| --- | --- | --- |
| Alpha v1 | `38072e4abf047538df149c7e46b1c62cf34b3e62` | `dcf3ff9bc5d4176c5a99db65da73fa62908e722851550b2f16f58131b08d45c8` |
| Alpha v2 | `4e24c8e1b52c46ca84617ef379643915ae96470a` | `4c3434850fd7d528751330282c9a06a7ceca40a9c99ecd17f9b9e12955e54700` |
| Beta v1 | `ec0468f8680913b90fa5f6dc53bb9256c534d4f9` | `c80c3c59bf75d3d980242f5a933b0a1c2fd25537d7b119d0fb907277a1f59dd6` |

Final fixture registry SHA-256:
`c769c5d15ada162ec0ef72fa59c6c445c838b3ff66e72e3f5df44f2ccf321707`.
Beta's surviving `index.html` SHA-256:
`b8832f2b3a4091d4a55e804f6fab481703c4fced96cac9e3bd90eb942ece1bde`.

## Static lifecycle and routing review

The server skill explicitly separates status/diagnosis from ensure/open, stop,
login installation and relocation. Binding identity conflicts are configuration
failures and do not authorize adoption, overwrite or a second service. The
controller verifies loaded ownership and health; its status route does not call
ensure/install/build. The runtime binding is a skill input, not automatically
parsed by the controller. Workbench-flow links the focused skills and preserves
pure observation/preparation routes without simulator startup. No lifecycle
controller, live binding, private registry, browser, service, external project,
plugin installation or network operation was used for this review.

This is source-level independent skill review plus executed generic page registry
acceptance. It does not establish installed-skill discovery, live server reuse,
HTTP/browser behavior, Laifen geometry, export parity, phone behavior or physical
acceptance. Packaging validation is owned and recorded by the implementing agent.

## Final reread

Both findings are resolved in the reviewed source. The revised server skill and
runtime reference explicitly require the existing absolute root interpreter,
report its absence without syncing for status-only requests, limit preparation to
in-scope setup/ensure/open, and disclose status lock bookkeeping. Binding mismatch
still fails without adopting another runtime. No remaining blocking finding in
this bounded review. `git diff --check` exited 0 after the review edits.

Ignored evidence SHA-256, measured with
`shasum -a 256 .workbench/review-composable/review.mjs .workbench/review-composable/output.txt`:

- `review.mjs`: `e5b1b51dcca31e3b7c213feb2f51793ce6043c04ec06c2f20e25c64eb555d649`.
- `output.txt`: `ae4d5be343d2629ab693a68656937c8b41ba46a67bbd667b59ae7508493f05fb`.
