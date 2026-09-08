# Composable skills: incremental pilot

Step 2 authorized after the user reviewed step 1 and replied "ok": extract
simulator-server and simulator-page, route workbench-flow and the CAD recipe to
them, refresh policy identities and verify source packaging. Reuse executable
interfaces; do not add a new lifecycle API. An independent reviewer owns REVIEW.md
and isolated generic registration fixtures only; root owns implementation and
other records. Validate skill structure, registry policy hashes, package readback
and existing focused package/registry checks. Forward-test page operations on an
isolated registry, not the installed runtime. No installation or live service,
private registry, project assets, network or printer changes are authorized here.

## Step 1 scope and acceptance

User direction: proceed step by step with the proposed workflow/skill/tool
separation. Communication is in Chinese; repository documentation retains its
existing English convention.

This bounded step records decision 0003, links it from architecture, and updates
continuity. Skill extraction, tool implementation, packaging/install changes,
project changes and service operations are outside this step.

Acceptance: the decision distinguishes ownership and composition, defines the
playground pilot without claiming implementation, preserves existing safeguards,
and names the next bounded action. Check diff whitespace and changed document
links locally. No runtime or geometry test is needed for this documentation step.

Develop in the existing separate development worktree on
`codex/composable-skills`, based on `d92816a`. Canonical main remains the runtime
owner. Delivery follows the repository PR route; no remote push is part of this
local step.
