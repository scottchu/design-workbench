# Start here: Design Workbench

Read [AGENTS.md](AGENTS.md), [README.md](README.md),
[PROJECT_STATE.md](PROJECT_STATE.md) and its linked active handoff. Use current
repository evidence; do not reconstruct old chat or repeat completed migration
checks without a concrete discrepancy. Communicate in Chinese.

For product questions, read [product intent](docs/product.md) and the linked
architecture boundaries. Status and handoff records do not redefine that intent.

The GitHub repository is `scottchu/design-workbench`. Local folder names remain
unchanged by explicit user instruction. Check Git state before new work; develop
on a non-main branch and deliver through a PR.

Runtime operations use the existing binding at
`~/.config/cad-workbench/runtime.json`, selecting
`/Users/scottchu/Projects/personal/CAD-workbench` and that root's absolute
`.venv/bin/python`. The separate `CAD-workbench-next` worktree is for development,
not a replacement runtime. Do not rename either root or rebind the service.

PR4 source is merged and the running host has been refreshed to apps/playground.
The installed plugin was explicitly excluded from refresh: do not infer that the
five source skills are installed. Read current acceptance and the next bounded
step in PROJECT_STATE; this file deliberately does not maintain a second task list.
