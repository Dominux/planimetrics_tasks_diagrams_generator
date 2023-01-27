import unittest

from math_tasks_generator.helpers.functions import get_task_path
from math_tasks_generator.math_tasks import Task90, Task90Generator


class TestTask90(unittest.TestCase):
    def test_task_90(self):
        path = get_task_path(Task90)

        for i in range(10):
            # Creating path
            path_i = path / str(i)
            path_i.mkdir(parents=True, exist_ok=True)
            filepath = path_i / str(Task90._task_number)

            # Generating params and task
            params = Task90Generator.gen_params()
            task = Task90(params)

            # Saving prompt
            with filepath.with_suffix(".txt").open("w") as f:
                f.write(task.prompt)

            # Saving vector
            task.vector.saveSvg(filepath.with_suffix(".svg"))
