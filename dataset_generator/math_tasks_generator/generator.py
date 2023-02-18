from pathlib import Path

from math_tasks_generator.helpers.run_task import run_math_task
from math_tasks_generator.base import MathTaskUnit


AMOUNT = 100


class MainGenerator:
    path = Path("dataset")

    @classmethod
    def generate(cls, amount: int):
        for task_unit in MathTaskUnit.__subclasses__():
            run_math_task(
                math_task=task_unit._math_task,
                task_gen=task_unit._math_task_generator,
                amount=amount,
                path=cls.path,
            )


if __name__ == "__main__":
    MainGenerator.generate(AMOUNT)
