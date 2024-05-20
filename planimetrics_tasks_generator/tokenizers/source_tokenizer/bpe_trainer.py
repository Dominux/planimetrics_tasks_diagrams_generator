import re
from typing import TYPE_CHECKING
from collections import Counter, defaultdict

from tokenizers.constants import START_TOKEN, END_TOKEN
from tokenizers.source_tokenizer.source_tokenizer import SourceTokenizer

if TYPE_CHECKING:
    import typing as t


class BPETrainer:
    """
    Class to train a Byte-pair encoding tokenizer

    After train it returns a class to encode/decode text to/from vector via BPE
    """

    def train(
        self, sentences: "t.Iterable[str]", iterations_amount: int = 50
    ) -> "SourceTokenizer":
        corpus = self._construct_corpus(sentences)
        corpus_repr = self._build_corpus_repr(corpus)
        vocab = self._build_vocab(corpus)  # Step 1

        for _ in range(iterations_amount):
            pairs = self.get_stats(corpus_repr)  # Step 2

            if not pairs:
                break

            # step 3
            best = max(pairs, key=pairs.get)  # type: ignore
            corpus_repr = self.update_corpus(best, corpus_repr)

            # step 4
            vocab = self.update_vocab(vocab, pairs=pairs.keys())  # type: ignore

        return SourceTokenizer(vocab.keys())

    def _construct_corpus(self, sentences: "t.Iterable[str]") -> str:
        return "\n".join(f"{START_TOKEN}{sentence}{END_TOKEN}" for sentence in sentences)

    @classmethod
    def _build_vocab(cls, corpus: str) -> dict[str, None]:
        return {symbol: None for symbol in SourceTokenizer.clear(corpus)}

    @staticmethod
    def _build_corpus_repr(corpus: str):
        # Separate each char in word by space and add mark end of token
        tokens = [START_TOKEN, END_TOKEN]

        tokens.extend(
            (
                " ".join(f"{word}{SourceTokenizer.whitespace_character}")
                for word in corpus.split()
            )
        )

        # Count frequency of tokens in corpus
        return Counter(tokens)

    @staticmethod
    def get_stats(corpus_repr):
        pairs = defaultdict(int)
        for word, frequency in corpus_repr.items():
            symbols = word.split()

            # Counting up occurrences of pairs
            for i in range(len(symbols) - 1):
                pairs[symbols[i], symbols[i + 1]] += frequency

        return pairs

    @staticmethod
    def update_corpus(pair: tuple, v_in):
        v_out = {}

        bigram = re.escape(" ".join(pair))
        p = re.compile(r"(?<!\S)" + bigram + r"(?!\S)")

        for word in v_in:
            # replace most frequent pair in all vocabulary
            w_out = p.sub("".join(pair), word)
            v_out[w_out] = v_in[word]

        return v_out

    @staticmethod
    def update_vocab(
        vocab: dict[str, None], pairs: list[tuple[str, str]]
    ) -> dict[str, None]:
        united_pairs = {"".join(pair): None for pair in pairs}
        vocab.update(united_pairs)

        return vocab
