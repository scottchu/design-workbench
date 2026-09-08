# Managed local simulator with optional private access

User explicitly requested setting up the plugin's local server and an optional
selected Tailscale port that is not public. This supersedes the prior iteration's
no-service-setup boundary for this simulator only. Tailscale Serve provides private
tailnet access; Funnel is excluded. Existing routes, printer/slicer services,
authentication and access policies remain unchanged.

Workbench requires its own local runtime for simulation. Package intentional
simulator source and local lifecycle instructions; build with root npm tooling.
Use the actual adapter-node build with a macOS user LaunchAgent, fixed loopback
127.0.0.1:4179, identified health endpoint, owned start/reuse/stop, and lazy open.
Enable login persistence so the phone link works while this user is logged in.
Tailscale is optional; this host uses the free dedicated HTTPS port 8454.

Root owns HTTP origin policy, health endpoint, live service/Tailscale setup and
continuity. workbench_implementation owns lifecycle helper/tests/SERVICE.md.
sticker_migration owns source packaging, workflow skill and package tests.
Independent review follows stable implementations. Do not change external project
source or register/install the Codex plugin incidentally. Use existing PR 1.

Acceptance requires actual production build, local health, repeated ensure without
another process, owned stop/restart, private HTTPS list/asset/browser checks,
unchanged preexisting Tailscale configuration, no Funnel permission for8454,
package readback and independent review. No reboot, other-device or physical CAD
acceptance is claimed without direct evidence.
