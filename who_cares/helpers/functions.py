import math
from numbers import Number
from typing import Tuple

from who_cares.types import Coords


def get_triangle_coordinates(
    size_ab: Number,
    size_bc: Number,
    size_ac: Number,
) -> Tuple[Coords, Coords, Coords]:
    a = Coords(0, 0)
    b = Coords(size_ab, 0)

    cx = (size_ac**2 - size_bc**2 + size_ab**2) / (2 * size_ab)
    cy = math.sqrt(size_ac**2 - cx**2)
    c = Coords(cx, cy)

    return a, b, c
