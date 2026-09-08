# Roadmap compilation handoff

## Authorized PR delivery

After the user authorized proceeding, pushed `codex/composable-skills` and opened
[PR4](https://github.com/scottchu/design-workbench/pull/4) against main. Original
pushed tip was `9f15fee`; the follow-up documentation commit records this delivery.
Before push, actual package readback and all 70 current source/output identities
matched validated candidate 2; `scripts/check_registry.py` and diff whitespace
checks passed. Historical local tests and independent reviews remain applicable.
The PR is open, not merged. No plugin installation or live runtime operation ran.

## Subsequent repository rename

User authorized `design-workbench` and explicitly required local folder names to
remain unchanged. Executed `gh repo rename design-workbench --repo
scottchu/CAD-workbench --yes` and `git remote set-url origin
git@github.com:scottchu/design-workbench.git` from the development worktree.
GitHub readback confirms `scottchu/design-workbench`, unchanged repository ID
`1359625520` / node ID `R_kgDOUQo9MA`, private visibility and default branch main.
`git ls-remote origin refs/heads/main` remains
`d92816a47f71de5adc8130f468f07500f1079318` before/after. `git worktree list` confirms
both original directory paths unchanged. Runtime binding SHA-256 remains
`ebc0145e394acad27f76e5bde868e179c07ff5307adfeb28a66132e4b3e8afec` before/after.
No service operation, plugin rename/install, source push or PR creation occurred.
Existing technical identifiers and historical names remain compatibility context;
broader branding/package changes are separate work.

## Roadmap source handoff

Base: `6466d15`, local branch `codex/composable-skills`, development root
`/Users/scottchu/Projects/personal/CAD-workbench-next`.

The roadmap adds R1-R5 for accepting the focused playground skills, a narrow owned
MCP, consistent-image production, evidence-backed cross-domain contracts and
verified reusable tools. It preserves original CAD milestone IDs 0-6 and their
requirements. Each layer uses why -> how -> what. Architecture distinguishes these
future changes from the current implementation.

The dependency order keeps the bounded MCP slice from growing into a platform
prerequisite: return to actual Laifen milestone 1 and a separate image pilot, then
generalize from their evidence. Sticker-specific output rules remain reusable;
project design requirements and approval remain project-owned.

The earlier skill extraction at 6466d15 remains locally validated and is now in PR4.
Installed plugin still has three skills; no MCP, consistent-image skill or generic
image validator was implemented here. Runtime remains in canonical main at
`/Users/scottchu/Projects/personal/CAD-workbench` with its existing binding.

Next: review/merge PR4. Installation/live pilot acceptance is separate; the later
R2 implementation begins by defining a bounded read-only MCP contract. Do not
execute the whole roadmap as implicit authority from this documentation request.

See [VALIDATION.md](VALIDATION.md) for original requirement/heading preservation
and local documentation checks, and [REVIEW.md](REVIEW.md) for independent review.
Review clarified that the first R2 read-only checkpoint is sufficient before
returning to CAD milestone 1; completed mutation tooling is not a prerequisite.
