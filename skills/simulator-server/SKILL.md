---
name: simulator-server
description: Resolve, inspect and manage the owned Workbench simulator server, including reuse, opening the host and explicitly requested service lifecycle changes. Use for server health or lifecycle tasks; use simulator-page for a particular project page.
---

# Simulator Server

Manage one owned Workbench runtime. Read [runtime resolution](references/runtime.md)
before any operation and the linked service contract for the selected command.
Use the bound runtime's working directory and absolute root `.venv/bin/python`;
the installed skill/package location is not necessarily the runtime root.

Inputs: requested operation and the existing local runtime binding, or an explicitly
selected durable root if no binding exists. A project is not required for server
status. Missing or conflicting identity is a configuration failure, not permission
to adopt a listener, replace the binding or install a second service.

Choose only the requested scope:

- Status/diagnosis: inspect binding, controller status and identified health without
  ensuring, starting, building or installing anything. Use the existing absolute
  root interpreter; if it is missing, report that prerequisite without syncing the
  environment. The controller may write its local lifecycle lock; this is
  read-only with respect to service configuration and lifecycle, not zero disk writes.
- Ensure/open: reuse the owned healthy service or start its existing prepared
  build through the controller. `open` opens the host catalog. Missing prerequisites
  remain explicit; follow the runtime reference for in-scope setup.
- Stop or login install/uninstall: use the service contract for the explicitly
  requested operation. Stop and uninstall have different persistence effects.
  Relocation and private-access configuration are separate explicit tasks.

Server health does not establish availability of a particular page. For a selected
project simulator, hand the verified runtime root, instance, local URL and registry
path to [simulator-page](../simulator-page/SKILL.md). That task owns page selection
and asset checks; do not register pages as incidental server setup.

Return the requested operation, resolved root/instance, actual controller command
and result, observed health and registry path where available, and any unresolved
prerequisite. Distinguish a reused service from a newly started one only when
observed. Record a receipt in the requesting project's records when recording is
in scope; standalone diagnosis can return this result without a project write.
No server result implies browser, CAD, export, phone or physical acceptance.
