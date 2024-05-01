from pathlib import Path

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


class Vocabulary:
    def __init__(self, freq_treshold) -> None:
        default_tokens = (PAD_TOKEN, START_TOKEN, END_TOKEN, UNKNOWN_TOKEN)
        self.itos = {i: token for i, token in enumerate(default_tokens)}
        self.stoi = {token: i for i, token in enumerate(default_tokens)}
        self.freq_treshold = freq_treshold

    def __len__(self):
        return len(self.itos)

    @staticmethod
    def tokenizer_eng(text):
        ...        


class TasksDataset(Dataset):
    def __init__(self, root_dir: str, corpus_filepath: Path | str, freq_treshold=5) -> None:
        self.root_dir = root_dir
        self._data = TasksDataLoader(corpus_filepath)
        self.vocab = Vocabulary(freq_treshold)
        # self.vocab.build_vocabulary(self.)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        pair = self._data._pairs[index]
        return (self._to_tensor(pair[0]), self._to_tensor(pair[1]))

    def _to_tensor(self, text: str):
        numericalized = [
            self.vocab.stoi[START_TOKEN],
            *self.vocab.numericalize(),
            self.vocab.stoi[START_TOKEN]
        ]
        return torch.tensor(numericalized)

