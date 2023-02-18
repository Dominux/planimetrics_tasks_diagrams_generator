from dataclasses import dataclass
import random

from math_tasks_generator.base import MathTask, MathTaskGenerator, MathTaskUnit
from math_tasks_generator.helpers import get_random_letters, get_random_units


@dataclass
class Task95Params:
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
    side_3_size: float
    side_4_size: float
    units: str


class Task95(MathTask[Task95Params]):
    _task_number = 95

    _prompt_template = """
        На рисунке {picture_number} {side_2} = {side_4}, ∠1 = ∠2.
        а) Докажите, что треугольники {triangle_1} и {triangle_2} равны;
        б) найдите {side_1} и {side_2}, если {side_4} = {side_4_size} {units}, {side_3} = {side_3_size} {units}
    """

    _vector_template = """
        <defs></defs>

        <path d="M0,0 L3,-8" stroke-width="0.2" stroke="black" />
        <path d="M0,0 L12,0" stroke-width="0.2" stroke="black" />
        <path d="M3,-8 L15,-8" stroke-width="0.2" stroke="black" />
        <path d="M12,0 L15,-8" stroke-width="0.2" stroke="black" />
        <path d="M0,0 L15,-8" stroke-width="0.2" stroke="black" />

        <text x="0" y="1.6" font-size="1.5" dy="0em">{point_1}</text>
        <text x="1.7" y="-8" font-size="1.5" dy="0em">{point_2}</text>
        <text x="15.3" y="-8" font-size="1.5" dy="0em">{point_3}</text>
        <text x="12" y="1.5" font-size="1.5" dy="0em">{point_4}</text>

        <path d="M8,-8.4 L7.7,-7.6" stroke-width="0.1" stroke="black" />
        <path d="M7,-0.4 L6.7,0.4" stroke-width="0.1" stroke="black" />

        <text x="10.5" y="-6.5" font-size="1.2" dy="0em">1</text>
        <path d="M 12.7 -8 A 0.5 0.5 0 0 0 13.3 -7.1" fill="none" stroke-width="0.1" stroke="black"/>

        <text x="3.5" y="-0.5" font-size="1.2" dy="0em">2</text>
        <path d="M 1.7 0 A 0.5 0.5 0 0 0 1.6 -0.9" fill="none" stroke-width="0.1" stroke="black"/>

        <text x="11.5" y="-3.8" font-size="1.2" dy="0em">3</text>
        <path d="M 12.1 -6.5 A 0.5 0.5 0 0 0 14.2 -5.7" fill="none" stroke-width="0.1" stroke="black"/>
        <path d="M 12.5 -6.7 A 0.5 0.5 0 0 0 14.3 -6.2" fill="none" stroke-width="0.1" stroke="black"/>

        <text x="2.5" y="-2.8" font-size="1.2" dy="0em">4</text>
        <path d="M 1.1 -2.8 A 0.5 0.5 0 0 1 2.2 -1.1" fill="none" stroke-width="0.1" stroke="black"/>
        <path d="M 0.7 -2 A 0.5 0.5 0 0 1 1.9 -1.1" fill="none" stroke-width="0.1" stroke="black"/>
    """


class Task95Generator(MathTaskGenerator[Task95Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        side_1 = f"{points[0]}{points[1]}"
        side_2 = f"{points[1]}{points[2]}"
        side_3 = f"{points[2]}{points[3]}"
        side_4 = f"{points[3]}{points[0]}"

        picture_number = random.randint(1, 1500)

        triangle_1 = "".join((points[0], points[1], points[2]))
        triangle_2 = "".join((points[0], points[2], points[3]))

        side_3_size = random.randint(1, 20)
        side_4_size = random.randint(1, 20)

        units = get_random_units()

        return Task95Params(
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
            side_3_size=side_3_size,
            side_4_size=side_4_size,
            units=units,
        )


class Task95Unit(MathTaskUnit):
    _math_task = Task95
    _math_task_generator = Task95Generator
