import string

from tokenizers.base import BaseTokenizer
from tokenizers.constants import SPECIAL_TOKENS, SUBSCRIPT_NUMBERS
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

    def encode(self, text: str) -> list[int]:
        return [self.word2index[s] for s in text]

    def decode_index(self, index: int) -> str:
        return self.index2word[index]
