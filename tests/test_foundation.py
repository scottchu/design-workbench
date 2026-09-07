"""Focused checks for failures the setup must reject without running CAD."""

import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from cad_smoke import EXPECTED_VOLUME, measurement_errors
from doctor import environment_errors


class FoundationTests(unittest.TestCase):
    def test_environment_rejects_wrong_python_package_and_environment(self):
        self.assertEqual(len(environment_errors((3, 11), ROOT, "0.4.0")), 3)
        self.assertEqual(environment_errors((3, 12), ROOT / ".venv", "0.5.0"), [])

    def test_missing_hole_and_wrong_scale_fail(self):
        self.assertTrue(measurement_errors(True, 1, (20, 12, 6), 20 * 12 * 6))
        self.assertTrue(measurement_errors(True, 1, (200, 120, 60), EXPECTED_VOLUME))

    def test_invalid_empty_and_multiple_solids_fail(self):
        for valid, count in ((False, 1), (True, 0), (True, 2)):
            self.assertTrue(measurement_errors(valid, count, (20, 12, 6), EXPECTED_VOLUME))

    def test_nonfinite_measurements_fail(self):
        for value in (math.nan, math.inf, -math.inf):
            self.assertTrue(measurement_errors(True, 1, (value, 12, 6), EXPECTED_VOLUME))
            self.assertTrue(measurement_errors(True, 1, (20, 12, 6), value))

    def test_expected_geometry_passes(self):
        self.assertEqual(measurement_errors(True, 1, (20, 12, 6), EXPECTED_VOLUME), [])


if __name__ == "__main__":
    unittest.main()
