import abc
from dataclasses import asdict, dataclass
from typing import Generic, Type, TypeVar


@dataclass
class Params:
    ...


TParams = TypeVar("TParams", bound=Params)


class MathTask(Generic[TParams], metaclass=abc.ABCMeta):
    """
    Base class for math tasks
    """

    _task_number: int
    _prompt_template: str
    _figure_template: str

    def __init__(self, params: "Params", minify: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._params = params
        self._minify = minify

    @property 
    def prompt(self) -> str:
        prompt = self._prompt_template.format_map(asdict(self._params))
        return self.minify_text(prompt, sep=" ")

    @property
    def figure(self) -> str:
        return str(self._task_number)

    @staticmethod
    def minify_text(raw_text: str, sep: str = "") -> str:
        return sep.join([line.strip() for line in raw_text.splitlines()]).strip()


class MathTaskGenerator(Generic[TParams], metaclass=abc.ABCMeta):
    """
    Base class for math task generators
    """

    @staticmethod
    @abc.abstractmethod
    def gen_params() -> "Params":
        ...


class MathTaskUnit(abc.ABC):
    """
    Base class to store math tasks in a single place
    """

    _math_task: Type["MathTask"]
    _math_task_generator: Type["MathTaskGenerator"]
