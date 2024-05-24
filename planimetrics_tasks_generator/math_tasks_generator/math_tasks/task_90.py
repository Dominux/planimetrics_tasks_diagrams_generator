import random
from dataclasses import dataclass

from math_tasks_generator.helpers import (
    get_random_letters,
    get_random_units,
)
from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)


@dataclass
class Task90Params(Params):
    point_1: str
    point_2: str
    point_3: str
    side_1: str
    side_2: str
    triangle: str
    side_1_size: float
    units: str
    side_3: str
    side_3_side_2_diff: float


class Task90(MathTask[Task90Params]):
    _task_number = 90

    _prompt_template = """
        Сторона {side_1} треугольника {triangle} равна {side_1_size} {units}, 
        сторона {side_2} вдвое больше стороны {side_1}, 
        а сторона {side_3} на {side_3_side_2_diff} {units} меньше стороны {side_2}.
        Найдите периметр треугольника {triangle}.
    """

    _figure_template = """
        [
            {{
                "type":"triangle",
                "name":"{triangle}"
            }},
            {{
                "type":"line",
                "name":"{side_1}",
                "length":"{side_1_size} {units}"
            }},
            {{
                "type":"relation",
                "rel_type":"difference",
                "difference":"2x",
                "objects":[
                    "{side_2}",
                    "{side_1}"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"difference",
                "difference":"-{side_3_side_2_diff} {units}",
                "objects":[
                    "{side_3}",
                    "{side_2}"
                ]
            }}
        ]
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


class Task90Unit(MathTaskUnit):
    _math_task = Task90
    _math_task_generator = Task90Generator
