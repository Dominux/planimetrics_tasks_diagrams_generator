import random
from dataclasses import dataclass
from numbers import Number

from math_tasks_generator.helpers import get_random_letters, get_random_units
from math_tasks_generator.base import MathTask, MathTaskGenerator


@dataclass
class Task90Params:
    point_1: str
    point_2: str
    point_3: str
    side_1: str
    side_2: str
    triangle: str
    side_1_size: Number
    units: str
    side_3: str
    side_3_side_2_diff: Number


class Task90(MathTask[Task90Params]):
    _task_number = 90

    _prompt_template = """
        Сторона {side_1} треугольника {triangle} равна {side_1_size} {units}, 
        сторона {side_2} вдвое больше стороны {side_1}, 
        а сторона {side_3} на {side_3_side_2_diff} {units} меньше стороны {side_2}.
        Найдите периметр треугольника {triangle}.
    """

    _vector_template = """
        <defs>
        </defs>
        <circle cx="0" cy="0" r="0.05" fill="red" />
        <circle cx="7" cy="2" r="0.05" fill="red" />
        <circle cx="-1" cy="-12" r="0.05" fill="red" />
        <path d="M0,0 L7,2" stroke-width="0.025" stroke="red" />
        <path d="M7,2 L-1,-12" stroke-width="0.025" stroke="red" />
        <path d="M-1,-12 L0,0" stroke-width="0.025" stroke="red" />
        <text x="0.1" y="-0.2" font-size="1" dy="0em">{point_1}</text>
        <text x="7.1" y="2.1" font-size="1" dy="0em">{point_2}</text>
        <text x="-1.3" y="-12.2" font-size="1" dy="0em">{point_3}</text>
    """


class Task90Generator(MathTaskGenerator[Task90Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(3)

        side_1 = f"{points[0]}{points[1]}"
        side_2 = f"{points[1]}{points[2]}"
        side_3 = f"{points[2]}{points[0]}"

        triangle = "".join(points)

        side_1_size = random.randint(1, 20)
        side_3_side_2_diff = random.randint(1, side_1_size * 2 - 1)

        units = get_random_units()

        return Task90Params(
            point_1=points[0],
            point_2=points[1],
            point_3=points[2],
            side_1=side_1,
            side_2=side_2,
            side_3=side_3,
            triangle=triangle,
            side_1_size=side_1_size,
            side_3_side_2_diff=side_3_side_2_diff,
            units=units,
        )
