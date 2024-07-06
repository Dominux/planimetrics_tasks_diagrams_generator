from dataclasses import dataclass

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task717Params(Params):
    point_a: str
    point_b: str
    point_c: str
    point_d: str


class Task717(MathTask[Task717Params]):
    _task_number = 717

    _prompt_template = """
        Отрезок {point_a}{point_b} является диаметром окружности,
        а хорды {point_b}{point_c} и {point_a}{point_d} параллельны.
        Докажите, что хорды {point_c}{point_d} является диаметром.
    """


class Task717Generator(MathTaskGenerator[Task717Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        return Task717Params(
            point_a=points[0],
            point_b=points[1],
            point_c=points[2],
            point_d=points[3],
        )


class Task717Unit(MathTaskUnit):
    _math_task = Task717
    _math_task_generator = Task717Generator
