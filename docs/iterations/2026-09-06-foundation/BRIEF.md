# Foundation iteration

Date: 2026-09-06
Baseline: empty local Git repository, unborn `setup/foundation` branch; no remote.
Owner: root coordinator. User request: start setting up the repository based on the preceding CAD workflow discussion.

## Requested outcome

- Establish CAD Workbench as the reusable software repository. Actual designs and physical observations remain in design-projects.
- Preserve the intended design -> CAD review -> preparation -> printer observation workflow, with separate domains and execution boundaries.
- Reuse a pinned text-to-CAD/cadgen release initially; evaluate selective forks only from demonstrated integration blockers.
- Provide a reproducible local development environment and a small, real CAD generation/export verification path.
- Document current implementation honestly and maintain a roadmap with observable exit gates.
- Preserve early, small user validation of ambiguous design intent and distinguish CAD, artifact/slicer, and physical evidence.

## Scope boundaries

No migration or modification of existing repositories, no upstream rewrite, no remote repository creation/push, no deployment or printer operations. Do not build a placeholder editor or claim the future UI, slicing, or monitoring integrations exist. Do not copy private design assets, printer profiles, credentials, or raw conversations. Only generic developer fixtures belong here.

## Coordination DAG

User steering during implementation: use asdf for Node, Bun and most development tools. F0-D updates decision 0001 and F0-I pins the selected toolchain locally; do not modify global tool settings.

| ID | Owner/role | Dependencies | Exclusive output | Done gate |
| --- | --- | --- | --- | --- |
| F0-D | reboot_architecture / architecture and documentation | brief + empty baseline | README.md, AGENTS.md, docs except iteration status/evidence | Small frozen foundation contract, architecture and roadmap; exact handoff to implementation |
| F0-I | text_to_cad_audit / implementation | F0-D contract fingerprint | workspace configuration, locks, packages, scripts, generic fixtures/tests | Installable environment and working bounded CAD smoke path |
| F0-V | workflow_evidence / independent validation | F0-I candidate fingerprint | iteration VALIDATION.md and ignored validation output | Prescribed checks and actual exported geometry readback; no source edits |
| F0-R | independent reviewer / formal review | F0-I + F0-V | iteration REVIEW.md | Scope, install commands, provenance and documentation reviewed |
| F0-H | root / coordination | F0-V + F0-R | PROJECT_STATE.md, NEXT_AGENT.md, iteration HANDOFF.md and manifest/status indexes | Reconciled result and local source commit |

At most three workers. Each task receives a SHA-256 manifest of its decision-bearing files before execution. Mutable coordination/evidence records are excluded from candidate manifests. One writer per scope. No commits by workers. Initial attempt plus at most two focused repairs; stop and report reproducible external blockers. Architecture budget: about 4 minutes; implementation: about 12 minutes; validation/review: about 5 minutes each. These are qualitative ceilings, not tool-enforced limits. Use balanced reasoning for bounded setup; strong reasoning for independent review where needed.
