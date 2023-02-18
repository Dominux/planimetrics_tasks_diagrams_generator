import unittest

from math_tasks_generator.helpers.tests import test_math_task
from math_tasks_generator.math_tasks import Task96, Task96Generator


class TestTask96(unittest.TestCase):
    def test_task_96(self):
        test_math_task(Task96, Task96Generator)
