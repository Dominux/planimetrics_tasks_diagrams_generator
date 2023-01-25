from dataclasses import dataclass
from numbers import Number

import drawSvg as draw

from who_cares.helpers import get_triangle_coordinates

from .base import MathTask
from who_cares.primitives import Point, Line


@dataclass
class TrianglePerimeterParams:
    side_1: str
    side_2: str
    triangle: str
    side_1_size: Number
    units_1: str
    side_3: str
    side_3_side_2_diff: Number


class TrianglePerimeterTask(MathTask):
    _prompt_template = """
        Сторона {side_1} треугольника {triangle} равна {side_1_size} {units_1}, 
        сторона {side_2} вдвое больше стороны {side_1}, 
        а сторона {side_3} на {side_3_side_2_diff} {units_1} меньше сторона {side_2}.
        Найдите периметр треугольника {triangle}.
    """

    def __init__(self, params: TrianglePerimeterParams, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._params = params

    @property
    def vector(self) -> draw.Drawing:
        d = draw.Drawing(10, 10, origin="center")

        side_2_size = self._params.side_1_size * 2
        side_3_size = side_2_size - self._params.side_3_side_2_diff

        a, b, c = get_triangle_coordinates(
            self._params.side_1_size, side_2_size, side_3_size
        )

        p1 = Point(a.x, a.y, 0.025, "red")
        p2 = Point(b.x, b.y, 0.025, "red")
        p3 = Point(c.x, c.y, 0.025, "red")

        line1 = Line(a.x, a.y, b.x, b.y, 0.025, "red")
        line2 = Line(b.x, b.y, c.x, c.y, 0.025, "red")
        line3 = Line(c.x, c.y, a.x, a.y, 0.025, "red")

        for el in (p1, p2, p3, line1, line2, line3):
            d.append(el)

        return d
