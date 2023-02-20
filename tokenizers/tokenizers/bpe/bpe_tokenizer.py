from __future__ import annotations

from dataclasses import dataclass

from tokenizers.base import BaseTokenizer, RawVocabType


class BPETokenizer(BaseTokenizer):
    """
    Byte-pair encoding tokenizer

    NOTE: Internal datatype is optimized to perform encoding, but not to decode,
    so decoding will take more time/power
    """

    def __init__(self, vocab: RawVocabType) -> None:
        self._vocab = Vocab.build_vocab(vocab)

    def encode(self, text: str) -> str:
        ...

    def decode(self, vector: str) -> str:
        ...


@dataclass
class VocabItem:
    freequency: int
    index: int


class Vocab(dict[str, VocabItem]):
    @staticmethod
    def build_vocab(vocab: RawVocabType) -> Vocab:
        return Vocab(
            {
                word: VocabItem(freequency, index)
                for index, (word, freequency) in enumerate(
                    sorted(vocab.items(), key=lambda item: item[1], reverse=True)
                )
            }
        )
