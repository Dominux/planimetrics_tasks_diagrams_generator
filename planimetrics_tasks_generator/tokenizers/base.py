import abc
import typing as t

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
        return "".join(self.decode_index(i) for i in vector)

    @abc.abstractmethod
    def decode_index(self, index: int) -> str:
        """
        index -> text
        """
