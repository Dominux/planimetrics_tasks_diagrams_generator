import abc


CorpusReprType = dict[str, int]


class BaseTokenizer(abc.ABC):
    """
    Base class for all tokenizers
    """

    @abc.abstractmethod
    def encode(self, text: str) -> str:
        """
        text -> vector
        """

    @abc.abstractmethod
    def decode(self, vector: str) -> str:
        """
        vector -> text
        """
