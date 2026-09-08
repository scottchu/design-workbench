# Independent plugin-install binding review

Status: **PASS for the narrow runtime-binding instruction candidate.** No material finding. Installation, cached artifact parity, real service reuse and private HTTPS preservation are separate root acceptance gates; this review did not execute them.

Reviewer: `/root/boundary_inventory`, independent of root's documentation/binding/package/install implementation. Sole write: this review. No live lifecycle, configuration, service, Tailscale, plugin-install or artifact-modification command was run.

## Candidate identity

Reviewed BRIEF.md, the complete updated local-server skill reference and SERVICE.md, their diff and the policy manifest. Git baseline: `57513d19014711424329a5e0d3e9c6f10689b47b` plus the declared documentation changes.

| Path | SHA-256 |
| --- | --- |
| `skills/workbench-flow/references/local-server.md` | `dd9e89dec67e53527e57752b9b8633416aa2e426370cb6c216eb72233b0db2f1` |
| `apps/simulator/SERVICE.md` | `a67e27fd5899c1d1191854f14eb808f46a8b017faed1f1d11914d219b66d8a2a` |
| `catalog/POLICY.sha256` | `c7726e22954a054ab93e87293baeb925066ef9b74acc7aa8a90142d8cdfffe1c` |
| Unchanged `scripts/simulator_service.py` | `64c3c56d2cf793a56f18db18a826095c763c7a3630d49b3991ad5d1a61dd2332` |

`git diff --exit-code -- scripts/simulator_service.py apps/simulator/src/lib/server/access.js apps/simulator/src/hooks.server.js apps/simulator/src/routes/health/+server.js` passed: controller and application ownership/origin/health code remain unchanged. `uv run python scripts/check_registry.py` passed: twelve capabilities, two recipes, current local references and policy hashes. No workflow or service ran through that check.

## Instruction walkthrough

1. **Fresh installed-plugin request to open existing Laifen:** read the cached skill's bundled SERVICE/registration documentation; resolve the optional user-local version-1 binding; require its canonical absolute runtime root, fixed local URL and root-derived instance. Use the bound original root's environment and unchanged lifecycle controller for status/ensure/open. The cache is the instruction source, not another service owner. After matching health, select the requested existing simulator registration. No build, reinstall, Tailscale change or competing runtime is implied by valid existing binding reuse.
2. **Missing binding:** the instructions require an explicitly selected durable runtime root before setup. Absence does not authorize adopting whichever process answers port 4179, silently treating the cache as the owner or replacing another checkout. Real status/health verification precedes writing a new binding. This may require resolving the missing root; an unselected runtime cannot be reported ready.
3. **Binding/root/instance/URL mismatch or foreign loaded job:** report a configuration error and preserve the binding/service. The unchanged controller still checks actual loaded arguments, working directory and environment, and refuses occupied-port adoption. A root-string hash alone does not authorize a process; status and owned-health checks remain required before open.
4. **Stopped but correctly owned service:** ensure may restart that same selected runtime under the existing lazy-open contract; login installation/reconfiguration and uninstall remain separately scoped. An installed plugin update never relocates it implicitly.

The runtime binding is user-local machine configuration, intentionally absent from distributed source. The controller does not silently read it; agent instructions select the root explicitly. This remains a small workflow binding rather than a second runtime controller. Existing model/source/artifact identities and sibling-unavailable simulator behavior are retained.

## Installation acceptance handoff

Root should freeze the actual binding, new package receipt/input manifest and installed cached identities; verify installed/enabled state and three discoverable skills, invoke the bound original controller and demonstrate same-process healthy reuse, then verify the existing private HTTPS route remains unchanged. Preserve prior binding/configuration if any conflict appears. Installation/state checks in this task do not prove a new conversation actually selected and executed the newly installed skills. A fresh-session invocation remains explicitly untested until directly observed.
