# Workflow migration completeness review

Reviewer: `/root/boundary_inventory`, independent read-only reviewer. Date:
2026-09-08. This review owns only this record; it did not modify source/project
files, install anything, operate services, or run CAD/device workflows.

## Verdict

**Repair needed before claiming the entire workflow is consolidated.** The
baseline reusable-file inventory is fully mapped, and project-local retention is
appropriate. A baseline root instruction lost an explicit simulation restriction
when the root was slimmed, and a separate older canonical branch contains useful
reusable policy additions outside the selected migration baseline. Neither finding
means project CAD or evidence should be moved into Workbench.

Reviewed identities:

- Extraction baseline: `71d661c14098860b7a374e13043fb084994be8a0`.
- Source separation branch: `8c0710c49b60b8c17ff66fc424f608c07d420588`.
- Workbench HEAD at review: `f3c8628a9b09630951514110f7d66e2a13f59404`.
- Canonical design checkout HEAD: `a8834040afe401637d36e94bd8fdd9e1d9874d35`,
  branch `codex/xt60-p20-r1-fixed-rod-reset`, ahead three of its tracking branch,
  with preexisting tracked and untracked work.
- Additional policy commit: `03fab9a8f0d36a38c18a6789d17afec3ce41eb61`
  (2026-08-26, `wip: preserve P17 rail experiments and workflow updates`). Its
  branch and the extraction baseline share merge base
  `b69b6ad12af611644987f026eef4940db9c7bb34`.

## Full baseline inventory, beyond the extraction manifest

The baseline has 60 tracked files outside `projects/`. The 40 explicit entries in
`../2026-09-07-workflow-ownership/EXTRACTION.json` cover every file in these groups:

| Original reusable source | Workbench owner | Count |
| --- | --- | ---: |
| `docs/{ADDING_A_PROJECT,CAD_WORKFLOW,FDM_DESIGN_RULES,PROJECT_CONTINUITY}.md` | `workflows/policies/` | 4 |
| `.agents/skills/design-reflection/`, `.agents/skills/sticker-pack-production/` | `skills/` | 7 |
| `docs/templates/project-continuity/` | `templates/project-continuity/` | 12 |
| `tools/cad-viewer-service/` | same relative path; preserved legacy source | 17 |

The other 20 paths were inspected/classified, rather than assumed missing:

- Seven `docs/iterations/2026-08-31-printing-profiles/` files (`BRIEF.md`,
  `CANDIDATE.sha256`, `DESIGN.md`, `HANDOFF.md`, `RECOVERY.md`, `REVIEW.md`,
  `VALIDATION.md`) are historical evidence retained in the source repository.
- `docs/WORKSHOP.md` is project-repository inventory, not portable policy.
- `.github/pull_request_template.md` and `.github/repository-policy.toml` remain
  the source repository's delivery form/declaration. They retain local evidence
  pointers and do not provide a competing CAD policy implementation.
- `.gitignore`, `.python-version`, `package.json`, `package-lock.json`,
  `pyproject.toml`, `uv.lock`, and `tests/test_repository_structure.py` remain
  source-repository environment/dependency/consumer validation infrastructure.
- `AGENTS.md`, `README.md`, and `docs/ARCHITECTURE.md` become local ownership,
  commands and external-binding entrypoints. Their reusable semantics therefore
  require comparison beyond the 40-file checksum inventory.

The separation branch's AGENTS and README resolve the external binding and keep
project sources, generation, tests, dependencies, records and workshop facts local.
Shared policy compatibility pages are navigation, not duplicate implementations.
The Workbench README and `docs/architecture.md` distinguish reusable workflow,
project authority, upstream CAD, external printer/slicer services, and the preserved
host-specific legacy viewer. Moving that viewer source does not prove portable
runtime migration; its existing host dependencies intentionally remain explicit.

## Findings

### C1 — P2: baseline full-simulation restriction is weaker after root slimming

Baseline `AGENTS.md`, CAD workflow section, explicitly says an integrated/full
simulation follows passed small relationship gates and must never be the sole
user-validation surface. Current `workflows/policies/CAD_WORKFLOW.md:58` preserves
small teachable gates, exact confirmation, evidence boundaries and the exception
for already explicit unchanged intent, but omits those two integration restrictions.
The source branch's replacement AGENTS no longer carries them either.

Restore the integration restriction in that shared gate subsection while preserving
the newer explicit-intent/no-repeat exception. This is a narrow semantic migration
repair, not a reason to introduce universal approval gates.

### C2 — P2 for a universal completeness claim: divergent reusable policy remains

Commit `03fab9a8f0d36a38c18a6789d17afec3ce41eb61` adds generic guidance in
`AGENTS.md`, `docs/ARCHITECTURE.md` and `docs/CAD_WORKFLOW.md` that is not present in
the selected baseline. Current canonical files preserve it. The substantive
additions to reconcile are:

- Explicit spatial intent fields (frame, orientation, state topology, part identity,
  allowed motion), with expensive downstream work stopped while ambiguity is open.
- A per-object allowed-change/forbidden-change contract for bounded corrections;
  later narrower user instructions immediately refreeze the scope.
- One deterministic pure-math authority for repeated geometry/trajectory/frame
  relationships, shared by production callers; direct nominal/boundary,
  determinism, applicable inverse/round-trip, and caller-equivalence checks;
  BREP, tessellation and serialization downstream of cheap analytic acceptance.
- A failed analytic or intent gate stops downstream work; explicitly authorized
  evidence-only experiments remain non-candidates excluded from delivery claims.
- Validate media on the user's actual delivery surface before claiming usability;
  local render, HTTP success, viewer readiness or agent inspection alone does not
  prove that user experience.
- One current contract/candidate/source-artifact-independent-review authority
  chain, excluding superseded artifacts and acceptance receipts. Workbench already
  contains much of this through immutable manifests and continuity rules; reconcile
  the explicit no-mixing statement without adding a second authority.

This is **not evidence of baseline file loss**, nor proof these older instructions
should supersede every newer policy. Reconcile additive semantics individually.
Do not copy the old files wholesale: their branch lacks newer printing-profile,
canonical-backlog, current-gate and early-intent refinements already retained in
Workbench. Canonical uncommitted shared edits currently restore progressive gates
and printing-profile guidance already represented by the extraction baseline;
they are not automatically additional migration omissions. Project WIP remains
untouched and outside this software/policy transfer.

## Evidence and limits

Read-only checks used `git ls-tree -r --name-only` on the baseline, extraction JSON
inventory comparison, `git show` on the exact baseline/source/policy commits,
`git diff` for baseline-to-canonical-HEAD and canonical working changes, `git log`
restricted to shared paths, `git merge-base`, and `git status`. Content searches
used `/opt/homebrew/bin/rg` explicitly. Reviewed Workbench roots, four policies,
templates/skills/tool ownership, and the current plugin-install brief. Focused
searches found no equivalent full-simulation restriction or shared pure-math and
delivery-surface instructions in current `workflows/`, `skills/`, `contracts/`,
`templates/`, AGENTS, README or architecture.

This bounded review establishes path coverage and identifies policy deltas; it
does not claim exhaustive semantic extraction from every historical project record
or every Git branch. The coordinator owns the separate current 40-entry hashes,
installed-cache parity, binding pins, and remote PR/merge-state checks and may append
their exact executed results below. No costly prior preservation run was repeated.

## Independent repair disposition — 2026-09-08

**PASS for C1 and C2 semantic consolidation.** This disposition supersedes the
initial repair-needed verdict for the policy candidate identified below. Reviewer
`/root/boundary_inventory` independently inspected the coordinator's three-file
diff and surrounding policy sections without editing implementation.

| Finding | Verified disposition |
| --- | --- |
| C1 | CAD intent gate now permits integrated/full simulation after applicable small relationship gates pass and forbids it as the sole user-validation surface. |
| C2 spatial intent | Frame, orientation, state topology, identities and allowed motion are explicit; an unresolved applicable gate stops parallel downstream CAD/export/slicing/printing. |
| C2 bounded changes | Per-object delta mask includes allowed transforms/parameters, invariants and forbidden changes; a narrower later instruction supersedes and refreezes scope. |
| C2 parametric authority | One deterministic pure-math function is shared by affected parts/rails/generators; direct nominal/boundary, determinism, applicable inverse/round-trip and caller-equivalence checks precede BREP/tessellation/serialization. Existing named-parameter guidance remains. |
| C2 failed gates | Failed analytic/intent gates stop downstream work; the explicit evidence-only exception requires non-candidate labeling and exclusion from delivery/acceptance claims. |
| C2 delivery surface | User-facing visibility/readability/usability claims require actual delivery-surface evidence or user confirmation, limited to the checked interaction. |
| C2 active authority | One current contract, fingerprint and source-artifact-independent-review chain; superseded receipts stay outside current acceptance, using existing records/manifests. |

The explicit-and-unchanged-intent exception, no-repeat-confirmation rule and
no-universal-permission-check statement remain intact. The initial unresolved-gate
rule and later evidence-only exception read together preserve the boundary between
candidate progression and a separately authorized investigation. Newer backlog,
current-gate, printing-profile and PR/evidence separation rules are retained;
there is no wholesale replacement with the older branch policy.

Exact reviewed SHA-256 identities:

- `workflows/policies/CAD_WORKFLOW.md`:
  `2668c44ba23d9af326be3fad115688ba0b5050fa8a307dfcfae44e1c20a0f56a`.
- `workflows/policies/PROJECT_CONTINUITY.md`:
  `4ae55ba092616e33a7be1c1988f438a1c1a582e327814139c747ac8bf577c4ac`.
- `catalog/POLICY.sha256`:
  `b95f77ef16d317366d1c93f7ff76dee92c0e69976ce55facec10512e23b6c3cf`.

Executed checks: `git diff --` the three paths and focused surrounding reads;
`git diff --check --` the same paths (exit 0); `shasum -a 256` on the three paths;
`shasum -a 256 -c catalog/POLICY.sha256` (33/33 entries OK, exit 0).
No canonical design, project, package, installation or service mutation was made by
this reviewer. Packaging, installed-cache verification and consumer pin updates
remain coordinator-owned subsequent delivery gates. The bounded audit limits above
still apply: this does not assert extraction from every historical project record
or every Git branch.
