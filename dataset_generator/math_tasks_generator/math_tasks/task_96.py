from dataclasses import dataclass
from numbers import Number
import random

from math_tasks_generator.base import MathTask, MathTaskGenerator
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task96Params:
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
    angle_1_value: Number
    angle_2_value: Number
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

    _vector_template = """
        <defs></defs>

        <path d="M0,0 L3,-8" stroke-width="0.2" stroke="black" />
        <path d="M0,0 L12,0" stroke-width="0.2" stroke="black" />
        <path d="M3,-8 L12,0" stroke-width="0.2" stroke="black" />
        <path d="M12,0 L15,-8" stroke-width="0.2" stroke="black" />
        <path d="M0,0 L15,-8" stroke-width="0.2" stroke="black" />

        <text x="0" y="1.6" font-size="1.5" dy="0em">{point_A}</text>
        <text x="1.7" y="-8" font-size="1.5" dy="0em">{point_B}</text>
        <text x="15.3" y="-8" font-size="1.5" dy="0em">{point_D}</text>
        <text x="12" y="1.5" font-size="1.5" dy="0em">{point_C}</text>
        <text x="7.2" y="-4.8" font-size="1.5" dy="0em">{point_O}</text>

        <path d="M4.3,-2.8 L4.7,-2" stroke-width="0.1" stroke="black" />
        <path d="M11,-6.4 L11.4,-5.6" stroke-width="0.1" stroke="black" />

        <path d="M5.3,-5.4 L5.7,-6.2" stroke-width="0.1" stroke="black" />
        <path d="M5.6,-5.1 L6,-5.9" stroke-width="0.1" stroke="black" />

        <path d="M9.3,-1.8 L9.7,-2.7" stroke-width="0.1" stroke="black" />
        <path d="M9.6,-1.5 L10,-2.4" stroke-width="0.1" stroke="black" />

        <text x="3.2" y="-4.9" font-size="1.2" dy="0em">1</text>
        <path d="M 2.5 -6.5 A 0.5 0.5 0 0 0 4.1 -7" fill="none" stroke-width="0.1" stroke="black"/>

        <text x="9.5" y="-0.3" font-size="1.2" dy="0em">2</text>
        <path d="M 10.7 0 A 0.5 0.5 0 0 1 10.9 -0.9" fill="none" stroke-width="0.1" stroke="black"/>
    """


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
