from pathlib import Path
from typing import Iterable, List

from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator

from math_tasks_generator import generator as dataset_generator
from data_loader import DataLoader


# https://pytorch.org/tutorials/beginner/translation_transformer.html


SRC_LANGUAGE = 'de'
TGT_LANGUAGE = 'en'
LANGUAGE_INDEX = {SRC_LANGUAGE: 0, TGT_LANGUAGE: 1}

# Define special symbols and indices
UNK_IDX, PAD_IDX, BOS_IDX, EOS_IDX = 0, 1, 2, 3
# Make sure the tokens are in order of their indices to properly insert them in vocab
special_symbols = ['<unk>', '<pad>', '<bos>', '<eos>']

def generate_dataset() -> Path:
    dataset_generator.MainGenerator().generate()
    return dataset_generator.MainGenerator.path

# helper function to yield list of tokens
def yield_tokens(data_iter: Iterable[tuple[str, str]], language: str):
    for data_sample in data_iter:
        yield data_sample[LANGUAGE_INDEX[language]]

def main():
    dataset_path = generate_dataset()
    data_loader = DataLoader(dataset_path)
    vocab_transform = {}

    for ln in (SRC_LANGUAGE, TGT_LANGUAGE):
        # Create torchtext's Vocab object
        vocab_transform[ln] = build_vocab_from_iterator(
            yield_tokens(data_loader, ln),
            min_freq=1,
            specials=special_symbols,
            special_first=True
        )

    # Set ``UNK_IDX`` as the default index. This index is returned when the token is not found.
    # If not set, it throws ``RuntimeError`` when the queried token is not found in the Vocabulary.
    for ln in (SRC_LANGUAGE, TGT_LANGUAGE):
        vocab_transform[ln].set_default_index(UNK_IDX)


if __name__ == "__main__":
    main()
