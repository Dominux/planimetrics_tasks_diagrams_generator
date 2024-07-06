from dataclasses import dataclass

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task145Params(Params):
    point_1: str
    point_2: str
    point_3: str
    point_4: str


class Task145(MathTask[Task145Params]):
    _task_number = 145

    _prompt_template = """
        Отрезок {point_1}{point_2} - диаметр окружности с центром {point_3}, 
        а {point_1}{point_4} и {point_4}{point_2} - равные хорды этой окружности.
        Найдите ∠{point_4}{point_3}{point_1}.
    """


class Task145Generator(MathTaskGenerator[Task145Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        return Task145Params(
            point_1=points[0],
            point_2=points[1],
            point_3=points[2],
            point_4=points[3],
        )


class Task145Unit(MathTaskUnit):
    _math_task = Task145
    _math_task_generator = Task145Generator
