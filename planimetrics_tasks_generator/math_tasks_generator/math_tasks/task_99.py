from dataclasses import dataclass

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task99Params(Params):
    point_A: str
    point_B: str
    point_C: str
    point_D: str
    point_E: str


class Task99(MathTask[Task99Params]):
    _task_number = 99

    _prompt_template = """
        На сторонах угла {point_C}{point_A}{point_D} отмечены точки {point_B} и {point_E} так,
        что точка {point_B} лежит на отрезке {point_A}{point_C}, а точка {point_E} — на
        отрезке {point_A}{point_D}, причем {point_A}{point_C} = {point_A}{point_D} и
        {point_A}{point_B} = {point_A}{point_E}. Докажите, что 
        ∠{point_C}{point_B}{point_D} = ∠{point_D}{point_E}{point_C}
    """

    _figure_template = """
        [
            {{
                "type":"line",
                "name":"{point_A}{point_C}"
            }},
            {{
                "type":"line",
                "name":"{point_A}{point_D}"
            }},
            {{
                "type":"line",
                "name":"{point_A}{point_B}"
            }},
            {{
                "type":"line",
                "name":"{point_A}{point_E}"
            }},
            {{
                "type":"angle",
                "name":"{point_C}{point_A}{point_D}",
            }},
            {{
                "type":"angle",
                "name":"{point_C}{point_B}{point_D}",
            }},
            {{
                "type":"angle",
                "name":"{point_D}{point_E}{point_C}",
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{point_A}{point_C}",
                    "{point_A}{point_D}"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{point_A}{point_B}",
                    "{point_A}{point_E}"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{point_C}{point_B}{point_D}",
                    "{point_D}{point_E}{point_C}"
                ]
            }},
        ]
    """


class Task99Generator(MathTaskGenerator[Task99Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(5)

        point_A = points[0]
        point_B = points[1]
        point_C = points[2]
        point_D = points[3]
        point_E = points[4]

        return Task99Params(
            point_A=point_A,
            point_B=point_B,
            point_C=point_C,
            point_D=point_D,
            point_E=point_E,
        )


class Task99Unit(MathTaskUnit):
    _math_task = Task99
    _math_task_generator = Task99Generator
