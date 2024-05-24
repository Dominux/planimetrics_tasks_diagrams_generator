from dataclasses import dataclass

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task97Params(Params):
    point_A: str
    point_B: str
    point_C: str
    point_D: str
    point_of_crossing: str
    line_AC: str
    line_BD: str
    triangle_ABC: str
    triangle_CDA: str


class Task97(MathTask[Task97Params]):
    _task_number = 97

    _prompt_template = """
        Отрезки {line_AC} и {line_BD} точкой пересечения делятся пополам.
        Докажите, что △{triangle_ABC} = △{triangle_CDA}.
    """

    _figure_template = """
        [
            {{
                "type":"triangle",
                "name":"{triangle_ABC}
            }},
            {{
                "type":"triangle",
                "name":"{triangle_CDA}
            }},
            {{
                "type":"line",
                "name":"{line_AC}
            }},
            {{
                "type":"line",
                "name":"{line_BD}
            }},
            {{
                "type":"relation",
                "rel_type":"equality",
                "objects":[
                    "{triangle_ABC}",
                    "{triangle_CDA}"
                ]
            }},
            {{
                "type":"relation",
                "rel_type":"intersection",
                "objects":[
                    "{line_AC}",
                    "{line_BD}"
                ]
            }},
        ]
    """


class Task97Generator(MathTaskGenerator[Task97Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(5)

        point_A = points[0]
        point_B = points[1]
        point_C = points[2]
        point_D = points[3]
        point_of_crossing = points[4]

        line_AC = f"{point_A}{point_C}"
        line_BD = f"{point_B}{point_D}"

        triangle_ABC = f"{point_A}{point_B}{point_C}"
        triangle_CDA = f"{point_C}{point_D}{point_A}"

        return Task97Params(
            point_A=point_A,
            point_B=point_B,
            point_C=point_C,
            point_D=point_D,
            point_of_crossing=point_of_crossing,
            line_AC=line_AC,
            line_BD=line_BD,
            triangle_ABC=triangle_ABC,
            triangle_CDA=triangle_CDA,
        )


class Task97Unit(MathTaskUnit):
    _math_task = Task97
    _math_task_generator = Task97Generator
