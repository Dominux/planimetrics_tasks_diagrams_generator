from pathlib import Path
import random
import string
from typing import List, Type

from math_tasks_generator.base import MathTask


def get_random_letter() -> str:
    return random.choice(string.ascii_uppercase)


def get_random_letters(length: int) -> List[str]:
    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)
    return alphabet[:length]


units = ("мм", "см", "дм", "м")


def get_random_units() -> str:
    return random.choice(units)


def get_task_path(task: Type[MathTask]) -> Path:
    return Path("examples") / str(task._task_number)
