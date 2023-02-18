from dataclasses import dataclass

from math_tasks_generator.base import MathTask, MathTaskGenerator, MathTaskUnit
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task98Params:
    point_A: str
    point_B: str
    point_C: str
    point_P: str


class Task98(MathTask[Task98Params]):
    _task_number = 98

    _prompt_template = """
        В треугольниках {point_A}{point_B}{point_C} и {point_A}₁{point_B}₁{point_C}₁
        {point_A}{point_B} = {point_A}₁{point_B}₁, {point_A}{point_C} = {point_A}₁{point_C}₁,
        ∠{point_A} = ∠{point_A}₁. На сторонах {point_A}{point_B} и {point_A}₁{point_B}₁
        отмечены точки {point_P} и {point_P}₁ так, что {point_A}{point_P} = {point_A}₁{point_P}₁.
        Докажите, что △{point_B}{point_P}{point_C} и △{point_B}₁{point_P}₁{point_C}₁.
    """

    _vector_template = """
        <defs></defs>
        <path d="M0,0 L7,2" stroke-width="0.2" stroke="black" />
        <path d="M7,2 L-1,-12" stroke-width="0.2" stroke="black" />
        <path d="M-1,-12 L0,0" stroke-width="0.2" stroke="black" />
        <text x="1" y="-1" font-size="1.5" dy="0em">{point_A}</text>
        <text x="-1.3" y="-12.2" font-size="1.5" dy="0em">{point_B}</text>
        <text x="7.1" y="2.1" font-size="1.5" dy="0em">{point_C}</text>

        <path d="M3.2,1.5 L3.5,0.4" stroke-width="0.1" stroke="black" />

        <path d="M-1,-4.5 L0.1,-4.5" stroke-width="0.1" stroke="black" />
        <path d="M-1,-4.2 L0.1,-4.2" stroke-width="0.1" stroke="black" />

        <path d="M 0 -0.7 A 0.5 0.5 0 0 1 1 0.3" fill="none" stroke-width="0.1" stroke="black"/>

        <text x="-1.7" y="-7" font-size="1.5" dy="0em">{point_P}</text>
        <path d="M-0.6,-7 L7,2" stroke-width="0.2" stroke="black" />

        <path d="M3.5,-2.8 L3.2,-1.8" stroke-width="0.1" stroke="black" />
        <path d="M3.3,-3 L3,-2" stroke-width="0.1" stroke="black" />
        <path d="M3.1,-3.2 L2.8,-2.2" stroke-width="0.1" stroke="black" />

        <path d="M-3,0 L-10,2" stroke-width="0.2" stroke="black" />
        <path d="M-10,2 L-4,-12" stroke-width="0.2" stroke="black" />
        <path d="M-4,-12 L-3,0" stroke-width="0.2" stroke="black" />
        <text x="-5.8" y="-0.8" font-size="1.5" dy="0em">{point_A}₁</text>
        <text x="-4.8" y="-12.2" font-size="1.5" dy="0em">{point_B}₁</text>
        <text x="-11.8" y="2.3" font-size="1.5" dy="0em">{point_C}₁</text>

        <path d="M-6.2,1.5 L-6.5,0.4" stroke-width="0.1" stroke="black" />

        <path d="M-4,-4.5 L-2.8,-4.5" stroke-width="0.1" stroke="black" />
        <path d="M-4,-4.2 L-2.8,-4.2" stroke-width="0.1" stroke="black" />

        <path d="M -3 -0.7 A 0.5 0.5 0 0 0 -4 0.3" fill="none" stroke-width="0.1" stroke="black"/>

        <text x="-5.3" y="-7" font-size="1.5" dy="0em">{point_P}₁</text>
        <path d="M-3.6,-7 L-10,2" stroke-width="0.2" stroke="black" />

        <path d="M-7.2,-2.7 L-6.8,-1.7" stroke-width="0.1" stroke="black" />
        <path d="M-7,-3 L-6.6,-2" stroke-width="0.1" stroke="black" />
        <path d="M-6.8,-3.3 L-6.4,-2.3" stroke-width="0.1" stroke="black" />
    """


class Task98Generator(MathTaskGenerator[Task98Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        point_A = points[0]
        point_B = points[1]
        point_C = points[2]
        point_P = points[3]

        return Task98Params(
            point_A=point_A,
            point_B=point_B,
            point_C=point_C,
            point_P=point_P,
        )


class Task98Unit(MathTaskUnit):
    _math_task = Task98
    _math_task_generator = Task98Generator
