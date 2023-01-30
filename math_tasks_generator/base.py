import abc
from dataclasses import asdict
from typing import Generic, TypeVar


Params = TypeVar("Params")


class MathTask(Generic[Params], metaclass=abc.ABCMeta):
    """
    Base class for math tasks
    """

    _task_number: int
    _prompt_template: str = ""
    _vector_template: str = ""

    def __init__(self, params: Params, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._params = params

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

    @staticmethod
    def minify_vector(raw_vector: str, minify: bool = False) -> str:
        delimiter = "" if minify else "\n"
        return delimiter.join([line.strip() for line in raw_vector.splitlines()])

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
