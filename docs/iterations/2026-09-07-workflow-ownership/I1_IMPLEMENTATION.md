# I1 implementation receipt

Owner: workbench_implementation. Scope: Workbench reusable content only. No commits, remote changes, project source mutations, plugin installation, art/CAD generation or service operation.

## Input identity and path incident

Initial `shasum -a 256 -c .workbench/workflow-ownership/I1-inputs.sha256` passed all declared inputs. The original 0868 source checkout then disappeared; cause unknown. Implementation read immutable blobs at `71d661c14098860b7a374e13043fb084994be8a0` through the canonical design-projects Git object database only, not its working files. The coordinator subsequently supplied `design-projects-workflow-separation` and reported all 43 relocated inputs verified. Source paths/revision/hashes are in `EXTRACTION.json`.

The workflow-library untracked draft supplied category IDs and recipe structure. Its unvalidated separate-library ownership and broad maturity claims were rewritten. Its malformed receipt JSON was replaced with valid JSON Schema; this is an envelope contract, not a runtime acceptance validator.

## Delivered content and identity

- `catalog/`: twelve categories and two recipes, provider kind/path/version/commands, evidence limits, gates and policy manifest.
- `contracts/`: project-owned binding requirements and receipt/provenance envelope.
- `workflows/`: two recipes plus four adapted shared policies.
- `skills/`: two existing skills with explicit external project/runtime/inventory bindings. The Jaelin audit CLI is a versioned provider example, never a universal implementation.
- `templates/project-continuity/`: twelve templates, with policy reference adaptation.
- `tools/cad-viewer-service/`: seventeen original files, byte-identical with executable modes preserved; `tools/LEGACY_VIEWER.md` separates history and live service dependencies.
- `scripts/check_registry.py` and `tests/test_registry.py`: catalog/reference/hash checks and four credible failure tests.
- `docs/decisions/0002-workflow-ownership.md`: ownership and adaptation decision.

`EXTRACTION.json` maps forty old/new paths and SHA-256 values, distinguishing identical and adapted content. Its SHA-256 is `4320a2daf24d784dbab7536bfee1e4d11e1299bf94cbd92d3e160c16f8153e97`.

`catalog/POLICY.sha256` SHA-256 is `dc6d7e776edd2bacb6f96baa462f41f1e427eae562fd77b398493f9de9f4c47b`. It pins maintained catalog/contracts/workflows/skills/templates; delivery Git revision is separately assigned by the coordinator. This is a candidate, not a published or installed package.

## Commands and results

- `uv run python scripts/check_registry.py` — PASS: twelve categories, two recipes, safe local paths, declared metadata, policy bytes and maintained Markdown links. This does not execute workflows or validate domain acceptance.
- `uv run python -m unittest discover -s tests -p test_registry.py -v` — 4 PASS: clean candidate, policy-byte tampering, unknown capability ID and escaping recipe path.
- `uv run python /Users/scottchu/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/design-reflection` and the same command for `skills/sticker-pack-production` — initially blocked by `ModuleNotFoundError: No module named 'yaml'`. The coordinator added root dev dependency `pyyaml==6.0.3` through uv; both commands then reran and PASS. No alternate environment used.
- Manual root `uv run python` readback checked both SKILL.md plain-scalar frontmatters for exact name, nonempty description and no unfinished scaffold; PASS. Maintained local skill links pass the registry checker. This does not replace behavioral forward-testing.
- Root `uv run python` readback compared each of the seventeen legacy file hashes against `EXTRACTION.json`, then called `node --check <absolute-path>` for every `.mjs` in that set; PASS. It independently read `payload/install-manifest.json` and checked SHA-256 and mode for its seven payload entries; PASS. No module was imported or executed, and no installer, runtime-refresh test or service command ran.
- `git diff --check` — PASS for tracked changes (new files also inspected by focused checks).

## Acceptance limits and remaining join

Policy/source relocation and discovery checks are implementation evidence only. The independent validator/reviewer must review project bindings, preservation, skill behavior and cross-repository references on the final joined candidate. The reusable source does not establish portable recipe execution, current Grenadier/XT60 capability acceptance, slicing readiness or physical/platform acceptance. Legacy root wording tests should not be retained as a requirement for project compatibility pointers to duplicate policy text; functional catalog/hash checks live with Workbench ownership.
