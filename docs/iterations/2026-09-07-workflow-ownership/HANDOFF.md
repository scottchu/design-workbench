# Workflow ownership handoff

Status: migration implementation and independent preservation/acceptance review complete. Plugin packaging and local simulator passed independent validation/review and root browser/artifact acceptance; PR delivery in progress.

## Source checkout relocation

After the final source-task write release and successful frozen-input verification, `/Users/scottchu/.codex/worktrees/0868/design-projects` disappeared externally. No agent in this task removed it; the cause is unverified. Its branch and all required commits remained available in the common Git repository.

Root ran `git -C /Users/scottchu/Projects/personal/design-projects worktree add /Users/scottchu/Projects/personal/design-projects-workflow-separation codex/separate-sticker-repository`. At relocation, the replacement was clean at the same `71d661c14098860b7a374e13043fb084994be8a0`. Project tree `0d068f4d20cd8417756fbe5c16b41110ccd376ba` and sticker skill tree `829d718e59fc5bb5719281b47a46e653dbdc1bd0` match the frozen handoff. All 43 entries of the I1 input manifest verified after only substituting the checkout prefix. This is the active source checkout for subsequent work; old paths in historical receipts identify their original observation.

The canonical design checkout remains dirty and untouched. The original live-pilot worktree at `3fc3` remains present. Draft library and sticker destination remain at their original paths.

## Environment

Workbench `uv sync --locked --all-packages --all-groups` succeeded using CPython 3.12.13, creating only this checkout's root `.venv` and installing 61 locked packages. No lock or global toolchain changes. No CAD smoke rerun, printer or service operation.

## Accepted migration

V1 restored and compared the original sticker WIP, including tracked patch, 189 archive payloads and 189 AppleDouble sidecars. V2 and R1 accepted Workbench provider `36f41715ee2257c0f2e41e40329216e3d2b2747f`, source `b8b0f5d9e38a2b2d1f1f6b07b9ec6f9f283c8565`, and sticker `33fcac4f56ccb0dbc59f54c7882f9c16acfd58bf`. See PRESERVATION_VALIDATION.md, VALIDATION.md and REVIEW.md for exact commands, hashes, preserved history and limitations.

848 sticker project files and 2504 retained source/project records match frozen originals. 884 migrated paths were retired after preservation. Shared authority now resides in Workbench; both project bindings pin provider 36f4171. Workbench tests 9 pass, sticker tests 14 pass, source tests 10 pass plus one preexisting Laifen missing VALIDATION.md failure. No project evidence was fabricated to hide it. Git-mode preservation passed; full POSIX mode preservation is not claimed.

The empty workflow-library remote and local draft remain superseded and intact. Sticker history, divergent documentation branch, live-pilot base, exact recovery archive/patch and historical tag remain retained. No historical release is moved.

## Plugin and local simulator

The user's final scope in PLUGIN_ADDENDUM.md supersedes the earlier shared-backend proposal: Workbench owns a workflow plugin and one loopback SvelteKit simulator host. Orca retains printer/slicer MCP/API/dashboard/widgets. Text-to-CAD and U1 remain separately maintained providers; none is cloned or installed here.

PLUGIN_IMPLEMENTATION.md identifies the generated ignored package and its 44 source files. SIMULATOR_IMPLEMENTATION.md identifies the actual external Laifen six-file build and source hash. Runtime registry `.workbench/simulators.json` is explicit ignored local state. Current local URL: http://127.0.0.1:4179/simulators/laifen-customizer. Root owns the task-specific dev process. Existing services/Tailscale routes are untouched.

## Delivery

Review branches and PR delivery remain pending; no merge authorized. PLUGIN_SIMULATOR_VALIDATION.md and PLUGIN_SIMULATOR_REVIEW.md now pass. R2 stale-entry isolation repair passed eight tests, zero-error Svelte check and production build. ROOT_BROWSER_ACCEPTANCE.md records actual generation, parameter-change, download and measured STL extent checks. The final root-owned dev session is 42116; stop it before regenerating SvelteKit output. New plugin/simulator acceptance is separate from migration acceptance at provider36. Do not silently upgrade consumer bindings or claim all simulators have been registered.
