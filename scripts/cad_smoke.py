"""Build a generic cadgen fixture and independently inspect its written STEP."""

import argparse
from datetime import datetime, timezone
import hashlib
from importlib import metadata
import json
import math
import os
from pathlib import Path
import subprocess
import sys

from doctor import environment_errors

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures/smoke/plate.py"
OUTPUT = ROOT / ".workbench/smoke"
EXPECTED_DIMENSIONS = (20.0, 12.0, 6.0)
EXPECTED_VOLUME = 20 * 12 * 6 - math.pi * 2**2 * 6


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def measurement_errors(valid, solid_count, dimensions, volume):
    errors = []
    if not valid:
        errors.append("Written STEP geometry is invalid")
    if solid_count != 1:
        errors.append(f"Expected one solid, received {solid_count}")
    if len(dimensions) != 3 or any(
        not math.isfinite(actual) or abs(actual - expected) > 0.01
        for actual, expected in zip(dimensions, EXPECTED_DIMENSIONS)
    ):
        errors.append(f"Unexpected bounding dimensions: {dimensions}")
    if not math.isfinite(volume) or abs(volume - EXPECTED_VOLUME) > 0.1:
        errors.append(f"Unexpected material volume: {volume}")
    return errors


def run(command, env):
    result = subprocess.run(command, cwd=ROOT, env=env, capture_output=True,
                            text=True, timeout=180)
    for stream in (result.stdout, result.stderr):
        if stream:
            print(stream, file=sys.stderr, end="" if stream.endswith("\n") else "\n")
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}): {command}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", action="store_true",
                        help="Require a real snapshot of the generated STEP")
    args = parser.parse_args()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    receipt = {
        "schema_version": 1,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "ok": False,
        "fixture": {"path": str(FIXTURE), "sha256": sha256(FIXTURE)},
        "acceptance": {"cad_readback": "not checked", "snapshot": "not requested",
                       "slicer": "not checked", "physical": "not checked"},
    }
    try:
        version = metadata.version("cadgen")
        receipt["runtime"] = {"python": sys.version.split()[0], "cadgen": version,
                              "build123d": metadata.version("build123d"),
                              "cadquery_ocp": metadata.version("cadquery-ocp")}
        errors = environment_errors(sys.version_info, sys.prefix, version)
        if errors:
            raise RuntimeError("; ".join(errors))
        env = dict(os.environ, CADGEN_DAEMON="0", CADGEN_JOBS="2",
                   CADGEN_VALIDATE_WORKERS="1", CADGEN_CACHE_DIR=str(ROOT / ".workbench/cache"))
        command = [sys.executable, str(FIXTURE), "--force", "--json"]
        receipt["generation_command"] = command
        receipt["execution_environment"] = {key: env[key] for key in (
            "CADGEN_DAEMON", "CADGEN_JOBS", "CADGEN_VALIDATE_WORKERS", "CADGEN_CACHE_DIR")}
        run(command, env)
        artifact = OUTPUT / "plate.step"
        if not artifact.is_file() or not artifact.stat().st_size:
            raise RuntimeError("Generation did not produce a non-empty STEP")
        # Import the bytes with the CAD kernel, independently of cadgen's cached tree.
        from build123d import import_step
        shape = import_step(str(artifact))
        size = shape.bounding_box().size
        dimensions = [size.X, size.Y, size.Z]
        solids = shape.solids()
        valid = shape.is_valid and all(solid.is_valid for solid in solids)
        volume = shape.volume
        receipt["step"] = {"path": str(artifact), "sha256": sha256(artifact)}
        receipt["measurements"] = {"valid": valid, "solid_count": len(solids),
                                   "dimensions_mm": dimensions, "volume_mm3": volume,
                                   "expected_volume_mm3": EXPECTED_VOLUME}
        errors = measurement_errors(valid, len(solids), dimensions, volume)
        if errors:
            raise RuntimeError("; ".join(errors))
        receipt["acceptance"]["cad_readback"] = "passed"
        if args.snapshot:
            receipt["acceptance"]["snapshot"] = "failed"
            snapshot = OUTPUT / "plate.png"
            command = [sys.executable, "-m", "cadgen.cli", "step", "snapshot",
                       str(artifact), str(snapshot), "--json"]
            receipt["snapshot_command"] = command
            run(command, env)
            if not snapshot.is_file() or not snapshot.stat().st_size:
                raise RuntimeError("Snapshot command produced no image")
            receipt["snapshot"] = {"path": str(snapshot), "sha256": sha256(snapshot)}
            receipt["acceptance"]["snapshot"] = "generated; visual review still required"
        receipt["ok"] = True
    except Exception as exc:
        receipt["error"] = f"{type(exc).__name__}: {exc}"
    receipt_path = OUTPUT / "receipt.json"
    receipt["receipt_path"] = str(receipt_path)
    text = json.dumps(receipt, indent=2)
    receipt_path.write_text(text + "\n")
    print(text)
    return int(not receipt["ok"])


if __name__ == "__main__":
    raise SystemExit(main())
