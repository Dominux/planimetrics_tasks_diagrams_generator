from __future__ import annotations

from tokenizers.base import BaseTokenizer


class BPETokenizer(BaseTokenizer):
    """
    Byte-pair encoding tokenizer
    """

    def __init__(self, vocab: set[str]) -> None:
        self._vocab = vocab

    def encode(self, text: str) -> str:
        ...

    def decode(self, vector: str) -> str:
        ...
