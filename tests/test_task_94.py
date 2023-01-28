import unittest

from math_tasks_generator.helpers.tests import test_math_task
from math_tasks_generator.math_tasks import Task94, Task94Generator


class TestTask94(unittest.TestCase):
    def test_task_94(self):
        test_math_task(Task94, Task94Generator)
