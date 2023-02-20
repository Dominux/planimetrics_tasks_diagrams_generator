import re
from collections import Counter, defaultdict

from tokenizers.base import BaseTrainer, VocabType
from tokenizers.bpe.bpe_tokenizer import BPETokenizer


class BPETrainer(BaseTrainer):
    """
    Class to train a Byte-pair encoding

    After train it returns a class to encode/decode text to/from vector via BPE

    OOP enterprise adaptation of the script:
    https://gist.github.com/akashjaswal/ba302b943dfb4e56ace0d5761d01b9cf#file-bpe-py
    """

    def train(self) -> BPETokenizer:
        # reading corpus file
        with self._corpus_filepath.open() as f:
            corpus = f.read()

        vocab = self.build_vocab(corpus)  # Step 1

        num_merges = 50  # Hyperparameter
        for _ in range(num_merges):
            pairs = self.get_stats(vocab)  # Step 2

            if not pairs:
                break

            # step 3
            best = max(pairs, key=pairs.get)  # type: ignore
            vocab = self.merge_vocab(best, vocab)

        return BPETokenizer(vocab)

    @staticmethod
    def build_vocab(corpus: str) -> VocabType:
        """Step 1. Build vocab from text corpus"""

        # Separate each char in word by space and add mark end of token
        tokens = [" ".join(word) + " </w>" for word in corpus.split()]

        # Count frequency of tokens in corpus
        vocab = Counter(tokens)

        return vocab

    @staticmethod
    def get_stats(vocab: VocabType) -> VocabType:
        """Step 2. Get counts of pairs of consecutive symbols"""

        pairs = defaultdict(int)
        for word, frequency in vocab.items():
            symbols = word.split()

            # Counting up occurrences of pairs
            for i in range(len(symbols) - 1):
                pairs[symbols[i], symbols[i + 1]] += frequency

        return pairs

    @staticmethod
    def merge_vocab(pair: tuple, v_in: VocabType) -> VocabType:
        """Step 3. Merge all occurrences of the most frequent pair"""

        v_out = {}
        bigram = re.escape(" ".join(pair))
        p = re.compile(r"(?<!\S)" + bigram + r"(?!\S)")

        for word in v_in:
            # replace most frequent pair in all vocabulary
            w_out = p.sub("".join(pair), word)
            v_out[w_out] = v_in[word]

        return v_out
