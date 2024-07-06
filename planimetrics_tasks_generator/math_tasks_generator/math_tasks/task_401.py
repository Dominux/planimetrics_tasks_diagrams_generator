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
class Task401Params(Params):
    point_a: str
    point_b: str
    point_c: str
    point_d: str
    bc_1_size: float
    bc_2_size: float
    dc_1_size: float
    dc_2_size: float
    bc_units: str
    dc_units: str


class Task401(MathTask[Task401Params]):
    _task_number = 401

    _prompt_template = """
       Найдите периметр прямоугольника {point_a}{point_b}{point_c}{point_d},
       если бисскектриса угла {point_a} делит строну:
       а) {point_b}{point_c} на отрезки {bc_1_size} {bc_units} и {bc_2_size} {bc_units};
       б) {point_d}{point_c} на отрезки {dc_1_size} {dc_units} и {dc_2_size} {dc_units}.
    """


class Task401Generator(MathTaskGenerator[Task401Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        return Task401Params(
            point_a=points[0],
            point_b=points[1],
            point_c=points[2],
            point_d=points[3],
            bc_1_size=random.uniform(1, 100),
            bc_2_size=random.uniform(1, 100),
            dc_1_size=random.uniform(1, 100),
            dc_2_size=random.uniform(1, 100),
            bc_units=get_random_units(),
            dc_units=get_random_units(),
        )


class Task401Unit(MathTaskUnit):
    _math_task = Task401
    _math_task_generator = Task401Generator
