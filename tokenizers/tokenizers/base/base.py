import abc


RawVocabType = dict[str, int]


class BaseTokenizer(abc.ABC):
    """
    Base class for all tokenizers
    """

    def __init__(self, vocab: RawVocabType) -> None:
        self._vocab = vocab

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
