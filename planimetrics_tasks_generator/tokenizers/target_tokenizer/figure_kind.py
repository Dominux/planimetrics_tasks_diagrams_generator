import abc
import enum


class FigureKindInvariant(abc.ABC):
    name: str

    def __init__(self, value: str):
        self._value = value

    @abc.abstractmethod
    def format(self) -> str:
        ...
    

class TriangleInvariant(FigureKindInvariant):
    name = "triangle"

    def format(self) -> str:
        return self._value.upper()


class FigureKind(enum.Enum):
    Triangle = TriangleInvariant

    @staticmethod
    def names():
        return [sub.name for sub in FigureKindInvariant.__subclasses__()]
