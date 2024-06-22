import os
from pathlib import Path
import random
import re
import typing as t
if t.TYPE_CHECKING:
    from typing_extensions import Self

from math_tasks_generator.helpers.functions import get_random_letters


class DataProvider:
    _src_ext = ".txt"
    _tgt_ext = ".figure"

    def __init__(self, pairs: "list[tuple[str, str]]", shuffle: "bool" = True):
        self._pairs = pairs
        if shuffle:
            random.shuffle(self._pairs)

    def __len__(self):
        return len(self._pairs)
    
    def __getitem__(self, index: "int"):
        return self._pairs[index]
    
    def iter_src(self):
        return (pair[0] for pair in self._pairs)
    
    @classmethod
    def build(cls, corpus_filepath: "Path | str") -> "Self":
        pairs = []

        # reading corpus files
        for root, _, files in os.walk(corpus_filepath):
            if not files:
                continue

            for filepath in files:
                fullpath = Path(root) / filepath
                with open(fullpath) as f:
                    if filepath.endswith(cls._src_ext):
                        src_sentence = f.read()
                    else:
                        tgt_sentence = f.read()

            pair = (src_sentence, tgt_sentence)
            pairs.append(pair)

        return cls(pairs)

    def train_val_test(
        self, val_fraction: "float", test_fraction: "float" 
    ) -> "tuple[Self, Self, Self]":
        """Divides the original dataprovider onto train, validation and test ones"""

        fractions_sum = val_fraction + test_fraction
        assert fractions_sum < 1, "Sum of `val_fraction` and`test_fraction` must be less than 1"

        val_point = round(len(self) * val_fraction)
        test_point = round(len(self) * fractions_sum)

        val_data = self.__class__(self._pairs[:val_point], shuffle=False)
        test_data = self.__class__(self._pairs[val_point : test_point], shuffle=False)
        self._pairs = self._pairs[test_point:]

        return self, val_data, test_data


class TrianglesTasksDataProvider(DataProvider):
    @classmethod
    def build(cls, corpus_filepath: Path | str) -> "Self":
        if isinstance(corpus_filepath, str):
            corpus_filepath = Path(corpus_filepath)

        pairs = []

        regex = re.compile(r"[A-Z]{3}")

        with corpus_filepath.open() as f:
            for i, line in enumerate(f):
                triangle_match = re.search(regex, line)
                assert triangle_match, f'Row {i}, line: "{line:.20}..."'
                pairs.append((line, triangle_match[0]))

        return cls(pairs)

    def augment_data(self, factor: int = 5):
        # Actually, the data isn't clear, it contains a lot of common triangle names
        # Therefore it needs to be replaced with arbitrary names
        new_pairs = []

        for pair in self._pairs:
            for _ in range(factor):
                random_triangle_name = "".join(get_random_letters(3))
                new_task_text = pair[0].replace(pair[1], random_triangle_name)
                new_pairs.append((new_task_text, random_triangle_name))

        self._pairs = new_pairs
