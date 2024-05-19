import abc
import typing as t


class BaseTokenizer(t.Sized, metaclass=abc.ABCMeta):
    """
    Base class for all tokenizers
    """

    @abc.abstractmethod
    def encode(self, text: str) -> list[int]:
        """
        text -> vector
        """

    def decode(self, vector: list[int]) -> str:
        """
        vector -> text
        """
        return "".join(self.decode_index(i) for i in vector)

    @abc.abstractmethod
    def decode_index(self, index: int) -> str:
        """
        index -> text
        """
