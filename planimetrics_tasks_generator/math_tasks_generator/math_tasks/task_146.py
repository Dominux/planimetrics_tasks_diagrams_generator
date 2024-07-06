from dataclasses import dataclass
import random

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters, get_random_units


@dataclass
class Task146Params(Params):
    point_a: str
    point_b: str
    point_c: str
    point_d: str
    point_o: str
    cb_size: int
    ab_size: int
    units: str


class Task146(MathTask[Task146Params]):
    _task_number = 146

    _prompt_template = """
        Отрезки {point_a}{point_b} и {point_c}{point_d} - диаметры окружности с центром {point_o}.
        Найдите периметр треугольника {point_a}{point_o}{point_d}, если известно,
        что {point_c}{point_b} = {cb_size} {units}, {point_a}{point_b} = {ab_size} {units}.
    """


class Task146Generator(MathTaskGenerator[Task146Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(5)

        return Task146Params(
            point_a=points[0],
            point_b=points[1],
            point_c=points[2],
            point_d=points[3],
            point_o=points[4],
            cb_size=random.randint(1, 30),
            ab_size=random.randint(1, 30),
            units=get_random_units(),
        )


class Task146Unit(MathTaskUnit):
    _math_task = Task146
    _math_task_generator = Task146Generator
