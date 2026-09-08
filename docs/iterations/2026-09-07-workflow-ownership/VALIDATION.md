# Independent joined validation (V2)

Status: **PASS for the scoped separation change, with the explicitly pre-existing Laifen continuity test failure retained. V2-1 is resolved and independently rechecked.** V2 is read-only against the authoritative repositories and owns this record plus ignored `.workbench/workflow-ownership/v2/` scratch.

## Scope and frozen identity

- Provider: Workbench commit `36f41715ee2257c0f2e41e40329216e3d2b2747f`, committed `catalog/POLICY.sha256` hash `6f1ab6580b67cd9e58dd2302f07cdc65a3a2bfa2213e650139a7ce4542bf9536`. All 30 listed policy files were read from that exact commit, hashed independently, and compared to current provider files.
- Design consumer: `/Users/scottchu/Projects/personal/design-projects-workflow-separation`; original authority `71d661c14098860b7a374e13043fb084994be8a0`. Initially checked candidate manifest hash `f3aa463e4008a52fac92a178b2d37c1aac029246a5ad2a0a760809b507bb1372`.
- Sticker consumer: `/Users/scottchu/Projects/personal/sticker-projects`; accepted imported authority `dafdb8eb9b0cbc9449dce84a225f2a59f3e3f88b` plus scoped root/binding/history/recovery configuration.
- Root's newer plugin packaging paths are outside this scoped provider/consumer gate. This validation does not imply plugin installation or validate that later package.

## Results

| Check | Result |
| --- | --- |
| Final sticker project | PASS: 848 actual files, 387,625,617 bytes equal the immutable project manifest and original source Git bytes |
| Other design projects and context | PASS: all 2,504 files, 657,791,302 bytes match manifest and baseline Git bytes |
| Independent retained-path census | PASS: 1,239 Laifen + 814 Kage + 443 XT60 + 7 historical root iteration records + 1 workshop file exactly equal preserved-manifest paths |
| Retired migration paths | PASS: all 884 recorded baseline hashes match original Git; all retired paths absent from consumer disk |
| History | PASS: all 11 original-to-filtered mappings have identical selected project/skill path, mode and blob tuples, including divergent `86ce8309...` |
| Destination-contained recovery base | PASS: `recovery/live-pilot-base-fef4f264` resolves to `7f4da69ed1af9339a0d1e6d9395acf710d48cc90`; its selected trees equal original `fef4f264...` |
| Recovery readback reuse | PASS: every one of V1's eight frozen inputs remains byte-identical; actual V1 isolated restore of 1,023 project + five skill files therefore remains applicable to the independently equal filtered base |
| Provider binding bytes | PASS: both consumers name the exact committed provider revision and policy-manifest SHA-256 |
| Sticker bound commands | PASS: direct Bun argv, declared cwd/runtime, actual source hashes and imported commit bytes verified; `contract`, `candidate`, `review-lint` and flags match source CLI dispatch at lines 436–441 |
| Production selection | PASS: invocation remains `not-selected`; missing input tokens explicitly block execution |
| Copied workflow retirement | PASS: design consumer's `.agents/skills`, `docs/templates`, viewer service removed; four policy filenames are small external references; sticker's sole compatibility SKILL.md is a seven-line pointer |
| Registry and maintained local links | PASS: checker finds 12 capabilities, two mapped recipes, no missing/escaping local references or policy-hash mismatch |
| Receipt schema | JSON parses and structural contract statically reviewed; no installed JSON Schema validator in approved root environment, so runtime standards-conformance validation is not claimed |

The mapped recovery tree proof plus unchanged V1 inputs removes dependency on the original checkout for project/skill restoration. Original WIP and recovery archives remain untouched. V1's explicit full-POSIX-permission limitation remains: Git modes/bytes are preserved, but full tracked filesystem metadata is not claimed.

## Focused execution

Executed independently:

```sh
# Workbench root
uv run python -m unittest discover -s tests -v
uv run python scripts/check_registry.py
uv run python .workbench/workflow-ownership/v2/validate.py > .workbench/workflow-ownership/v2/check.log

# Design consumer root
uv run pytest tests/test_repository_structure.py

# Sticker consumer root
npm test
```

- Workbench: **9/9 PASS**. Registry validates identity/reference integrity and existing tests exercise policy tampering, unknown capability and path escape failures.
- Sticker: **14/14 PASS**, 35.152 seconds, including real audit calls and synthetic 32-slot stress fixtures in temporary output. No production art generation or project build ran.
- Design consumer initially: **9 PASS, 1 FAIL**; after the added ID regression test: **10 PASS, 1 FAIL**. The failure is the still-enforced `test_workspace_members_externalize_project_continuity`: Laifen CURRENT points to `2026-09-06-pattern-reference-intake`, whose `VALIDATION.md` is absent. Independent `git cat-file -e 71d661c14098860b7a374e13043fb084994be8a0:projects/laifen-wave-case/docs/iterations/2026-09-06-pattern-reference-intake/VALIDATION.md` also fails, and CURRENT bytes equal baseline. This defect predates separation; no skip, weakened assertion or invented evidence was added.
- `git diff --check` for all three repositories and staged design/Workbench checks passed.

The preserved pinned sharp dependency advisory reported by I2 remains outside scope; V2 did not upgrade dependencies or perform network audit. No CAD/browser/service/printer build or physical acceptance is inferred.

## Fictional external binding walkthrough

The ignored fixture at `.workbench/workflow-ownership/v2/fictional-external-project/` binds only `projects/example-widget`, exact fictional revision, null workshop and no machine commands. It contains an explicit read-only AGENTS instruction and an UNKNOWN candidate record. Applying the adapted instructions yields:

- Design reflection selects that external target, never Workbench's own tree. Missing canonical records/candidate checks and workshop availability remain UNKNOWN. Its next minimal experiment is capture the missing candidate evidence; no geometry/artifact/physical acceptance or write is authorized.
- Sticker production reports machine validation unavailable because no compatible `contract`, `candidate`, `review-lint` provider is bound. Jaelin's named npm command is a versioned example and cannot be executed as a fallback for this fictional pack.

This is an independent instruction walkthrough and scoped path/guard inspection, not a claim that an installed skill runtime or generic dispatcher exists. No production command was dispatched.

## Finding V2-1

The initial design binding used workflow ID `cad-fabrication`, while the pinned catalog canonical ID is `WF-CAD-FABRICATION`. The recipe path resolved, but the binding contract explicitly calls for workflow IDs. Reported promptly to the coordinator; I3 owns the correction and focused canonical-ID regression assertion. Repair rechecked: the binding now uses `WF-CAD-FABRICATION`, and a focused consumer regression assertion rejects an incorrect ID. The complete refreshed candidate manifest matches every file. `uv run pytest tests/test_repository_structure.py -k 'binding or workflow'` from the design consumer root passed 3 tests (8 deselected). A final full root run passed 10 and reproduced only the same pre-existing Laifen failure.

Ignored evidence: `validate.py`, `INPUTS.sha256`, `RESULT.json`, `check.log` and the fictional fixture. `REPAIR_INPUTS.sha256` separately freezes the updated candidate/binding/test. Unrelated provider/plugin changes do not expand this gate.

## Final evidence identities

- Refreshed design candidate manifest: `8abfd09926fd99188fff0169652a6442744e26a7bcf937a752c4d71bc15e65c3`.
- Binding SHA-256: `1a2fbc4b251d7e32b754dd8521b5aaa0fe5dec0881a2e4c1efb23a556cf314fb`.
- Consumer test SHA-256: `1bac5043a72dc8d49152686c403751834b69d627c19ea3aec42530ed9e4da07e`.
- V2 initial frozen inputs SHA-256: `5e16b222c81459960de79abaaebcf3108baaaac25b1fc536e98c761ef0b2442e`.
- V2 final result SHA-256: `3c15055bc7ace90a926751e69961822e36bd0cafeb433b3cd81d27cf87190526`.

One repair test invocation initially ran from Workbench, where pytest is intentionally unavailable; it failed to spawn without executing tests. The rerun used the design consumer's own approved root uv environment and produced the results above. No environment installation or fallback interpreter was used.
