# 0003: Focused skills composed by documented workflows

Status: accepted direction for incremental implementation, 2026-09-08. Step 1
records the boundary; step 2's local source extraction passed the checks in the
[active validation](../iterations/2026-09-08-composable-skills/VALIDATION.md).
Installed-skill and live acceptance remain pending.

## Decision

The project owns what is being made and what the user approved. The workflow owns
how it is produced, checked and revised. Skills guide bounded tasks; tools execute
operations. Design decisions discovered through a workflow remain project-owned.

| Layer | Owns |
| --- | --- |
| Project | Intent, requirements, source, parameters, configuration, candidates, actual commands and inputs, evidence, approvals, current state and next action. |
| Workflow Markdown in `workflows/` | Cross-task sequence, dependencies, approval gates, evidence requirements and recovery routing; references focused skills and shared contracts. |
| Skill | One independently useful task: when to use it, explicit inputs, prerequisites, procedure, available tools, output evidence and failure handling. |
| Tool | Executable operations and machine-checkable enforcement, with explicit arguments and results. Project-specific tools may remain project-owned. |

Use one canonical definition for each shared contract or rule. A workflow composes
skills by referencing their task contracts; it does not copy their operating
instructions. A skill references workflow gates when applicable without reproducing
the whole workflow. A standalone task invocation does not bypass applicable gates
or acquire authority for later actions. No workflow engine is required.

Split by coherent responsibility, not by command count. Status, ensure, stop and
login registration share server ownership rules and belong in one server skill.
Do not create a separate skill for each CLI verb. A tool or Markdown file alone
does not establish a callable, installed or successfully executed capability.

## First pilot: playground lifecycle

Extract the existing simulator guidance into two focused skills:

- `simulator-server`: resolve and verify the bound runtime; inspect health; reuse
  and open it; handle explicitly scoped start/stop and login-service operations.
- `simulator-page`: register, verify, open, update or deliberately remove one
  project-built page, preserving source/build identity and healthy sibling pages.
  It consumes a healthy runtime established through the server skill.

The page task takes the project identity, documented build output, page ID and
requested operation. Project-specific source builds use that project's runtime
and commands. Page implementation, parameter math, experiment purpose, design
choices and acceptance remain external. Pages are registered built apps, not
independently managed server processes.

Reuse the current lifecycle controller and registration interface. Inspect update
and removal support before promising commands: today updates are explicit local
registry edits/re-registration, not a complete page-management CLI. Missing safe
operations must be reported and scoped separately, not hidden behind invented
interfaces. No live registry mutation is required to prove the documentation split.

Keep `workbench-flow` as a thin project/task router referencing the recipes and
focused skills. Retain the existing runtime binding, ownership/conflict checks,
authorization boundaries and source/asset validation. Do not reinstall plugins,
change the running service or relocate assets as part of extraction.

## Composition and acceptance

Each skill must be independently invocable with explicit project/runtime inputs
and return a bounded result another task can consume without reconstructing chat:
operation, selected identities, actual outcome, evidence locations and unresolved
prerequisites. Reuse existing bindings and receipt contracts; do not invent a
parallel state store or require new schemas without demonstrated need.

For the pilot, verify discovery/packaging and local references; exercise safe
success and failure paths using generic fixtures. Keep source/package checks,
installed-skill invocation, live server reuse and actual page behavior as separate
acceptance claims. Record which were performed. Existing Laifen measurements,
export parity and roadmap milestone 1 remain separate work.

After the pilot, consider focused sticker tasks such as contract preparation,
bounded production, candidate review and deterministic composition. G0-G3 ordering
and advancement remain in the sticker workflow; preserve existing safeguards while
extracting procedures. Generic audit/composition/export tooling requires its own
inspection and verification before extraction. `design-reflection` already has a
bounded read-only outcome and does not need splitting now.

## Consequences

This refines decision 0002 without moving project authority or external provider
ownership. The source pilot packages five skills; the installed three-skill plugin
remains unchanged until separately scoped release and installation.
Project observations may motivate general workflow/tool improvements; preserve the
original observation and approval in its project. More skills are useful only if
they reduce duplicated procedure and support independently useful tasks.
