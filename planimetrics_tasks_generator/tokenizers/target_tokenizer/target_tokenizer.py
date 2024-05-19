import string
import typing as t

import torch

from tokenizers.base import BaseTokenizer
from tokenizers.constants import END_TOKEN, SPECIAL_TOKENS, START_TOKEN, SUBSCRIPT_NUMBERS
from tokenizers.target_tokenizer.figure_kind import FigureKind


DEFAULT_VOCAB = [
    *SPECIAL_TOKENS,
    *string.ascii_lowercase,
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
            [self.word2index[s] for s in self.clear_tgt(text)]
        )

    def decode_index(self, index: int) -> str:
        return self.index2word[index]
    
    def from_indeces(self, indeces: "t.Iterable[int]") -> str:
        return self.decode(indeces).replace(START_TOKEN, "").replace(END_TOKEN, "")
    
    @classmethod
    def clear_tgt(cls, tgt: str) -> str:
        return tgt.lower()
