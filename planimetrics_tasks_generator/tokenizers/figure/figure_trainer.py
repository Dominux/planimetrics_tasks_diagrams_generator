import os
from pathlib import Path

from tokenizers.base import BaseTrainer
from tokenizers.figure import FigureTokenizer


class FigureTrainer(BaseTrainer):
    def train(self, file_ext: str = ".figure") -> FigureTokenizer:
        for root, _, files in os.walk(self._corpus_filepath):
            for filepath in files:
                if filepath.endswith(file_ext):
                    fullpath = Path(root) / filepath
                    with open(fullpath) as f:
                        sentence = f.read()
                        self.all_sentences.append(sentence)

        return FigureTokenizer(self.all_sentences)
