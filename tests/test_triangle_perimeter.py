import unittest

from who_cares.math_tasks import TrianglePerimeterTask, TrianglePerimeterParams


class TestTrianglePerimetersTask(unittest.TestCase):
    def test_triangle_perimeters_task(self):
        params = TrianglePerimeterParams(
            triangle="ABC",
            units_1="см",
            side_1="AB",
            side_2="BC",
            side_3="AC",
            side_1_size=7,
            side_3_side_2_diff=5,
        )
        task = TrianglePerimeterTask(params)

        # Saving prompt
        with open("lmao.txt", "w") as f:
            f.write(task.prompt)

        # Saving vector
        task.vector.saveSvg("lmao.svg")
