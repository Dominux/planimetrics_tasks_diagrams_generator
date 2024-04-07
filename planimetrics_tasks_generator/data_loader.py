import os
from pathlib import Path
from typing import List


class DataLoader:
    _txt_file_path = ".txt"
    _figure_file_path = ".figure"

    def __init__(self, corpus_filepath: Path | str) -> None:
        self._pairs = self._load(corpus_filepath)

    def __iter__(self):
        return iter(self._pairs)

    @classmethod
    def _load(cls, corpus_filepath: Path | str) -> List[tuple[str, str]]:
        pairs = []

        for root, _, files in os.walk(corpus_filepath):
            if not files:
                continue

            for filepath in files:
                fullpath = Path(root) / filepath
                with open(fullpath) as f:
                    if filepath.endswith(cls._txt_file_path):
                        txt_sentence = f.read()
                    else:
                        figure_sentence = f.read()

            pair = (txt_sentence, figure_sentence)
            pairs.append(pair)

        return pairs

