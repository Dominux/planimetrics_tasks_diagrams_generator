import abc
from dataclasses import asdict
from typing import Any

import drawSvg as draw


class MathTask(abc.ABC):
    """
    Base class for math tasks
    """

    _task_number: int
    _params: Any
    _prompt_template: str = ""

    @property
    def prompt(self) -> str:
        return self._prompt_template.format(**asdict(self._params))

    @property
    @abc.abstractmethod
    def vector(self) -> draw.Drawing:
        ...


class MathTaskGenerator(abc.ABC):
    """
    Base class for math task generators
    """

    @abc.abstractstaticmethod
    def gen_params() -> Any:
        ...
