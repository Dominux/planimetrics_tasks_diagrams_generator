import os
from copy import deepcopy
import json
import random
from pathlib import Path
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


class TasksDataProvider(DataProvider):
    @classmethod
    def build(cls, corpus_filepath: Path | str) -> "Self":
        if isinstance(corpus_filepath, str):
            corpus_filepath = Path(corpus_filepath)

        pairs = []

        with corpus_filepath.open() as f:
            for i, line in enumerate(f):
                if not i:
                    # skipping first row
                    continue

                line = line.strip() # cleaninng from whitespace sht around the line
                x, y = line.split("\t")
                assert x and y, f'Row {i}, line: "{line:.20}..."'
                pairs.append((x, y))

        return cls(pairs)

    def augment_data(self, factor: int = 5):
        # Actually, the data isn't clear, it contains a lot of common names
        # Therefore it needs to be replaced with arbitrary names
        new_pairs = []

        for x, y in self._pairs:
            y_json = json.loads(y)

            for _ in range(factor):
                new_x = x
                new_y_json = deepcopy(y_json)

                for i, figure in enumerate(y_json):
                    old_name = figure["name"]
                    new_name = "".join(get_random_letters(len(old_name)))
                    new_x = new_x.replace(figure["name"], new_name)
                    new_y_json[i]["name"] = new_name

                new_pairs.append((new_x, json.dumps(new_y_json)))

        self._pairs = new_pairs
