import unittest

from math_tasks_generator.helpers.tests import test_math_task
from math_tasks_generator.math_tasks import Task95, Task95Generator


class TestTask95(unittest.TestCase):
    def test_task_95(self):
        test_math_task(Task95, Task95Generator)
