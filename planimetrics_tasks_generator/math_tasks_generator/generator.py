from pathlib import Path

from math_tasks_generator.helpers.run_task import (
    run_math_task,
)
from math_tasks_generator.base import MathTaskUnit

# Creating all tasks
import math_tasks_generator.math_tasks


AMOUNT = 20


class MainGenerator:
    path = Path("dataset")

    @classmethod
    def generate(cls, amount: int = AMOUNT):
        for task_unit in MathTaskUnit.__subclasses__():
            path = cls.path / str(task_unit._math_task._task_number)

            run_math_task(
                math_task=task_unit._math_task,
                task_gen=task_unit._math_task_generator,
                amount=amount,
                path=path,
                minify=True,
            )


if __name__ == "__main__":
    MainGenerator.generate(AMOUNT)
