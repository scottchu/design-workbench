# Playground source rename validation

Date: 2026-09-08. Root: `/Users/scottchu/Projects/personal/CAD-workbench-next`.
Base: `e2e243f`, branch `codex/composable-skills`, PR4 follow-up.

## Commands and results

| Command from root | Result |
| --- | --- |
| `npm install --ignore-scripts` | PASS; workspace link replaced, existing three low advisories remain; no dependency upgrade |
| `npm ls --workspaces --depth=0` | Resolves @design-workbench/playground to ./apps/playground with pinned dependencies |
| `uv run python -m unittest discover -s tests -v` | 32 pass, including three new legacy-path compatibility tests |
| `uv run python scripts/check_registry.py` | PASS: policy hashes and references |
| `npm run check:playground` | Zero errors and warnings |
| `npm run test:playground` | 11 pass |
| `npm run build:playground` | PASS: actual adapter-node production build at new path |
| `uv run python /Users/scottchu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/simulator-page` | PASS |
| `uv run python /Users/scottchu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/simulator-server` | PASS |
| `uv run python scripts/package_plugin.py --output .workbench/playground-name/candidate-2/cad-workbench` | PASS: 70 source/output files, actual package readback |
| `uv run python scripts/package_plugin.py --check .workbench/playground-name/candidate-2/cad-workbench` | PASS |
| `git check-ignore apps/simulator/build/index.js apps/simulator/.svelte-kit/generated.js apps/playground/build/index.js apps/playground/.svelte-kit/generated.js` | All four paths ignored |

Compared lockfile package entries against `git show e2e243f:package-lock.json`:
all entries outside the old/new workspace package and symlink keys are identical.
All 70 packaged file hashes were also compared to current source and matched.
Old `*:simulator` npm scripts forward to canonical `*:playground` scripts; no
claim of starting dev servers is made. The build reported an empty env.js chunk,
but completed successfully; no warning was hidden as a runtime check.

## Exact identities

| File | SHA-256 |
| --- | --- |
| package-lock.json | `8c219ff1b7a0e646a7d3785f0fed3b7a52d74b83420e5bd8f6b7afe17f4ecb78` |
| scripts/simulator_service.py | `f44b455c2d59e1600b7d2b63d7e67184460b19830099c233acd93644eb33040f` |
| apps/playground/build/index.js | `3b35d0c50706a8a0bfde97d4b764c66ca59096d724ec4dd03b68aa8e784b2a32` |
| catalog/POLICY.sha256 | `168a8dbcf612e22de7c822b590b9b5f4a4beffdd82a7a99fcbd2eff152c5d7fd` |
| candidate-2 PACKAGE_INPUTS.sha256 | `69787085433c45a656f0f20aed75f5268da6ad0732466bd58d9e591c2b147fcc` |
| candidate-2 PACKAGE_RECEIPT.json | `bc541447154dce70c6c3254f7c201176bf3b347baf1947bf25bbfe3472c8cd62` |

Candidate-2 lives under ignored `.workbench/playground-name/`; its receipt combines
base Git revision with exact uncommitted declared input hashes. It supersedes
candidate-1 after the reviewed app_root resolution clarification. The standalone
build-entry hash identifies that file only, not a full production deployment.

## Acceptance boundary

[Independent review](REVIEW.md) probes stopped legacy reuse, missing new build and
foreign legacy configuration using isolated fake lifecycle providers. Tests prove
source compatibility behavior, not successful migration of the running service.
No live launchctl/server request, private registry mutation, browser session,
plugin installation, root directory rename, external project edit or CAD/export
operation ran. UI naming was built and type-checked, not visually browser-accepted.
