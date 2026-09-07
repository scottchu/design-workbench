# External project binding

A binding is project-owned configuration, not a second copy of project state. Store it in the consuming repository (for example `workflow-binding.json`). Record:

- Workbench repository URL, delivery Git revision and policy manifest path/SHA-256. A candidate may use the manifest alone until delivery assigns the exact commit; never label an unresolved revision installed or released.
- Workflow IDs and the canonical catalog/recipe paths.
- External repository root, exact project revision, project root and source entrypoints; hashes for dirty source and declared inputs. A moving branch is discovery only.
- Each command as an executable/argument array with an explicit working directory, interpreter/runtime version and provider source identity. Resolve paths against the selected external checkout, verify scope and availability, and do not blindly execute arbitrary JSON shell text.
- Optional workshop inventory path in the external project repository, or explicit null. Availability is not process evidence.
- Project-owned current-state/iteration and evidence paths. Read these at execution time; never duplicate their changing status in this catalog.

Runtime dependencies remain with their owner. Workbench's root uv environment is for Workbench tools; it is not a fallback Python for external project builds. Skills in `skills/` are source packages, not installed plugins. Each consuming agent must explicitly resolve the bound skill path/version using its supported discovery mechanism.

For stickers, bind `contract`, `candidate`, and `review-lint` plus source authority, masters and fresh evidence paths. For CAD, bind the real generation, actual geometry validation, written export/readback and optional viewer/slicer commands. A missing command is an unresolved capability, never permission to invent success. Do not assume Jaelin npm commands or STEP export apply to every backend.
