# Current source and evidence

The current documents must explain the product, effective choices, demonstrated
behavior and unresolved work without replaying conversations or iterations.
Git commits and pull requests preserve how those documents changed.

## Source ownership

Product intent explains why and the desired outcomes. Specifications define
behavior and acceptance. Concepts define meaning and relationships; architecture
assigns responsibilities, interfaces and constraints. Workflows describe how to
produce and review outcomes. Each topic has one owner; these roles do not require
a separate folder for every kind of document.

Decisions record adopted choices, rationale, scope and explicit supersession.
Technical stacks can be replaced through a new decision while preserving required
behavior. Effective build parameters select a target under those constraints;
not every decision is merely a parameter. If a technology is itself a product
requirement, replacing it also requires changing that requirement. Evidence for an
old implementation does not automatically validate the replacement.

Reconstruction consumes effective source and decisions at an identified revision,
plus declared target parameters, dependencies and generation tooling. It should
not infer current requirements by replaying historical iterations. Derived ASTs,
ontologies and composition graphs cannot silently change their source.

## Iteration closeout

An iteration may use temporary planning and handoff notes. When its intended work
is complete, incorporate adopted intent, behavior, architecture and acceptance
conditions into their owning documents. Retain unresolved matters as explicit
open questions, not completed behavior. Summarize lasting findings and limits in
current verification documentation and link the evidence that supports them.

Remove notes whose planning or handoff purpose has ended once their useful content
is accounted for. Git retains their earlier revisions. Do not require a fixed
brief/validation/review/handoff bundle for routine changes or duplicate commit
chronology in documents.

Current verification prose explains the question, method, result, scope and
limitations. Exact commands, stack versions, machine paths, raw reviews and hashes
belong in separately identified evidence or executable verification tooling.
Evidence must remain retrievable, not merely referenced in a disposable worktree.
The current reconstruction uses tracked generic records under `evidence/`.
Private runtime and project data remain with their owners.

Existing historical records with consumers or package dependencies remain until
their useful content and references are deliberately reconciled. This rule does
not authorize a blanket deletion of old iterations.

## Delivery and worktree lifecycle

After review and integration, remove temporary development worktrees only after
checking tracked, untracked and ignored contents for unfinished work and unique
evidence. Preserve unresolved work in its existing location or an explicitly
identified recoverable location. A running service root has a separate lifecycle.

PROJECT_STATE records actual delivery, runtime and remaining acceptance gaps that
Git alone cannot establish. NEXT_AGENT provides navigation. Neither is a second
product specification or chronological task log.
