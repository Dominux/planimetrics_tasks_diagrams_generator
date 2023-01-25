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
        d = draw.Drawing(20, 20, origin="center")

        side_2_size = self._params.side_1_size * 2
        side_3_size = side_2_size - self._params.side_3_side_2_diff

        a, b, c = get_triangle_coordinates(
            self._params.side_1_size, side_2_size, side_3_size
        )

        p1 = Point(a.x, a.y, 0.05, "red")
        p2 = Point(b.x, b.y, 0.05, "red")
        p3 = Point(c.x, c.y, 0.05, "red")

        line1 = Line(a.x, a.y, b.x, b.y, 0.025, "red")
        line2 = Line(b.x, b.y, c.x, c.y, 0.025, "red")
        line3 = Line(c.x, c.y, a.x, a.y, 0.025, "red")

        points_names = list(self._params.triangle)

        point_a = draw.Text(points_names[0], fontSize=1, x=a.x, y=a.y)
        point_b = draw.Text(points_names[1], fontSize=1, x=b.x, y=b.y)
        point_c = draw.Text(points_names[2], fontSize=1, x=c.x, y=c.y)

        for el in (p1, p2, p3, line1, line2, line3, point_a, point_b, point_c):
            d.append(el)

        return d
