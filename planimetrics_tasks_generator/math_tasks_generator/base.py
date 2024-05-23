import abc
from dataclasses import asdict, dataclass
from typing import Generic, Type, TYPE_CHECKING, TypeVar
if TYPE_CHECKING:
    from typing import Iterable


@dataclass
class Params:
    ...


TParams = TypeVar("TParams", bound=Params)


class MathTask(Generic[TParams], metaclass=abc.ABCMeta):
    """
    Base class for math tasks
    """

    _task_number: int
    _prompt_template: str = ""
    _triangles_params_key: "Iterable[str]"

    def __init__(self, params: "Params", minify: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._params = params
        self._minify = minify

    @property 
    def prompt(self) -> str:
        prompt = self._prompt_template.format(**asdict(self._params))
        return self.minify_text(prompt)

    @property
    def figure(self) -> str:
        return "\n".join(getattr(self._params, k) for k in self._triangles_params_key)

    @staticmethod
    def minify_text(raw_text: str) -> str:
        return " ".join([line.strip() for line in raw_text.splitlines()]).strip()


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
