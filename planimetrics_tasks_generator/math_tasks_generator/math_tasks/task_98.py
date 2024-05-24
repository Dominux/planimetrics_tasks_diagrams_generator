from dataclasses import dataclass

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task98Params(Params):
    point_A: str
    point_B: str
    point_C: str
    point_P: str
    triangle_ABC: str
    triangle_A1B1C1: str
    triangle_BPC: str
    triangle_B1P1C1: str


class Task98(MathTask[Task98Params]):
    _task_number = 98

    _prompt_template = """
        В треугольниках {triangle_ABC} и {triangle_A1B1C1}
        {point_A}{point_B} = {point_A}₁{point_B}₁, {point_A}{point_C} = {point_A}₁{point_C}₁,
        ∠{point_A} = ∠{point_A}₁. На сторонах {point_A}{point_B} и {point_A}₁{point_B}₁
        отмечены точки {point_P} и {point_P}₁ так, что {point_A}{point_P} = {point_A}₁{point_P}₁.
        Докажите, что △{triangle_BPC} и △{triangle_B1P1C1}.
    """

    _figure_template = """
        [
            {{
                "type":"triangle",
                "name":"{triangle_ABC}"
            }},
            {{
                "type":"triangle",
                "name":"{triangle_A1B1C1}"
            }},
            {{
                "type":"triangle",
                "name":"{triangle_BPC}"
            }},
            {{
                "type":"triangle",
                "name":"{triangle_B1P1C1}"
            }},
            {{
                "type":"line",
                "name":"{point_A}{point_B}"
            }},
            {{
                "type":"line",
                "name":"{point_A}₁{point_B}₁"
            }},
            {{
                "type":"line",
                "name":"{point_A}{point_C}"
            }},
            {{
                "type":"line",
                "name":"{point_A}₁{point_C}₁"
            }},
            {{
                "type":"line",
                "name":"{point_A}{point_P}"
            }},
            {{
                "type":"line",
                "name":"{point_A}₁{point_P}₁"
            }},
            {{
                "type":"angle",
                "name":"{point_A}",
            }},
            {{
                "type":"angle",
                "name":"{point_A}₁",
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{triangle_BPC}",
                    "{triangle_B1P1C1}"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{point_A}{point_B}",
                    "{point_A}₁{point_B}₁"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{point_A}{point_C}",
                    "{point_A}₁{point_C}₁"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{point_A}{point_P}",
                    "{point_A}₁{point_P}₁"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{point_A}",
                    "{point_A}₁"
                ]
            }}
        ]
    """


class Task98Generator(MathTaskGenerator[Task98Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        point_A = points[0]
        point_B = points[1]
        point_C = points[2]
        point_P = points[3]

        triangle_ABC = f"{point_A}{point_B}{point_C}"
        triangle_A1B1C1 = f"{point_A}₁{point_B}₁{point_C}₁"
        triangle_BPC = f"{point_B}{point_P}{point_C}"
        triangle_B1P1C1 = f"{point_B}₁{point_P}₁{point_C}₁"

        return Task98Params(
            point_A=point_A,
            point_B=point_B,
            point_C=point_C,
            point_P=point_P,
            triangle_ABC=triangle_ABC,
            triangle_A1B1C1=triangle_A1B1C1,
            triangle_BPC=triangle_BPC,
            triangle_B1P1C1=triangle_B1P1C1
        )


class Task98Unit(MathTaskUnit):
    _math_task = Task98
    _math_task_generator = Task98Generator
