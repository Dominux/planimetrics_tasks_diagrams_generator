from __future__ import annotations

from typing import Iterable

from tokenizers.base import BaseTokenizer


class BPETokenizer(BaseTokenizer):
    """
    Byte-pair encoding tokenizer
    """

    whitespace_character = "_"

    def __init__(self, vocab: Iterable[str], all_sentences: list[str]) -> None:
        self.word2index = {token: i for i, token in enumerate(vocab)}
        self.index2word = {i: token for i, token in enumerate(vocab)}

        self.all_sentences = all_sentences
        vocab_amount = len(vocab)  # type: ignore

    def encode(self, text: str) -> list[int]:
        # preparing text
        text = text.replace(" ", self.whitespace_character).lower()

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
        if token and index:
            vector.append(index)

        return vector

    def decode(self, vector: Iterable[int]) -> str:
        return "".join(
            [
                self.index2word[index].replace(self.whitespace_character, " ")
                for index in vector
            ]
        )
