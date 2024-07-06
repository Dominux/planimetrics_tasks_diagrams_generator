from dataclasses import dataclass

from math_tasks_generator.base import (
    MathTask,
    MathTaskGenerator,
    MathTaskUnit,
    Params,
)
from math_tasks_generator.helpers import get_random_letters


@dataclass
class Task730Params(Params):
    point_a: str
    point_b: str
    point_c: str
    point_o: str


class Task730(MathTask[Task730Params]):
    _task_number = 730

    _prompt_template = """
        Через точки {point_a} и {point_b} проведены прямые,
        перпендкилярные к сторонам угла {point_a}{point_o}{point_b}
        и пересекающиеся в точке {point_c} внутри угла. Докажите,
        что около четырехугольника {point_a}{point_c}{point_b}{point_o}
        можно описать окружность.
    """


class Task730Generator(MathTaskGenerator[Task730Params]):
    @staticmethod
    def gen_params():
        points = get_random_letters(4)

        return Task730Params(
            point_a=points[0],
            point_b=points[1],
            point_c=points[2],
            point_o=points[3],
        )


class Task730Unit(MathTaskUnit):
    _math_task = Task730
    _math_task_generator = Task730Generator
