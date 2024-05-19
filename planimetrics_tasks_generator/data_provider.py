from __future__ import annotations

import os
from pathlib import Path


class DataProvider:
    _src_ext = ".txt"
    _tgt_ext = ".figure"

    def __init__(self, pairs: "list[tuple[str, str]]"):
        self._pairs = pairs

    def __len__(self):
        return len(self._pairs)
    
    def __getitem__(self, index: "int"):
        return self._pairs[index]
    
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
