# Working on CAD Workbench

Read the README, relevant decision records and active iteration brief before material changes. Use repository state and evidence records as the handoff authority; do not infer implementation status from a roadmap.

## Scope

- This repository owns reusable software and generic developer fixtures. Actual designs, project requirements, release artifacts and physical observations remain in their project repositories.
- Preserve unrelated work. Do not migrate repositories, copy private assets, install/register plugins, deploy or operate printers as an incidental setup action.
- Prefer existing supported upstream interfaces. Keep adapters small; do not reproduce an entire viewer lifecycle or create speculative abstractions.
- Treat source plus explicit parameters as the geometry authority. Derived images, meshes and UI overlays are evidence/projections, never a competing model implementation.

## Environment

- Prefer asdf for development tools. Root `.tool-versions` pins Node.js, Bun and uv. The foundation deliberately uses uv-managed CPython 3.12.13 from `.python-version`; retain that scoped choice rather than installing a second Python base. Bun is available but npm remains the sole JavaScript workspace package manager. Do not change global toolchain configuration incidentally.
- Use Python 3.12, the root uv workspace and root `uv.lock`. Run Python tooling through `uv run` from the repository root.
- The root `.venv` is the only Python environment. Repair it with `uv sync --all-packages --all-groups`; never select a system or project-local fallback. If a subprocess needs an interpreter path, pass the absolute root `.venv/bin/python` path.
- Use the root npm workspace and root `package-lock.json`; run npm commands at the root. Future package-specific dependencies belong in their own workspace package manifests. Do not create nested installs or lockfiles.
- Keep generated artifacts, environments, caches and diagnostic scratch output ignored. Commit only intentional source, locks, documentation, tests and explicitly designated fixtures.
- For shell search, use `/opt/homebrew/bin/rg` explicitly. If it is unavailable, report that before choosing another search tool.

## Validation and delivery

- Run focused local checks that catch credible failures, including actual artifact readback for export changes. Do not substitute mocked process success or a screenshot for geometry evidence.
- Record exact commands, results, source/artifact identities and limitations. Distinguish CAD checks, written-artifact/slicer evidence and physical acceptance.
- Use delegation when it resolves a concrete scope or independence need. Keep one writer per namespace and bounded task ownership. Separate implementation from acceptance review for substantial changes; do not require a large role ceremony for routine software edits.
- Keep active iteration/handoff records current for material changes. Report blockers without presenting planned checks as completed.
- Develop intended trunk changes on a non-main branch and deliver through a pull request unless the user explicitly overrides that route. The initial local foundation does not authorize remote creation or push.
- No repository-hosted CI. Required validation runs locally; absence of CI does not waive it.
