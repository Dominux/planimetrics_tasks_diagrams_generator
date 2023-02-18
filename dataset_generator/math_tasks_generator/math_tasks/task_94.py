from dataclasses import dataclass
from numbers import Number
import random

from math_tasks_generator.base import MathTask, MathTaskGenerator
from math_tasks_generator.helpers import get_random_letters, get_random_units


@dataclass
class Task94Params:
    picture_number: int
    point_1: str
    point_2: str
    point_3: str
    point_4: str
    side_1: str
    side_2: str
    side_3: str
    side_4: str
    triangle_1: str
    triangle_2: str
    side_2_size: Number
    side_4_size: Number
    units: str


class Task94(MathTask[Task94Params]):
    _task_number = 94

    _prompt_template = """
        На рисунке {picture_number} {side_1} = {side_4}, ∠1 = ∠2.
        а) Докажите, что треугольники {triangle_1} и {triangle_2} равны;
        б) найдите {side_3} и {side_1}, если {side_2} = {side_2_size} {units}, {side_4} = {side_4_size} {units}
    """

    _vector_template = """
        <defs></defs>

        <path d="M0,0 L12,0" stroke-width="0.2" stroke="black" />
        <path d="M0,0 L13,-5" stroke-width="0.2" stroke="black" />
        <path d="M13,-5 L12,0" stroke-width="0.2" stroke="black" />
        <path d="M0,0 L13,5" stroke-width="0.2" stroke="black" />
        <path d="M13,5 L12,0" stroke-width="0.2" stroke="black" />

        <text x="0" y="1.8" font-size="1.5" dy="0em">{point_1}</text>
        <text x="13.3" y="-4" font-size="1.5" dy="0em">{point_2}</text>
        <text x="13.3" y="5" font-size="1.5" dy="0em">{point_3}</text>
        <text x="12.6" y="0.5" font-size="1.5" dy="0em">{point_4}</text>

        <path d="M2,0 L1.7,-0.63" stroke-width="0.1" stroke="black" />
        <path d="M2.3,0 L2.1,0.7" stroke-width="0.1" stroke="black" />

        <text x="4" y="-0.4" font-size="1.2" dy="0em">1</text>
        <text x="4" y="1.15" font-size="1.2" dy="0em">2</text>

        <path d="M6.5,-2 L6,-2.8" stroke-width="0.1" stroke="black" />
        <path d="M6.5,2 L6,2.8" stroke-width="0.1" stroke="black" />
    """


class Task94Generator(MathTaskGenerator[Task94Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        side_1 = f"{points[0]}{points[1]}"
        side_2 = f"{points[1]}{points[3]}"
        side_3 = f"{points[3]}{points[2]}"
        side_4 = f"{points[2]}{points[0]}"

        picture_number = random.randint(1, 1500)

        triangle_1 = "".join((points[0], points[1], points[3]))
        triangle_2 = "".join((points[0], points[2], points[3]))

        side_2_size = random.randint(1, 20)
        side_4_size = random.randint(1, 20)

        units = get_random_units()

        return Task94Params(
            picture_number=picture_number,
            point_1=points[0],
            point_2=points[1],
            point_3=points[2],
            point_4=points[3],
            side_1=side_1,
            side_2=side_2,
            side_3=side_3,
            side_4=side_4,
            triangle_1=triangle_1,
            triangle_2=triangle_2,
            side_2_size=side_2_size,
            side_4_size=side_4_size,
            units=units,
        )
