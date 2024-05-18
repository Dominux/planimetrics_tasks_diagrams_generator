import copy
from pathlib import Path
from typing import TYPE_CHECKING

from settings import BATCH_SIZE
from tokenizers.bpe.bpe_trainer import BPETrainer
from tokenizers.constants import END_TOKEN, PAD_IDX, START_TOKEN
if TYPE_CHECKING:
    from typing import Any

# import pandas as pd
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader, Dataset


# https://www.youtube.com/watch?v=9sHcLvVXsns


class TasksDataset(Dataset):
    def __init__(self, corpus_filepath: "Path | str", freq_treshold=1) -> None:
        self.src_tokenizer = BPETrainer(corpus_filepath).train()
        self.tgt_tokenizer = BPETrainer(corpus_filepath).train(file_ext=".figure")

    def __len__(self):
        return len(self.src_tokenizer.all_sentences)

    def __getitem__(self, index: "int"):
        src = self.src_tokenizer.all_sentences[index]
        tgt = self.tgt_tokenizer.all_sentences[index]

        return (self.src_tokenizer.encode(src), self.tgt_tokenizer.encode(tgt))
    
    def from_indeces(self, indeces: "list[int]") -> str:
        return self.tgt_tokenizer.decode(indeces).replace(START_TOKEN, "").replace(END_TOKEN, "")
    
    def divide(self, fraction: "float") -> "tuple[TasksDataset, TasksDataset]":
        new_dataset = copy.deepcopy(self)

        new_dataset.src_tokenizer.index2word = self.src_tokenizer.index2word
        new_dataset.src_tokenizer.word2index = self.src_tokenizer.word2index
        new_dataset.tgt_tokenizer.index2word = self.tgt_tokenizer.index2word
        new_dataset.tgt_tokenizer.word2index = self.tgt_tokenizer.word2index

        point = round(len(self) * fraction)

        new_dataset.src_tokenizer.all_sentences = self.src_tokenizer.all_sentences[:point]
        self.src_tokenizer.all_sentences = self.src_tokenizer.all_sentences[point:]
        new_dataset.tgt_tokenizer.all_sentences = self.tgt_tokenizer.all_sentences[:point]
        self.tgt_tokenizer.all_sentences = self.tgt_tokenizer.all_sentences[point:]
        
        return (self, new_dataset)


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
    dataset: TasksDataset,
    batch_size=BATCH_SIZE,
    num_workers=8,
    shuffle=True,
    pin_memory=True,
):
    collate = TasksCollate(PAD_IDX)
    return DataLoader(
        dataset=dataset, 
        batch_size=batch_size, 
        num_workers=num_workers, 
        shuffle=shuffle, 
        pin_memory=pin_memory, 
        collate_fn=collate,
    )
