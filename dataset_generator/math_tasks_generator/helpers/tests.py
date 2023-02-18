from typing import Type

from math_tasks_generator.base import MathTask, MathTaskGenerator
from math_tasks_generator.helpers.run_task import run_math_task


def test_math_task(math_task: Type[MathTask], task_gen: Type[MathTaskGenerator]):
    return run_math_task(math_task, task_gen=task_gen)
