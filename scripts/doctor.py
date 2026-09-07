"""Read-only diagnostics for the pinned root Python environment."""

from importlib import metadata
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
CADGEN_VERSION = "0.5.0"


def environment_errors(version, prefix, cadgen_version, root=ROOT):
    errors = []
    if tuple(version[:2]) != (3, 12):
        errors.append("Python 3.12 is required")
    if Path(prefix).resolve() != (root / ".venv").resolve():
        errors.append("Interpreter must use the repository root .venv")
    if cadgen_version != CADGEN_VERSION:
        errors.append(f"cadgen=={CADGEN_VERSION} is required")
    return errors


def installed_version(name):
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        return None


def main():
    cadgen_version = installed_version("cadgen")
    errors = environment_errors(sys.version_info, sys.prefix, cadgen_version)
    print(json.dumps({
        "ok": not errors,
        "python": sys.version.split()[0],
        "executable": sys.executable,
        "environment": sys.prefix,
        "expected_environment": str(ROOT / ".venv"),
        "cadgen": cadgen_version,
        "toolchain_pins": (ROOT / ".tool-versions").read_text().splitlines(),
        "optional_capabilities": {
            "snapshot": {"playwright": installed_version("playwright"),
                         "browser_status": "not checked; actual snapshot verifies availability"},
            "mesh_and_dxf_builders": {"node": shutil.which("node"),
                                      "requirement": "Node.js >=20; version not checked"},
        },
        "errors": errors,
    }, indent=2))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
