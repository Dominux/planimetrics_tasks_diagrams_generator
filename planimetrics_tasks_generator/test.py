from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Iterable, Any

# import pandas as pd
import spacy
import torch
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader, Dataset

from data_loader import DataLoader as TasksDataLoader


# https://www.youtube.com/watch?v=9sHcLvVXsns


PAD_TOKEN = "<PAD>"
UNKNOWN_TOKEN = "<UNK>"
START_TOKEN = "<SOS>"
END_TOKEN = "<EOS>"


spacy_eng = spacy.load("en_core_web_sm")


class Vocabulary:
    def __init__(self, freq_treshold: "int") -> None:
        default_tokens = (PAD_TOKEN, START_TOKEN, END_TOKEN, UNKNOWN_TOKEN)
        self.itos = {i: token for i, token in enumerate(default_tokens)}
        self.stoi = {token: i for i, token in enumerate(default_tokens)}
        self.freq_treshold = freq_treshold

    def __len__(self):
        return len(self.itos)

    @staticmethod
    def tokenizer_eng(text):
        return [tok.text.lower() for tok in spacy_eng.tokenizer(text)]
    
    def build_vocabulary(self, sentence_list: "Iterable[str]"):
        frequencies = defaultdict(int)
        idx = len(self.itos)

        for sentence in sentence_list:
            for word in self.tokenizer_eng(sentence):
                frequencies[word] += 1
            
                if frequencies[word] == self.freq_treshold:
                    self.stoi[word] = idx
                    self.itos[idx] = word
                    idx += 1

    def numericalize(self, text: "str"):
        tokenized_text = self.tokenizer_eng(text)

        return [
            self.stoi[token] if token in self.stoi else self.stoi[UNKNOWN_TOKEN]
            for token in tokenized_text
        ]


class TasksDataset(Dataset):
    def __init__(self, root_dir: "str", corpus_filepath: "Path | str", freq_treshold=5) -> None:
        self.root_dir = root_dir
        self._data = TasksDataLoader(corpus_filepath)
        self.vocab = Vocabulary(freq_treshold)
        self.vocab.build_vocabulary([pair[0] for pair in self._data])

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index: "int"):
        pair = self._data._pairs[index]
        return (self._to_tensor(pair[0]), self._to_tensor(pair[1]))

    def _to_tensor(self, text: "str"):
        numericalized = [
            self.vocab.stoi[START_TOKEN],
            *self.vocab.numericalize(text),
            self.vocab.stoi[START_TOKEN]
        ]
        return torch.tensor(numericalized)


class TasksCollate:
    def __init__(self, pad_idx) -> None:
        self._pad_idx = pad_idx

    def __call__(self, batch: "list[tuple[Any, Any]]"):
        inputs = [pair[0] for pair in batch]
        inputs = pad_sequence(inputs, batch_first=False, padding_value=self._pad_idx)
        outputs = [pair[1] for pair in batch]
        outputs = pad_sequence(outputs, batch_first=False, padding_value=self._pad_idx)

        return inputs, outputs


def get_loader(
    root_dir: "str",
    corpus_filepath: "Path | str",
    batch_size=32,
    num_workers=8,
    shuffle=True,
    pin_memory=True,
):
    dataset = TasksDataset(root_dir, corpus_filepath)
    pad_idx = dataset.vocab.stoi[PAD_TOKEN]
    collate = TasksCollate(pad_idx)
    return DataLoader(
        dataset=dataset, 
        batch_size=batch_size, 
        num_workers=num_workers, 
        shuffle=shuffle, 
        pin_memory=pin_memory, 
        collate_fn=collate,
    )


if __name__ == "__main__":
    dataloader = get_loader("idk", "dataset")
    for idx, (input, output) in enumerate(dataloader):
        print(input.shape)
        print(output.shape)
