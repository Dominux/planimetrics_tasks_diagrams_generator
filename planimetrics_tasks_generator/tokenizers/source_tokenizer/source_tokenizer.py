from __future__ import annotations

import string
from typing import Iterable

import torch

from tokenizers.base import BaseTokenizer
from tokenizers.constants import SPECIAL_TOKENS, END_IDX, START_IDX, SUBSCRIPT_NUMBERS
from tokenizers.helpers import swap_2_elements_in_list


RUSSIAN_ALPHABET = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
DEFAULT_VOCAB = [
    *string.ascii_lowercase,
    *string.digits,
    *string.whitespace, 
    *string.punctuation,
    *RUSSIAN_ALPHABET,
    *SUBSCRIPT_NUMBERS,
]
INITIAL_VOCAB = [*SPECIAL_TOKENS, *DEFAULT_VOCAB]


class SourceTokenizer(BaseTokenizer):
    """
    Byte-pair encoding tokenizer

    #### WARNING: 
    This tokenizer is not lossless

    For a better translation of cases where "е" is used instead of "ё",
    this tokenizer replaces one with another during its encoding process.
    Therefore it leads to losing originallity
    """

    whitespace_character = "🕳"

    def __len__(self) -> int:
        return len(self.index2word)

    def __init__(self, vocab: Iterable[str]) -> None:
        # Changing vocab a bit
        vocab = list(vocab)
        for i, token in enumerate(INITIAL_VOCAB):
            swap_2_elements_in_list(vocab, token, i)

        self.word2index = {token: i for i, token in enumerate(vocab)}
        self.index2word = vocab

    def encode(self, text: str):
        # preparing text
        text = text.replace(" ", self.whitespace_character)

        vector = []

        # current values
        token = ""
        index = None

        # iterating through symbols
        for symbol in text:
            token = f"{token}{symbol}"

            if (new_index := self.word2index.get(token)) is None:
                # there's no such a token
                vector.append(index)

                token = symbol
                index = self.word2index.get(token)

            else:
                # indexing token
                index = new_index

        # saving renamed token
        if token and index is not None:
            vector.append(index)

        vector = [
            START_IDX,
            *vector,
            END_IDX
        ]
        return torch.tensor(vector)

    def decode_index(self, index: int) -> str:
        return self.index2word[index].replace(self.whitespace_character, " ")
