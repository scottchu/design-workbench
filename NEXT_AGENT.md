# Resume CAD Workbench

1. Read `AGENTS.md`, `README.md`, `PROJECT_STATE.md`, decision `docs/decisions/0001-foundation.md`, and the active foundation iteration's `HANDOFF.md`, `VALIDATION.md` and `REVIEW.md`.
2. Inspect `git status --short --branch` and `git log -1` before editing. The foundation branch tracks `origin/setup/foundation` in private `scottchu/CAD-workbench`. This is currently GitHub's default branch; no `main` branch or pull-request merge exists. Verify local/remote revisions before later delivery rather than assuming subsequent changes were pushed.
3. Use asdf-selected tools and the root uv environment. Reproduce the documented doctor/smoke commands when changes or uncertainty warrant it; do not reinstall unrelated global tools or rerun all tests merely to reread documentation.
4. Keep design source and physical observations in their project repositories. Only generic fixtures belong in this software repository.
5. Complete any unresolved foundation review finding before UI work. Otherwise open a new bounded iteration for the first real Laifen parameter-edit/regenerate/display/export path described in `docs/roadmap.md`. Inspect the current Laifen source before selecting it; historical worktree locations are discovery hints, not an active baseline.

Do not infer working editor, preparation, printer-control or agent-plugin capabilities from the roadmap. All are future work. Adding a remote, migration, deployment and printer operation each needs an appropriate task scope.
