from tokenizers.base import BaseTokenizer


class BPETokenizer(BaseTokenizer):
    """
    Byte-pair encoding tokenizer
    """

    def encode(self, text: str) -> str:
        ...

    def decode(self, vector: str) -> str:
        ...
