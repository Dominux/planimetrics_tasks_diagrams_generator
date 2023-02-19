import abc

from tokenizers.tokenizers.base.base import BaseTokenizer


class BaseTrainer(abc.ABC):
    """
    Base class for all tokenizers trainers
    """

    def __init__(self, corpus: str) -> None:
        """
        @param corpus - whole piece of text to train on
        """

        self._corpus = corpus

    @abc.abstractmethod
    def train(self) -> BaseTokenizer:
        ...
