import unittest

from math_tasks_generator.helpers.tests import test_math_task
from math_tasks_generator.math_tasks import Task90, Task90Generator


class TestTask90(unittest.TestCase):
    def test_task_90(self):
        test_math_task(Task90, Task90Generator)
