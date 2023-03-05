import abc
from pathlib import Path

from tokenizers.base.base import BaseTokenizer


class BaseTrainer(abc.ABC):
    """
    Base class for all tokenizers trainers
    """

    def __init__(self, corpus_filepath: Path | str) -> None:
        """
        @param corpus_filepath - a filepath to the whole piece of text to train on
        """

        if isinstance(corpus_filepath, str):
            corpus_filepath = Path(corpus_filepath)

        self._corpus_filepath = corpus_filepath
        self.all_sentences = []

    @abc.abstractmethod
    def train(self, iterations_amount: int = 50) -> BaseTokenizer:
        ...
