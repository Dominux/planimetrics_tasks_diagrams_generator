import unittest

from math_tasks_generator.helpers.tests import test_math_task
from math_tasks_generator.math_tasks import Task99, Task99Generator


class TestTask99(unittest.TestCase):
    def test_task_99(self):
        test_math_task(Task99, Task99Generator)
