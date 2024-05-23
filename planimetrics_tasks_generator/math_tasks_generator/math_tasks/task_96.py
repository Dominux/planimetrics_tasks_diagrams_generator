from dataclasses import dataclass
import random

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task96Params(Params):
    picture_number: int
    point_A: str
    point_B: str
    point_C: str
    point_D: str
    point_O: str
    side_OA: str
    side_OB: str
    side_OC: str
    side_OD: str
    angle_1_value: float
    angle_2_value: float
    triangle_AOB: str
    triangle_DOC: str
    angle_ACD: str


class Task96(MathTask[Task96Params]):
    _task_number = 96

    _prompt_template = """
        На рисунке {picture_number} {side_OA} = {side_OD}, {side_OB} = {side_OC},
        ∠1 = {angle_1_value}°, ∠2 = {angle_2_value}°.
        а) Докажите, что треугольники {triangle_AOB} и {triangle_DOC} равны;
        б) найдите ∠{angle_ACD}
    """

    _triangles_params_key = ("triangle_AOB", "triangle_DOC")


class Task96Generator(MathTaskGenerator[Task96Params]):
    @staticmethod
    def gen_params():
        picture_number = random.randint(1, 1500)

        points = get_random_letters(5)

        point_A = points[0]
        point_B = points[1]
        point_C = points[2]
        point_D = points[3]
        point_O = points[4]

        side_OA = f"{point_O}{point_A}"
        side_OB = f"{point_O}{point_B}"
        side_OC = f"{point_O}{point_C}"
        side_OD = f"{point_O}{point_D}"

        angle_1_value = random.randint(5, 85)
        angle_2_value = random.randint(5, 85)

        triangle_AOB = "".join((point_A, point_O, point_B))
        triangle_DOC = "".join((point_D, point_O, point_C))

        angle_ACD = "".join((point_A, point_C, point_D))

        return Task96Params(
            picture_number=picture_number,
            point_A=point_A,
            point_B=point_B,
            point_C=point_C,
            point_D=point_D,
            point_O=point_O,
            side_OA=side_OA,
            side_OB=side_OB,
            side_OC=side_OC,
            side_OD=side_OD,
            angle_1_value=angle_1_value,
            angle_2_value=angle_2_value,
            triangle_AOB=triangle_AOB,
            triangle_DOC=triangle_DOC,
            angle_ACD=angle_ACD,
        )


class Task96Unit(MathTaskUnit):
    _math_task = Task96
    _math_task_generator = Task96Generator
