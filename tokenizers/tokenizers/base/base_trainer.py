import abc
from pathlib import Path

from tokenizers.base.base import BaseTokenizer


class BaseTrainer(abc.ABC):
    """
    Base class for all tokenizers trainers
    """

    def __init__(self, corpus_filepath: Path) -> None:
        """
        @param corpus_filepath - a filepath to the whole piece of text to train on
        """

        self._corpus_filepath = corpus_filepath

    @abc.abstractmethod
    def train(self) -> BaseTokenizer:
        ...
