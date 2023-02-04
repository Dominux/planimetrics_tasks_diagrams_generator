import unittest

from math_tasks_generator.helpers.tests import test_math_task
from math_tasks_generator.math_tasks import Task98, Task98Generator


class TestTask98(unittest.TestCase):
    def test_task_98(self):
        test_math_task(Task98, Task98Generator)
