from __future__ import annotations

import os
from pathlib import Path
import random


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
    
    def iter_tgt(self):
        return (pair[1] for pair in self._pairs)
    
    @classmethod
    def build(cls, corpus_filepath: "Path | str") -> "DataProvider":
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
    ) -> "tuple[DataProvider, DataProvider, DataProvider]":
        """Divides the original dataprovider onto train, validation and test ones"""

        fractions_sum = val_fraction + test_fraction
        assert fractions_sum < 1, "Sum of `val_fraction` and`test_fraction` must be less than 1"

        val_point = round(len(self) * val_fraction)
        test_point = round(len(self) * fractions_sum)

        val_data = DataProvider(self._pairs[val_point:], shuffle=False)
        test_data = DataProvider(self._pairs[val_point : test_point], shuffle=False)
        self._pairs = self._pairs[:test_point]

        return self, val_data, test_data
