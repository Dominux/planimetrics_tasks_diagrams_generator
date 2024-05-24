from dataclasses import dataclass
import random

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import (
    get_random_letters,
    get_random_units,
)


@dataclass
class Task95Params(Params):
    picture_number: int
    point_1: str
    point_2: str
    point_3: str
    point_4: str
    side_1: str
    side_2: str
    side_3: str
    side_4: str
    triangle_1: str
    triangle_2: str
    side_3_size: float
    side_4_size: float
    units: str


class Task95(MathTask[Task95Params]):
    _task_number = 95

    _prompt_template = """
        На рисунке {picture_number} {side_2} = {side_4}, ∠1 = ∠2.
        а) Докажите, что треугольники {triangle_1} и {triangle_2} равны;
        б) найдите {side_1} и {side_2}, если {side_4} = {side_4_size} {units}, {side_3} = {side_3_size} {units}
    """

    _figure_template = """
        [
            {{
                "type":"triangle",
                "name":"{triangle_1}"
            }},
            {{
                "type":"triangle",
                "name":"{triangle_2}"
            }},
            {{
                "type":"line",
                "name":"{side_1}"
            }},
            {{
                "type":"line",
                "name":"{side_2}"
            }},
            {{
                "type":"line",
                "name":"{side_3}",
                "length":"{side_3_size} {units}"
            }},
            {{
                "type":"line",
                "name":"{side_4}",
                "length":"{side_4_size} {units}"
            }},
            {{
                "type":"angle",
                "name":"1"
            }},
            {{
                "type":"angle",
                "name":"2"
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{triangle_1}",
                    "{triangle_2}"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{side_2}",
                    "{side_4}"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "1",
                    "2"
                ]
            }}
        ]
    """


class Task95Generator(MathTaskGenerator[Task95Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        side_1 = f"{points[0]}{points[1]}"
        side_2 = f"{points[1]}{points[2]}"
        side_3 = f"{points[2]}{points[3]}"
        side_4 = f"{points[3]}{points[0]}"

        picture_number = random.randint(1, 1500)

        triangle_1 = "".join((points[0], points[1], points[2]))
        triangle_2 = "".join((points[0], points[2], points[3]))

        side_3_size = random.randint(1, 20)
        side_4_size = random.randint(1, 20)

        units = get_random_units()

        return Task95Params(
            picture_number=picture_number,
            point_1=points[0],
            point_2=points[1],
            point_3=points[2],
            point_4=points[3],
            side_1=side_1,
            side_2=side_2,
            side_3=side_3,
            side_4=side_4,
            triangle_1=triangle_1,
            triangle_2=triangle_2,
            side_3_size=side_3_size,
            side_4_size=side_4_size,
            units=units,
        )


class Task95Unit(MathTaskUnit):
    _math_task = Task95
    _math_task_generator = Task95Generator
