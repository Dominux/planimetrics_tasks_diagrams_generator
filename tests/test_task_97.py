import unittest

from math_tasks_generator.helpers.tests import test_math_task
from math_tasks_generator.math_tasks import Task97, Task97Generator


class TestTask97(unittest.TestCase):
    def test_task_97(self):
        test_math_task(Task97, Task97Generator)
