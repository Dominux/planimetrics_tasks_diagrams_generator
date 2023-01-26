import unittest

from who_cares.helpers.functions import get_task_path
from who_cares.math_tasks import (
    TrianglePerimeterTask,
    TrianglePerimeterTaskGenerator,
)


class TestTrianglePerimetersTask(unittest.TestCase):
    def test_triangle_perimeters_task(self):
        path = get_task_path(TrianglePerimeterTask)

        for i in range(10):
            # Creating path
            path_i = path / str(i)
            path_i.mkdir(parents=True, exist_ok=True)
            filepath = path_i / str(TrianglePerimeterTask._task_number)

            # Generating params and task
            params = TrianglePerimeterTaskGenerator.gen_params()
            task = TrianglePerimeterTask(params)

            # Saving prompt
            with filepath.with_suffix(".txt").open("w") as f:
                f.write(task.prompt)

            # Saving vector
            task.vector.saveSvg(filepath.with_suffix(".svg"))
