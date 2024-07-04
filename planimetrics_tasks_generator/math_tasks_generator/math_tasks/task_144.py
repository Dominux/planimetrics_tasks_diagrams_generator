from dataclasses import dataclass

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task144Params(Params):
    point_1: str
    point_2: str
    point_3: str
    point_4: str
    point_5: str
    point_6: str


class Task144(MathTask[Task144Params]):
    _task_number = 144

    _prompt_template = """
        Отрезки {point_1}{point_2} и {point_3}{point_4} - диаметры окружности. 
        Докажите, что: a) хорды {point_2}{point_4} и {point_1}{point_3} равны;
        б) хорды {point_1}{point_4} и {point_2}{point_3} равны; 
        в) ∠{point_2}{point_1}{point_4}=∠{point_2}{point_3}{point_4}.
    """


class Task144Generator(MathTaskGenerator[Task144Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(6)

        return Task144Params(
            point_1=points[0],
            point_2=points[1],
            point_3=points[2],
            point_4=points[3],
            point_5=points[4],
            point_6=points[5],
        )


class Task144Unit(MathTaskUnit):
    _math_task = Task144
    _math_task_generator = Task144Generator
