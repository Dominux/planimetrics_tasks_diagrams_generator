import string
import typing as t

import torch

from tokenizers.base import BaseTokenizer
from tokenizers.constants import END_IDX, SPECIAL_TOKENS, START_IDX, SUBSCRIPT_NUMBERS
from tokenizers.target_tokenizer.figure_kind import FigureKind


DEFAULT_VOCAB = [
    *SPECIAL_TOKENS,
    *string.ascii_lowercase,
    *string.ascii_uppercase,
    *string.whitespace,
    *SUBSCRIPT_NUMBERS,
    *FigureKind.names()
]

class TargetTokenizer(BaseTokenizer):
    index2word = DEFAULT_VOCAB
    word2index = {s: i for i, s in enumerate(DEFAULT_VOCAB)}

    def __len__(self) -> int:
        return len(self.index2word)

    def encode(self, text: str):
        return torch.tensor(
            (
                START_IDX,
                *[self.word2index[s] for s in self.clear(text)],
                END_IDX
            )
        )

    def decode_index(self, index: int) -> str:
        return self.index2word[index]
    
    def decode(self, vector: "t.Iterable[int]") -> str:
        return super().decode(vector).upper()
    
    @classmethod
    def clear(cls, tgt: str) -> str:
        return tgt.lower()
