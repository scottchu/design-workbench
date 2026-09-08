# Independent migration review (R1)

Status: **PASS for the frozen workflow ownership and repository separation candidate.** No material repair finding remains in this gate. This is not approval of the concurrent plugin/simulator additions or of remote delivery, installation, services, production art, CAD generation or physical/platform acceptance.

Reviewer identity: `/root/boundary_inventory`, acting as `R1 formal_review`. This reviewer performed the earlier read-only boundary inventory, but implemented none of I1/I2/I3 and owns neither V1 nor V2. Implementation owners were `workbench_implementation`, `sticker_migration` and `design_separation`; independent validator owners were `preservation_validation` and `acceptance_validation`. Review is read-only except this file.

## Frozen candidate

- Workbench provider: `36f41715ee2257c0f2e41e40329216e3d2b2747f`. Provider content was reviewed through Git blobs, excluding newer concurrent packaging/source changes.
- Provider policy manifest: `6f1ab6580b67cd9e58dd2302f07cdc65a3a2bfa2213e650139a7ce4542bf9536`, 30 entries.
- Design consumer: `b8b0f5d9e38a2b2d1f1f6b07b9ec6f9f283c8565`; candidate manifest `8abfd09926fd99188fff0169652a6442744e26a7bcf937a752c4d71bc15e65c3`, 14 entries; binding `1a2fbc4b251d7e32b754dd8521b5aaa0fe5dec0881a2e4c1efb23a556cf314fb`.
- Sticker consumer: `33fcac4f56ccb0dbc59f54c7882f9c16acfd58bf`; project manifest `e48e7464f8e8840b9018664a06d39ff043c0cd2bc171f1441b6e2b2e097c47a2`; binding `be5ffaa9bdf87a62a0ef9326af9117439827987bb3511155ab2faff0586b82b0`.
- Original design authority: `71d661c14098860b7a374e13043fb084994be8a0`; source recovery branch still resolves to that exact commit.

Both consumer working trees were clean at review. Subsequent candidate changes require scoped re-review; this approval does not float with a branch.

## Joined findings and requirement coverage

- **Ownership PASS:** reusable policies, templates, skills and legacy viewer source move to Workbench; project source/generation/tests/assets/decisions/evidence stay with projects. Four design policy paths and the sticker SKILL path are short compatibility pointers, not duplicated workflow implementations. Local workspace and delivery instructions remain legitimate repository bindings.
- **Preservation PASS:** independent V1/V2 evidence establishes 848 sticker project files, 2,504 remaining design/context files, eleven filtered-history mappings and actual isolated WIP restoration. R1 separately compared all four project Git tree identities, the forty extraction mappings, provider manifest and final design candidate. No project tree changed. Historical manifests and release paths remain intact.
- **Bindings PASS:** both consumers pin the same exact provider revision and manifest hash. Canonical workflow IDs match the provider catalog. Sticker command entries identify direct Bun argv, working directory, pinned runtime, source revision/hash, required unresolved inputs and separate evidence paths. R1 verified every listed source-entrypoint hash. The CAD consumer deliberately has no selected project build command; project selection must resolve its source and current records before execution. This is an explicit unselected capability, not a claimed generic dispatcher.
- **Recovery PASS:** exact patch/tar hashes still equal V1 inputs. R1 verified the destination-contained filtered recovery base has the same project and skill trees as the original baseline. V1's actual isolated apply/extract/readback remains applicable; it was not repeated. Original WIP remains distinct and unpromoted under the preservation evidence. Retained history maps and refs include the divergent documentation lineage and V2 tag.
- **Live-service boundary PASS:** legacy viewer payload was transferred unchanged. Host-specific canonical Python, installed payload and runtime lifecycle are explicitly separated from source ownership; this review did not operate them.
- **Prior finding V2-1 resolved:** final design binding uses `WF-CAD-FABRICATION`; independent V2 rechecked the correction and its focused regression assertion. No policy-copy workaround was introduced.
- **Draft reconciliation PASS:** retained `workflow-library/WORKBENCH_HANDOFF.md` explicitly supersedes the abandoned separate-library ownership without deleting the draft. Its empty-remote status is retained coordinator evidence, not a new network check by R1.

## Review execution

Read BRIEF, HANDOFF, I1_IMPLEMENTATION, PRESERVATION_VALIDATION, VALIDATION and the frozen EXTRACTION.json; consumer AGENTS/README/architecture/bindings/recovery records; current consumer test changes; pinned catalog and binding contract. Used explicit `/opt/homebrew/bin/rg` for searches.

From the Workbench root, `uv run python -` performed a read-only standard-library check using `git show <revision>:<path>`, `git rev-parse <revision>:<project-path>` and SHA-256. Results: 30 provider manifest entries PASS; 40 extraction source/destination identities PASS; 14 design candidate entries PASS; all project tree identities and source recovery ref PASS; both provider bindings PASS; sticker executable-source bindings PASS; filtered recovery base trees PASS. It printed the exact manifest/binding/patch/tar hashes recorded here. No scratch script or restored checkout was created by R1.

Additional exact checks:

```sh
# Design consumer root
git diff --check 71d661c14098860b7a374e13043fb084994be8a0 b8b0f5d9e38a2b2d1f1f6b07b9ec6f9f283c8565
git cat-file -e 71d661c14098860b7a374e13043fb084994be8a0:projects/laifen-wave-case/docs/iterations/2026-09-06-pattern-reference-intake/VALIDATION.md
# Sticker consumer root
git diff --check dafdb8eb9b0cbc9449dce84a225f2a59f3e3f88b 33fcac4f56ccb0dbc59f54c7882f9c16acfd58bf -- . ':!recovery/live-pilot-fef4f264/tracked-delta.patch'
git show-ref --heads --tags
git status --short
```

Whitespace checks passed. The preserved binary patch is intentional archived evidence: its original context-line whitespace is excluded, never normalized. Patch SHA-256 is `217a6b03fc4d03d0c465a8faed962f770af7b48b76dd85bdcf45bee3654c4f98`; tar SHA-256 is `3a1326940a91e572792dc4ff7ebf66b8628cad7e8d41007e18b96cbcb87e978e`.

The `cat-file` check returned exit 128 because the Laifen VALIDATION.md is absent in the original baseline, independently confirming the reported pre-existing defect. Retain V2's **10 design checks passed / one unchanged baseline failure**, **9 Workbench checks passed**, and **14 sticker checks passed** as validator evidence; R1 did not rerun these suites. Full POSIX metadata, clean-machine bootstrap, portable workflow execution, JSON Schema runtime conformance and platform/physical acceptance remain unproved as recorded by V1/V2.

## Delivery handoff

Proceed with the separately authorized PR delivery after the coordinator updates current status/handoff indexes to distinguish completed migration gates from pending plugin review and delivery. Existing checkpoint prose saying retirement or validation is pending must not be reported as current completion state. This is a continuity-tail action, not a request to rewrite historical evidence or alter the frozen accepted project trees. Preserve recovery refs when publishing; do not merge or operate services/devices under this review.
