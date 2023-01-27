import abc
from dataclasses import asdict
from typing import Any, Generic, TypeVar

import drawSvg as draw


Params = TypeVar("Params")


class MathTask(Generic[Params], metaclass=abc.ABCMeta):
    """
    Base class for math tasks
    """

    _task_number: int
    _params: Params
    _prompt_template: str = ""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def prompt(self) -> str:
        return self._prompt_template.format(**asdict(self._params))

    @property
    @abc.abstractmethod
    def vector(self) -> draw.Drawing:
        ...


class MathTaskGenerator(Generic[Params], metaclass=abc.ABCMeta):
    """
    Base class for math task generators
    """

    @abc.abstractstaticmethod
    def gen_params() -> Params:
        ...
