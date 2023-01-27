from pathlib import Path
import random
import string
import math
from numbers import Number
from typing import List, Tuple, Type

from math_tasks_generator.base import MathTask
from math_tasks_generator.types import Coords


def get_triangle_coordinates(
    size_ab: Number,
    size_bc: Number,
    size_ac: Number,
) -> Tuple[Coords, Coords, Coords]:
    # TODO: works badly, but I haven't found fine solution, so...

    a = Coords(0, 0)
    b = Coords(size_ab, 0)

    cx = (size_ac**2 - size_bc**2 + size_ab**2) / (2 * size_ab)

    cy = math.sqrt(abs(size_ac**2 - cx**2))

    c = Coords(cx, cy)

    return a, b, c


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
