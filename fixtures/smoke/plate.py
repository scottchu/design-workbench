"""Generic parametric plate; generated output is deliberately ignored."""

from cadgen import build123d as bd
from cadgen import step

WIDTH_MM = 20.0
DEPTH_MM = 12.0
HEIGHT_MM = 6.0
HOLE_DIAMETER_MM = 4.0


def make_plate(width, depth, height, hole_diameter):
    plate = bd.Box(width, depth, height) - bd.Cylinder(hole_diameter / 2, height)
    plate.label = "smoke_plate"
    return plate


@step(out="../../.workbench/smoke/plate.step")
def plate():
    return make_plate(WIDTH_MM, DEPTH_MM, HEIGHT_MM, HOLE_DIAMETER_MM)


if __name__ == "__main__":
    plate()
