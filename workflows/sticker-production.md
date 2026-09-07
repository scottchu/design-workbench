# Source-bound sticker production

**Workflow:** `WF-STICKER-PRODUCTION`  
**Capabilities:** `CAP-INTENT-GATE`, `CAP-VISUAL-REVIEW`, `CAP-HANDOFF`,
`CAP-ENV-DELIVERY`

Use this recipe for identity-sensitive sticker art derived from supplied sources. Workbench owns the [production skill](../skills/sticker-pack-production/SKILL.md); the external project owns its source, audit implementation, art, contract, evidence and approvals. This mapped recipe has not been run as a portable workflow.

## Inputs and boundary

Resolve the [project binding](../contracts/project-binding.md), verify the project revision and source hashes, then read the production skill and relevant references. Bind actual audit commands from the project; Jaelin's npm provider is an explicitly versioned example, not a universal implementation. Missing compatible audit tooling leaves that gate pending. Source authority and live evidence stay project-owned.

## Gate sequence

1. **G0 source authority:** freeze byte-preserved sources, names, roles, order,
   platform partition, authority precedence, and SHA-256. Stop on ambiguity or
   drift.
2. **G1 design contract:** one ordered contract row per slot. The user approves
   scene, pose, prop/contact, exact text or `null`, and allowed differences.
3. **G2 risk pilot:** cover each production method and the material identity,
   anatomy, occlusion, prop, edge, and typography risks. Machine preflight runs
   first; the user judges identity/feel; a distinct critic judges defects.
4. **G3 bounded waves:** at most eight unreviewed slots. Preserve passing hashes,
   rerun only failed slots within the canonical attempt ceiling, and stop a wave
   when two slots show the same method-level defect.

For one to three new assets or a narrow edit, use the skill's `DESIGN-PREVIEW`
gate. It can validate a design choice but cannot bypass G0-G3 production gates.
Text remains deterministic composition from an exact Unicode/font/method
contract; image generation does not render final copy.

## Evidence and receipt

Run only the commands resolved by the bound repository. Interpret exit codes
literally: the inspected `candidate` command normally returns `5` after clean
machine checks because human review is pending. Machine status, independent
review, and user design approval remain separate.

Record `domain_extension.sticker` with gate, contract SHA-256, candidate hashes,
stable implementer identity, distinct reviewer identity, machine result, human
disposition, user-approval path/hash, and any untested platform sizes. Promotion
requires current masters to match the audited hashes.

Stop at the earliest affected gate for source drift, ambiguous rows, unpiloted
methods, machine failure, incomplete review, unavailable independent review, or
disputed identity/anatomy/semantics.
