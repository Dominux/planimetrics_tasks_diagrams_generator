from dataclasses import dataclass

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task732Params(Params):
    point_a: str
    point_b: str
    point_c: str
    point_m: str
    point_h: str


class Task732(MathTask[Task732Params]):
    _task_number = 732

    _prompt_template = """
        В прямоугольном треугольнике {point_a}{point_b}{point_c} из точки {point_m}
        стороны {point_a}{point_c} проведен перпендикуляр {point_m}{point_h}
        к гипотенузе {point_a}{point_b}. Докажите, что углы {point_m}{point_h}{point_c}
        и {point_m}{point_b}{point_c} равны.
    """


class Task732Generator(MathTaskGenerator[Task732Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(5)

        return Task732Params(
            point_a=points[0],
            point_b=points[1],
            point_c=points[2],
            point_m=points[3],
            point_h=points[4],
        )


class Task732Unit(MathTaskUnit):
    _math_task = Task732
    _math_task_generator = Task732Generator
