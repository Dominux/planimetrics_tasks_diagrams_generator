from string import ascii_uppercase

from tokenizers.base import BaseTokenizer
from tokenizers.constants import EOS_TOKEN, SOS_TOKEN


_VOCAB = f"{SOS_TOKEN}{EOS_TOKEN}{ascii_uppercase}"


class FigureTokenizer(BaseTokenizer):
    _SYMBOL_TO_INDEX_VOCAB = {s: i for i, s in enumerate(_VOCAB)}

    vocab_amount = len(ascii_uppercase)

    def __init__(self, all_sentences: list[str]) -> None:
        self.all_sentences = all_sentences

    def encode(self, text: str) -> list[int]:
        return [self._SYMBOL_TO_INDEX_VOCAB[s] for s in text]

    def decode_index(self, index: int) -> str:
        return _VOCAB[index]
