# Independent plugin and simulator review (R2)

Status: **PASS — R2-1 repaired and independently rechecked.** No material source-review finding remains in the reviewed plugin/simulator candidate. Simulator interactive acceptance and independent V3 validation are separate join gates, not implied by this source review.

Reviewer: `/root/boundary_inventory`, independent of I4 `workbench_implementation`, I5 `sticker_migration`, and V3 validation. The reviewer performed earlier read-only architecture inventory and R1 migration review; it implemented neither new component. Only this review file was written.

## Scope and candidate identity

Reviewed the user boundary in PLUGIN_ADDENDUM.md and both PLUGIN_IMPLEMENTATION.md and SIMULATOR_IMPLEMENTATION.md. Workbench owns a workflow plugin and dedicated local SvelteKit simulator host. Existing Orca owns printer/slicer MCP, API, dashboard and widgets. The migration provider `36f41715ee2257c0f2e41e40329216e3d2b2747f` retains separate R1 approval; newer package bytes do not silently upgrade consumer bindings.

Source was still uncommitted. Decision-bearing identities inspected:

| Path | SHA-256 |
| --- | --- |
| `scripts/package_plugin.py` | `44f5795944ee8ed88e47be32be41c982f9cebc50dc8fa88fc76dadb1bc38375d` |
| `skills/workbench-flow/SKILL.md` | `e52280da70eea94d4c784c09e756d0dbd60f49e2dd17df134924eaab7ccf68e2` |
| `apps/simulator/src/lib/server/registry.js` | `5b00d96c326a569fbb0a4342bc51991e488c0e6b1a46ed01028b6342d79d998e` |
| `apps/simulator/scripts/register.mjs` | `b067a493ba6d21b141d633182ccb1e87402ec6fbc832f078123eda9730f5d08c` |
| `apps/simulator/vite.config.js` | `001dd122d02f2e5d5eff1d483d002073ea90f31f48aafffe5127d4a6cee9d5b7` |
| `.workbench/plugin/cad-workbench/PACKAGE_RECEIPT.json` | `082ea1c85522e44417a2c4b6d568e2dd32c7e707226949891dbef7cde3f016ca` |

## R2-1: isolate unavailable simulator registrations (P2)

`loadRegistry` validates every registration's existing filesystem roots and selected source bytes inside one `Promise.all`. Every asset route and selected simulator route first awaits that whole list. A normal source edit in simulator A, or disappearance of its old worktree, therefore makes unchanged simulator B's assets return 404 and removes all cards from the index. The local registration CLI also validates its candidate through this same function, so a stale registration blocks adding an unrelated valid simulator.

The source-hash gate should continue refusing A's stale assets. Its failure must be scoped to A: retain healthy registrations and expose the unavailable entry with its reason. Global schema/duplicate-ID ambiguity may still reject the whole registry. This is necessary for the shared host to support independently maintained project simulators without one project edit disabling all others.

Focused exit gate: two registered simulators, mutate/remove A's source or registered root, then verify B remains listed and its unchanged bytes remain readable; A remains unavailable and cannot serve old assets. Verify adding valid C is not blocked by A's stale source. No project source changes or weakening of hash/path checks is requested.

This finding follows directly from the inspected call graph (`loadRegistry` -> all source checks; index/selected/asset/registration consumers -> `loadRegistry`). R2 did not mutate live registry or project files to demonstrate it. Existing tests exercise single-entry drift rejection and do not cover sibling isolation.

## Other assessment

- **Packaging boundary sound:** source authorities are reused through a contained generated package, with explicit source/output hashes, no overwrite of an existing reviewed output, symlink/input checks and output readback. The package excludes legacy host configuration, project assets, external CAD/U1 code, credentials and fake MCP registration. Runtime installation is explicitly separate.
- **Workflow instruction walkthrough:** preparation-only ends at identified validated G-code; observation-only calls the external read-only provider independently of CAD success; missing start provider remains unavailable; explicit exact-artifact start retains installed external workflow authorization/preflight. Installed provider versions are distinguished from maintained source. No duplicate printer/slicer API or dashboard was introduced.
- **Actual simulator integration boundary sound:** the host serves unchanged registered built files, not invented model geometry. The selected source hash and observed revision are explicitly limited provenance; complete dependency/build attestation and physical acceptance are not claimed. Same-origin registered code is documented as trusted, not a hostile-code sandbox.
- **Path checks inspected:** relative assets reject traversal, hidden/encoded/backslash paths; realpath confinement and content hashes guard registered file reads; no HTTP registration/write API or arbitrary URL proxy exists. Loopback defaults and strict port are explicit.
- **HTTP spot checks:** read-only `curl -s -o /dev/null -w ...` against the task-owned server returned 403 for `/@fs/Users/scottchu/.codex/worktrees/7e46/CAD-workbench/.workbench/simulators.json` and the corresponding `pyproject.toml` path, including a foreign Origin on the latter. Attempts to request server-only registry source through Vite returned 500, not source bytes. These probes do not establish a complete hostile-origin/security audit and did not read or change credentials.

## R2-1 repair re-review

R2 independently read the repaired registry, registration CLI, selected route and index presentation, then ran `npm run test:simulator` from the Workbench root: **8/8 PASS**, exit 0. No build/check/dev command or live registry mutation was run during this review.

The loader now validates global identity ambiguity separately, resolves allowlisted roots with settled results, and records each unavailable registration independently. Healthy B stays listed and its original bytes remain readable after A's source drift or root removal. A remains visible as unavailable and cannot serve its assets. The selected route rejects unavailable entries; the index presents their reason without offering an open link. The actual CLI regression adds healthy C without repairing or overwriting stale A. Required hash, path, MIME and duplicate-ID failures still pass their existing tests. This closes R2-1 without weakening its fail-closed requirement.

Repaired candidate SHA-256:

| Path | SHA-256 |
| --- | --- |
| `apps/simulator/src/lib/server/registry.js` | `9b1bbd3b991ee085361791def721187e599caa6a7eafa9a72c9b60946ea488d7` |
| `apps/simulator/scripts/register.mjs` | `31a0c0b8052eadbcc6fd7963ebc328943a6a3b24cfc007d453f384e062a2e8dc` |
| `apps/simulator/tests/registry.test.js` | `b192f8fdd77477d6d3d63f19b11336311b0d139bdebf2692ca5a8acbdfb2053a` |
| `apps/simulator/src/routes/+page.svelte` | `ccfd2ceddf285561cbf829631625d8da017668a5ba08787c5dac58a0c59bcd49` |
| `apps/simulator/src/routes/simulators/[id]/+page.server.js` | `41646dc7b52e2a445fd33f6c7a241c8cbbee0781d08776fda7c8463a4aa958f1` |

The original finding and rejected hashes above remain historical evidence. No package source change was requested by R2-1; I4 package identity stays separately bound.

## Remaining acceptance

R2 source review and the focused repair gate pass on the identities above. Join V3's actual package checks/tests and the root's browser evidence for list/open, real WASM rebuild after parameter change and current STL download. Root reports a successful 180 mm parameter build/download with STL bounds changing from 39 x 39 x 219 mm to 39 x 39 x approximately 186 mm; this is coordinator-reported evidence, not independently repeated browser/artifact acceptance by R2, and must be bound in the root/V3 record. An HTTP 200, generated package or screenshot alone does not pass that interactive gate. No provider calls, service installation, external deployment or printer action was performed by R2.
