import abc
from dataclasses import asdict
from typing import Generic, Type, TypeVar


Params = TypeVar("Params")


class MathTask(Generic[Params], metaclass=abc.ABCMeta):
    """
    Base class for math tasks
    """

    _task_number: int
    _prompt_template: str = ""
    _triangle_params_key: str = ""

    def __init__(self, params: "Params", minify: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._params = params
        self._minify = minify

    @property
    def prompt(self) -> str:
        prompt = self._prompt_template.format(**asdict(self._params)) # type: ignore
        return self.minify_text(prompt)

    @property
    def vector(self) -> str:
        return getattr(self._params, self._triangle_params_key)

    @staticmethod
    def minify_text(raw_text: str) -> str:
        return " ".join([line.strip() for line in raw_text.splitlines()]).strip()


class MathTaskGenerator(Generic[Params], metaclass=abc.ABCMeta):
    """
    Base class for math task generators
    """

    @abc.abstractstaticmethod
    def gen_params() -> "Params":
        ...


class MathTaskUnit(abc.ABC):
    """
    Base class to store math tasks in a single place
    """

    _math_task: Type["MathTask"]
    _math_task_generator: Type["MathTaskGenerator"]
