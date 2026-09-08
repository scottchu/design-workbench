# Preserved CAD Viewer service source

`cad-viewer-service/` is a byte-identical extraction from design-projects revision `71d661c14098860b7a374e13043fb084994be8a0`. Its README, design and validation files are historical records of that implementation, not validation performed by this move. See the extraction manifest in the current workflow-ownership iteration for every source and destination hash.

This legacy service has an existing installed copy and depends on canonical design-projects `.venv` and a bundled Node runtime. Its embedded historical paths and install manifest are intentionally unchanged. Moving source does not move, reinstall, start, restart or establish ownership of the running service. Do not run its installer or runtime-refresh tests during repository separation. No new persistent viewer is introduced by Workbench. Prefer supported upstream interfaces for future integrations; runtime decoupling requires a separate scoped change and verification.
