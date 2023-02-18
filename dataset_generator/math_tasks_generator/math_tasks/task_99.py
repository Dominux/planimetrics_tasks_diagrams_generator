from dataclasses import dataclass

from math_tasks_generator.base import MathTask, MathTaskGenerator, MathTaskUnit
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task99Params:
    point_A: str
    point_B: str
    point_C: str
    point_D: str
    point_E: str


class Task99(MathTask[Task99Params]):
    _task_number = 99

    _prompt_template = """
        На сторонах угла {point_C}{point_A}{point_D} отмечены точки {point_B} и {point_E} так,
        что точка {point_B} лежит на отрезке {point_A}{point_C}, а точка {point_E} — на
        отрезке {point_A}{point_D}, причем {point_A}{point_C} = {point_A}{point_D} и
        {point_A}{point_B} = {point_A}{point_E}. Докажите, что 
        ∠{point_C}{point_B}{point_D} = ∠{point_D}{point_E}{point_C}
    """

    _vector_template = """
        <defs></defs>
        <path d="M0,0 L9,2" stroke-width="0.2" stroke="black" />
        <path d="M9,2 L-1,-14" stroke-width="0.2" stroke="black" />
        <path d="M-1,-14 L0,0" stroke-width="0.2" stroke="black" />
        <text x="0.3" y="-0.3" font-size="1.5" dy="0em">{point_C}</text>
        <text x="-1.5" y="-14.3" font-size="1.5" dy="0em">{point_A}</text>
        <text x="9.3" y="2.5" font-size="1.5" dy="0em">{point_D}</text>

        <path d="M-0.3,-5 L5.2,-4" stroke-width="0.2" stroke="black" />
        <text x="0" y="-5.3" font-size="1.5" dy="0em">{point_B}</text>
        <text x="5.6" y="-3.8" font-size="1.5" dy="0em">{point_E}</text>

        <path d="M-0.7,-2.5 L0.3,-2.4" stroke-width="0.1" stroke="black" />
        <path d="M7.4,-1.4 L6.4,-1.2" stroke-width="0.1" stroke="black" />

        <path d="M-1.2,-9 L-0.2,-8.9" stroke-width="0.1" stroke="black" />
        <path d="M-1.2,-9.3 L-0.2,-9.2" stroke-width="0.1" stroke="black" />

        <path d="M1.7,-8.8 L2.7,-8.9" stroke-width="0.1" stroke="black" />
        <path d="M1.5,-9.1 L2.5,-9.2" stroke-width="0.1" stroke="black" />
    """


class Task99Generator(MathTaskGenerator[Task99Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(5)

        point_A = points[0]
        point_B = points[1]
        point_C = points[2]
        point_D = points[3]
        point_E = points[4]

        return Task99Params(
            point_A=point_A,
            point_B=point_B,
            point_C=point_C,
            point_D=point_D,
            point_E=point_E,
        )


class Task99Unit(MathTaskUnit):
    _math_task = Task99
    _math_task_generator = Task99Generator
