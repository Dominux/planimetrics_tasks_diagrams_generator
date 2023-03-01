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
    _vector_template: str = ""

    def __init__(self, params: Params, minify: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._params = params
        self._minify = minify

    @property
    def prompt(self) -> str:
        prompt = self._prompt_template.format(**asdict(self._params))
        return self.minify_text(prompt)

    @property
    def vector(self) -> str:
        inner_svg = self._vector_template.format(**asdict(self._params))
        svg = """
            <?xml version="1.0" encoding="UTF-8"?>
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="40" height="40" viewBox="-20.0 -20.0 40 40">{}</svg>
        """.format(
            inner_svg
        )
        return self.minify_vector(svg)

    def minify_vector(self, raw_vector: str) -> str:
        delimiter = "" if self._minify else "\n"
        vector = delimiter.join([line.strip() for line in raw_vector.splitlines()])

        return vector[1:] if vector.startswith("\n") else vector

    @staticmethod
    def minify_text(raw_text: str) -> str:
        return " ".join([line.strip() for line in raw_text.splitlines()]).strip()


class MathTaskGenerator(Generic[Params], metaclass=abc.ABCMeta):
    """
    Base class for math task generators
    """

    @abc.abstractstaticmethod
    def gen_params() -> Params:
        ...


class MathTaskUnit(abc.ABC):
    """
    Base class to store math tasks in a single place
    """

    _math_task: Type[MathTask]
    _math_task_generator: Type[MathTaskGenerator]
