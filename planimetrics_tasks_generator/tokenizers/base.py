import abc
import typing as t

from tokenizers.constants import END_TOKEN, START_TOKEN

if t.TYPE_CHECKING:
    import torch


class BaseTokenizer(t.Sized, metaclass=abc.ABCMeta):
    """
    Base class for all tokenizers
    """

    @abc.abstractmethod
    def encode(self, text: str) -> "torch.Tensor":
        """
        text -> vector
        """

    def decode(self, vector: "t.Iterable[int]") -> str:
        """
        vector -> text
        """
        return "".join(self.decode_index(i) for i in vector).replace(START_TOKEN, "").replace(END_TOKEN, "")

    @abc.abstractmethod
    def decode_index(self, index: int) -> str:
        """
        index -> text
        """
