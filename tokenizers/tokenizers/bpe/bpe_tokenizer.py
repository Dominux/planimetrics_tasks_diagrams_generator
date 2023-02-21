from __future__ import annotations
from typing import Iterable

import numpy as np

from tokenizers.base import BaseTokenizer


class BPETokenizer(BaseTokenizer):
    """
    Byte-pair encoding tokenizer
    """

    whitespace_character = "_"

    def __init__(self, vocab: Iterable[str]) -> None:
        self._vocab = {token: i for i, token in enumerate(vocab)}
        self._index2word = {i: token for i, token in enumerate(vocab)}

    def encode(self, text: str) -> Iterable[int]:
        # preparing text
        text = text.replace(" ", self.whitespace_character)

        vector = []

        # current values
        token = ""
        index = None

        # iterating through symbols
        for symbol in text:
            token = f"{token}{symbol}"

            if (new_index := self._vocab.get(token)) is None:
                # there's no such a token
                vector.append(index)

                token = symbol
                index = self._vocab.get(token)

            else:
                # indexing token
                index = new_index

        # saving renamed token
        if token and index:
            vector.append(index)

        return np.array(vector)

    def decode(self, vector: Iterable[int]) -> str:
        return "".join(
            [
                self._index2word[index].replace(self.whitespace_character, " ")
                for index in vector
            ]
        )
