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
class Task406Params(Params):
    point_a: str
    point_b: str
    point_c: str
    point_d: str
    angle_b: int
    ac_size: float
    units: str


class Task406(MathTask[Task406Params]):
    _task_number = 406

    _prompt_template = """
        Найдите периметр ромба {point_a}{point_b}{point_c}{point_d},
        в котором ∠{point_b} = {angle_b}°, {point_a}{point_c} = {ac_size} {units}.
    """


class Task406Generator(MathTaskGenerator[Task406Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        return Task406Params(
            point_a=points[0],
            point_b=points[1],
            point_c=points[2],
            point_d=points[3],
            angle_b=random.randint(1, 179),
            ac_size=random.uniform(1, 100),
            units=get_random_units(),
        )


class Task406Unit(MathTaskUnit):
    _math_task = Task406
    _math_task_generator = Task406Generator
