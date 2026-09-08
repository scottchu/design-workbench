# Local simulator browser acceptance

Root performed actual Chrome CUA interactions on 2026-09-07 at
http://127.0.0.1:4179/simulators/laifen-customizer. Source and six built asset
identities are in SIMULATOR_IMPLEMENTATION.md; the source remains external and
unchanged. No printer, slicer, Tailscale or existing-service operation occurred.

## Observed interaction

The initial real OpenSCAD WASM compilation completed with the cutaway preview,
inside height 213 mm, outside height 219 mm and an enabled current STL link.
Changing inside height to 180 retained the previous preview with an explicit
Previous generation label, displayed outside height 186 mm and disabled download.
Generate then completed, displayed inside height 180 mm and re-enabled a new
current blob download. Both downloads were clicked through the actual UI, then
read from disk. Screenshots were visually inspected; generated geometry and its
height annotation were visible. This is a host/browser integration check, not
independent validation of all the source model's design relationships.

## Written artifact readback

Run from Workbench root: `uv run python .workbench/simulator-readback.py`.
The ignored script parses every ASCII STL vertex, checks finite coordinates and
triangle grouping, computes bounds, and compares dimensions with a 0.000001 mm
tolerance. Its JSON receipt is `.workbench/simulator-browser/download-readback.json`.
The first exact-float equality assertion failed on the 180 mm candidate's normal
floating point residual; explicit tolerance readback passed. Both files contain
39,904 triangles and minimum coordinate [-19.5, -19.5, 0].

| Browser input | Download in /Users/scottchu/Downloads | Bytes | SHA-256 | Measured extent mm |
| --- | --- | --- | --- | --- |
| Inside height 213 | container-assembled-e79086b77747.stl | 12160971 | b1b9db18e21cafed5237afb90e57831b72246c6ac2e4b4c88f736738fd0cf169 | 39, 39, 219 |
| Inside height 180 | container-assembled-2e668268029b.stl | 12514124 | dadfcae7df196ddd2722c3d4a44f6bcf5c4003f81725fa4f76d617a28be7b8bd | 39, 39, 185.99999999744844 |

This verifies actual written dimensions changed by the expected 33 mm while
outside diameter stayed 39 mm. It does not establish watertightness, wall/thread
correctness, slicer readiness or physical fit. Private STL downloads stay outside
this repository. The separate roadmap milestone 1 parameter/build-identity
contract remains unfulfilled by this single input check.

## Development process and final repair

V3's initial production build overlapped the dev process and regenerated shared
`.svelte-kit` output, followed by a Vite error overlay. That run was discarded.
Root stopped the verified task-owned loopback process and restarted it before the
successful two-download sequence above. Further final check/build ran only while
the dev process was stopped. This ordering is documented in NEXT_AGENT.md.

R2 isolated stale registrations so one project's source change cannot disable the
others. V3 reran check/build and all eight tests with the server stopped. After
restart, root observed a new successful 213 mm compilation, then navigated the
launcher: the registered Laifen card and working selected route were present,
with no error overlay. Final task-owned dev process: tool session 42116,
`npm run dev:simulator`, bound 127.0.0.1:4179. The browser launcher tab is retained
as a user deliverable. No background service or remote access is installed.
