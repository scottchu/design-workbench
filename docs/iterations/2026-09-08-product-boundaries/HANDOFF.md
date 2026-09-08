# Product and source boundaries

## Scope and authority

On 2026-09-08 the user approved the proposed documentation step after a read-only
comparison with `personal/compiler`: define Design Workbench's product in
why/how/what order, record intent-source/implementation/deliverable/runtime
boundaries, and give README, PROJECT_STATE and NEXT_AGENT distinct roles.

Agentic Compiler's vision and document-source architecture informed the
distinction between authored intent and derived evidence. Its docs-only operating
rule belongs to that project. Workbench retains its implementation sources and
does not claim a reproducible docs-to-product compiler.

## Result

- `docs/product.md` owns product purpose, approach, delivery scope and acceptance
  expectations. The product covers CAD, images and future design outcomes.
- `docs/architecture.md` owns source, implementation, build, deliverable, runtime
  and record responsibilities. These do not mandate new directories.
- README routes readers by question; PROJECT_STATE records current work;
  NEXT_AGENT points successors to the owning documents.

Only documentation changed. No runtime operation, packaging, plugin installation,
project asset change or local folder relocation is part of this work. Runtime
evidence remains in the [previous handoff](../2026-09-08-playground-refresh/HANDOFF.md).

## Validation and delivery

- `git diff --check`: passed.
- `uv run python scripts/check_registry.py`: passed, 12 capabilities, two mapped
  recipes, local references and policy hashes; no recipe executed.
- Inline `uv run python` link readback: all 44 local link targets in the six
  changed documents exist. The new README architecture anchor matches its heading.
- Reviewed the documentation against current packaging, decision 0003 and the
  previous runtime handoff: existing installation/runtime limits remain explicit.

These checks concern documentation consistency, not installed or runtime
acceptance. No software implementation changed; no software build was needed.

Next: review and integrate the documentation PR, then select the next bounded
implementation step from the roadmap. Runtime release layout and any later
physical source/runtime separation remain open.
