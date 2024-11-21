import string

import torch

from tokenizers.base import BaseTokenizer
from tokenizers.constants import SPECIAL_TOKENS, START_IDX, END_IDX


FIGURE_TOKENS = (
    'triangle',
    'quadrilateral',
    'parallelogram',
    'trapezoid',
    'square',
)
JSON_TOKENS = (
    '"',
    '[',
    ']',
    '{',
    '}',
    ':',
    ',',
)
DEFAULT_VOCAB = (
    *SPECIAL_TOKENS,
    *FIGURE_TOKENS,
    *JSON_TOKENS,
    *string.ascii_lowercase,
    ' ',
)


class TargetTokenizer(BaseTokenizer):
    index2word = DEFAULT_VOCAB
    word2index = {s: i for i, s in enumerate(DEFAULT_VOCAB)}

    def __len__(self) -> int:
        return len(self.index2word)

    def encode(self, text: str):
        """Kinda tricky way"""
        text = self.clear(text)

        vector = []
        i = 0
        while i < len(text):
            to_continue = False
            reminder = text[i:]

            for fig_word in FIGURE_TOKENS:
                if reminder.startswith(fig_word):

                    index = self.word2index[fig_word]
                    vector.append(index)
                    i += len(fig_word)

                    to_continue = True
                    break

            if to_continue:
                continue

            symbol = text[i]
            index = self.word2index[symbol]
            vector.append(index)
            i += 1

        return torch.tensor((START_IDX, *vector, END_IDX))


    def decode_index(self, index: int) -> str:
        return self.index2word[index]

    @classmethod
    def clear(cls, tgt: str) -> str:
        return tgt.lower()
