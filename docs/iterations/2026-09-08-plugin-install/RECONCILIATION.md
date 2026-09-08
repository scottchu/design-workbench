# Completeness reconciliation and plugin update

Date: 2026-09-08. User requested migration completeness before continuing plugin
installation. See [independent completeness review](MIGRATION_COMPLETENESS_REVIEW.md)
for the 60-file classification, semantic findings and source lineage.

## Root inventory checks before repair

Root compared all 40 extraction entries with the frozen design Git blobs at
`71d661c14098860b7a374e13043fb084994be8a0` and their current Workbench destinations:
all recorded source/destination hashes passed. The baseline skill/template/tool
inventory plus four policies equals those 40 paths exactly. On the separation
branch, 36 shared paths are retired and four policies are compatibility pointers
through `docs/workflows-binding.json`, pinned to Workbench
`36f41715ee2257c0f2e41e40329216e3d2b2747f`. An initial pointer assertion incorrectly
expected each page to repeat the SHA; following the central binding passed.

The already-installed `0.2.0+codex.20260908102059` package had 67 source files matching
both its receipt and current repository source. It did not need a reinstall until
this semantic repair. GitHub PR readbacks showed Workbench1, design23 and sticker1
OPEN; design `git ls-remote origin refs/heads/main` remained at the extraction
baseline. No merge or canonical-worktree cutover is implied.

## Additive policy repair

C1 restores the baseline AGENTS full-simulation restriction. C2 reconciles the
six policy groups from committed divergent guidance at
`03fab9a8f0d36a38c18a6789d17afec3ce41eb61`, without copying its older files wholesale.
CAD_WORKFLOW now covers spatial intent, per-object delta masks, shared deterministic
math and direct checks, downstream stop rules/evidence-only exceptions, and actual
delivery-surface evidence. PROJECT_CONTINUITY explicitly excludes superseded
candidate evidence from the current chain. Existing explicit-intent/no-repeat,
printing-profile, backlog and PR delivery rules are preserved.

The original EXTRACTION.json remains unchanged: it records the completed baseline
transfer, not this later adaptation. Its destination hashes are historical once
these two policy files evolve. The current policy index is catalog/POLICY.sha256;
its SHA-256 is `b95f77ef16d317366d1c93f7ff76dee92c0e69976ce55facec10512e23b6c3cf`.
Both consumer bindings still intentionally select the earlier accepted provider;
adopting the new policy revision and merging migration PRs remain explicit cutover
work. Canonical design WIP, private project assets and device providers are untouched.

## Focused validation

Executed from the root:

- `uv run python scripts/check_registry.py`: PASS, 12 capabilities, two recipes,
  local references and policy hashes; no recipe executed.
- `uv run python -m unittest discover -s tests -p 'test_registry.py' -v`: four PASS.
- `uv run python -m unittest discover -s tests -p 'test_package_plugin.py' -v`: eight
  PASS, including relocation, source boundaries and tamper detection.
- An initial pytest invocation failed because pytest is not a project dependency;
  the existing tests use unittest. No dependency was added.
- Plugin-creator marketplace helper returned `personal`; cachebuster helper changed
  only the suffix to `0.2.0+codex.20260908111035`.
- `uv run python scripts/package_plugin.py --output .workbench/plugin/completeness-20260908/cad-workbench`:
  PASS build and readback. Receipt SHA-256:
  `288ad0800e50769ca537b5e1f00cf19c9d2bc2886f5d24d9484c5fb72c14339a`.
- Bundled plugin-creator `validate_plugin.py` on that output: PASS.
- `uv run python scripts/simulator_service.py status`: loaded, healthy, managed,
  installed_for_login; same root instance `ca3daa81c9c60ef20aa7f16b`, localhost4179.

The receipt identifies base Git HEAD plus exact hashes for uncommitted declared
inputs. This documentation/policy change does not justify repeating CAD generation,
app build or printer tests. Full portable design-to-print execution remains unproven.

## Installation result

After independent C1/C2 review PASS, root preserved the old maintained source at
ignored `.workbench/plugin-install/source-before-completeness/cad-workbench`, then
copied the reviewed package to `/Users/scottchu/plugins/cad-workbench`. Before
copying, the complete old source inventory/hashes equaled the old installed cache;
afterward the complete maintained source equaled the new package. Source-package
readback passed. `codex plugin add cad-workbench@personal` succeeded.

`codex plugin list --marketplace personal --json` reports installed=true and
enabled=true for `0.2.0+codex.20260908111035`; U1 remains at its earlier enabled
version. All 67 cached source rows match both receipt and current repository hashes,
and the complete cache inventory including receipt/input manifest equals the staged
package. Bundled validation passed directly on the new cache. Marketplace bytes
are unchanged from the before-update snapshot. A final service status again reports
loaded/healthy/managed with the same instance; no service or network mutation ran.
The final Workbench commit and PR contain this evidence; no PR was merged.
