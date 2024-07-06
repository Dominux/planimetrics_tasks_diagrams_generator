from dataclasses import dataclass

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task402Params(Params):
    point_a: str
    point_b: str
    point_c: str
    point_d: str
    point_o: str


class Task402(MathTask[Task402Params]):
    _task_number = 402

    _prompt_template = """
        Диагонали прямоугольника {point_a}{point_b}{point_c}{point_d} пересекаются в точке {point_o}.
        Докажите, что треугольники {point_a}{point_o}{point_d} и {point_a}{point_o}{point_b} равнобедренные.
    """


class Task402Generator(MathTaskGenerator[Task402Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(5)

        return Task402Params(
            point_a=points[0],
            point_b=points[1],
            point_c=points[2],
            point_d=points[3],
            point_o=points[4],
        )


class Task402Unit(MathTaskUnit):
    _math_task = Task402
    _math_task_generator = Task402Generator
