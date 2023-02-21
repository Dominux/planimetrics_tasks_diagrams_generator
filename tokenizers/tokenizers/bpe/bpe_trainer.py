import os
from pathlib import Path
import re
from collections import Counter, defaultdict

from tokenizers.base import BaseTrainer, CorpusReprType
from tokenizers.bpe.bpe_tokenizer import BPETokenizer


class BPETrainer(BaseTrainer):
    """
    Class to train a Byte-pair encoding tokenizer

    After train it returns a class to encode/decode text to/from vector via BPE
    """

    _class = BPETokenizer

    def train(
        self, iterations_amount: int = 50, file_ext: str = ".txt"
    ) -> BPETokenizer:
        corpus = self._read_corpus(self._corpus_filepath, file_ext).lower()
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

        return self._class(vocab.keys())

    @staticmethod
    def _read_corpus(basepath: Path, file_ext: str) -> str:
        corpus = ""

        # reading corpus files
        for root, _, files in os.walk(basepath):
            for filepath in files:
                if filepath.endswith(file_ext):
                    fullpath = Path(root) / filepath
                    with open(fullpath) as f:
                        corpus = f"{corpus}\n{f.read()}"

        return corpus

    @staticmethod
    def _build_vocab(corpus: str) -> dict[str, None]:
        return {
            symbol: None
            for symbol in iter(corpus.replace(" ", BPETokenizer.whitespace_character))
        }

    @staticmethod
    def _build_corpus_repr(corpus: str) -> CorpusReprType:
        # Separate each char in word by space and add mark end of token
        tokens = [
            " ".join(f"{word}{BPETokenizer.whitespace_character}")
            for word in corpus.split()
        ]

        # Count frequency of tokens in corpus
        return Counter(tokens)

    @staticmethod
    def get_stats(corpus_repr: CorpusReprType) -> CorpusReprType:
        pairs = defaultdict(int)
        for word, frequency in corpus_repr.items():
            symbols = word.split()

            # Counting up occurrences of pairs
            for i in range(len(symbols) - 1):
                pairs[symbols[i], symbols[i + 1]] += frequency

        return pairs

    @staticmethod
    def update_corpus(pair: tuple, v_in: CorpusReprType) -> CorpusReprType:
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
