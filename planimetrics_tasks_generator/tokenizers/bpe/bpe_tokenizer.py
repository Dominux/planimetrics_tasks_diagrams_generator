from __future__ import annotations

from typing import Iterable

import torch

from tokenizers.base import BaseTokenizer
from tokenizers.constants import DEFAULT_TOKENS, END_IDX, START_IDX
from tokenizers.helpers import swap_2_elements_in_list


class BPETokenizer(BaseTokenizer):
    """
    Byte-pair encoding tokenizer
    """

    whitespace_character = "🕳"

    def __init__(self, vocab: Iterable[str], all_sentences: list[str]) -> None:
        # Changing vocab a bit
        vocab = list(vocab)
        for i, token in enumerate(DEFAULT_TOKENS):
            swap_2_elements_in_list(vocab, token, i)

        self.word2index = {token: i for i, token in enumerate(vocab)}
        self.index2word = {i: token for i, token in enumerate(vocab)}

        self.all_sentences = all_sentences
        self.vocab_amount = len(vocab)  # type: ignore

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
