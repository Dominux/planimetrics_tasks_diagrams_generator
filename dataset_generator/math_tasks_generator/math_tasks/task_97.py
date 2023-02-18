from dataclasses import dataclass

from math_tasks_generator.base import MathTask, MathTaskGenerator
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task97Params:
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

    _vector_template = """
        <defs></defs>

        <path d="M0,0 L3,-8" stroke-width="0.2" stroke="black" />
        <path d="M3,-8 L12,0" stroke-width="0.2" stroke="black" />
        <path d="M12,0 L15,-8" stroke-width="0.2" stroke="black" />
        <path d="M0,0 L15,-8" stroke-width="0.2" stroke="black" />
        <path d="M0,0 L12,0" stroke-width="0.2" stroke="black" />
        <path d="M3,-8 L15,-8" stroke-width="0.2" stroke="black" />

        <text x="0" y="1.6" font-size="1.5" dy="0em">{point_A}</text>
        <text x="1.7" y="-8" font-size="1.5" dy="0em">{point_B}</text>
        <text x="15.3" y="-8" font-size="1.5" dy="0em">{point_C}</text>
        <text x="12" y="1.5" font-size="1.5" dy="0em">{point_D}</text>
        <text x="7.2" y="-4.8" font-size="1.5" dy="0em">{point_of_crossing}</text>

        <path d="M4.3,-2.8 L4.7,-2" stroke-width="0.1" stroke="black" />
        <path d="M11,-6.4 L11.4,-5.6" stroke-width="0.1" stroke="black" />

        <path d="M5.3,-5.4 L5.7,-6.2" stroke-width="0.1" stroke="black" />
        <path d="M5.6,-5.1 L6,-5.9" stroke-width="0.1" stroke="black" />

        <path d="M9.3,-1.8 L9.7,-2.7" stroke-width="0.1" stroke="black" />
        <path d="M9.6,-1.5 L10,-2.4" stroke-width="0.1" stroke="black" />
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
