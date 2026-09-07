# Workflow ownership and project separation

Status: implementation in progress. Coordinator: Workbench root task.

## Authority and frozen baselines

The user transferred work from task 01a07973-41f4-7f72-864c-160d5171bd18 to this task and requested reusable workflows in CAD Workbench, with design-projects retaining projects only. Final write ownership release was received before mutations. This supersedes the separate workflow-library proposal and the prior next-action ordering; Laifen UI work remains pending.

- Workbench baseline: e336afc34bd2fa1709dd1760b5990d4bf3cf0fba; delivery branch codex/workflow-ownership; upstream default setup/foundation.
- Source: /Users/scottchu/.codex/worktrees/0868/design-projects, codex/separate-sticker-repository, 71d661c14098860b7a374e13043fb084994be8a0.
- Draft library: /Users/scottchu/Projects/personal/workflow-library, empty baseline 8624fb05d23cc3b747df0d46eecc55e3d8f404dd plus untracked checkpoint.
- Sticker destination: /Users/scottchu/Projects/personal/sticker-projects, codex/separate-sticker-repository, dafdb8eb9b0cbc9449dce84a225f2a59f3e3f88b plus docs/recovery checkpoint.

## Outcome and boundaries

Workbench owns a small discoverable catalog of twelve reported capability categories, two mapped recipes (sticker production and CAD fabrication), reusable policy/templates/skills and artifact/source/hash/evidence contracts. It does not introduce a workflow engine or force shared runtime environments. Canonical providers and their revisions, maturity evidence and completion gates must be explicit.

Project source, local generation logic, tests, assets, requirements, observations, accepted releases and historical records remain project-owned. Preserve projects/jaelin-sticker-pack relative paths. The sticker project is separated with history and distinct recoverable WIP; no stale WIP overlay. Shared workflow implementations and copied policies leave design-projects, with minimal explicit external references/bindings for discovery and compatibility. Workshop facts are project context, not reusable policy. Preserve existing live services without operating/reinstalling them. No art/CAD generation, printer operations, plugin registration or service deployment.

The canonical design checkout and original live-pilot worktree are read-only. Preserve the draft workflow-library and both empty private remotes; do not delete them. No source retirement before independent path/byte/recovery checks. Delivery uses review branches and PRs; no merge in this task.

## Bounded work and ownership

| ID | Owner | Scope | Dependencies / exit gate |
| --- | --- | --- | --- |
| B1 | boundary_inventory | Read-only source ownership/dependency assessment | frozen source and draft; concrete mapping and credible checks |
| I1 | workbench_implementation | Workbench catalog/contracts/workflows/skills/templates/tool source and focused checker | B1; no embedded project authority or invented runtime maturity |
| I2 | sticker_migration | sticker-projects only, history/recovery/root setup | checkpoint; accepted bytes preserved, divergent history retained, scoped checks |
| V1 | preservation_validation | independent read-only migration checks, evidence record only | I2; source/destination byte/path parity and actual recovery readback |
| I3 | design_separation | 0868 source checkout only, root bindings/policy/tests and removal of verified migrated paths | I1 + V1; project source/evidence untouched except authorized sticker retirement |
| V2 | acceptance_validation | independent checks of frozen final candidate, evidence only | I1/I2/I3; links/contracts/root checks and preserved identities |
| R1 | formal_review | separate read-only joined review | V1/V2; findings resolved before delivery |

One writer per namespace; at most three workers active. Root maintains coordination, input/candidate manifests, continuity and Git delivery. Task manifests bind relevant source and contracts; mutable evidence/status excluded. Workers return exact commands, hashes, findings and limitations. Qualitative ceilings: bounded scopes about 5–12 minutes each, initial attempt plus at most two focused repairs; checkpoint a concrete blocker rather than expand scope. Models/reasoning inherit unless an applicable repository rule requires otherwise.
