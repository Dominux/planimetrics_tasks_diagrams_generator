from dataclasses import dataclass
from numbers import Number

import drawSvg as draw

from math_tasks_generator.base import MathTask, MathTaskGenerator
from math_tasks_generator.helpers.functions import (
    get_random_letters,
    get_triangle_coordinates,
)
from math_tasks_generator.primitives.point import Point
from math_tasks_generator.types import Coords


@dataclass
class Task94Params:
    picture_number: int
    side_1: str
    side_2: str
    side_3: str
    side_4: str
    triangle_1: str
    triangle_2: str
    side_2_size: Number
    side_4_size: Number
    units: str


class Task94(MathTask[Task94Params]):
    _task_number = 94

    _prompt_template = """
    На рисунке {picture_number} {side_1} = {side_2}, ∠1 = ∠2.
    а) Докажите, что треугольники {triangle_1} и {triangle_2} равны;
    б) найдите {side_3} и {side_1}, если {side_2} = {side_2_size} {units}, {side_4} = {side_4_size} {units}
    """

    def __init__(self, params: Task94Params, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._params = params

    @property
    def vector(self) -> draw.Drawing:
        drawing = draw.Drawing(100, 100, origin="center")

        # setting center side size as an average of two others
        side_center_size = (self._params.side_2_size + self._params.side_4_size) / 2

        a, b, d = get_triangle_coordinates(
            self._params.side_2, self._params.side_4_size, side_center_size
        )
        c = Coords(-b.x, -b.y)

        p1 = Point(a.x, a.y, 0.05, "red")
        p2 = Point(b.x, b.y, 0.05, "red")
        p3 = Point(c.x, c.y, 0.05, "red")
        p4 = Point(d.x, d.y, 0.05, "red")

        for el in (p1, p2, p3, p4):
            drawing.append(el)

        return drawing


class Task94Generator(MathTaskGenerator[Task94Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        side_1 = f"{points[0]}{points[1]}"
        side_2 = f"{points[1]}{points[3]}"
        side_3 = f"{points[3]}{points[0]}"
        # side_4 = f"{points[3]}{points[0]}"
        side_center = f"{points[0]}{points[2]}"
