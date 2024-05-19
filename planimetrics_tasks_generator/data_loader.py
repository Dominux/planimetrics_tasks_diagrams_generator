import typing as t

from settings import BATCH_SIZE
from tokenizers.constants import END_TOKEN, PAD_IDX, START_TOKEN
if t.TYPE_CHECKING:
    from tokenizers import SourceTokenizer, TargetTokenizer
    from data_provider import DataProvider

from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader, Dataset


# https://www.youtube.com/watch?v=9sHcLvVXsns


class TasksDataset(Dataset):
    def __init__(
        self,
        data_provider: "DataProvider", 
        src_tokenizer: "SourceTokenizer", 
        tgt_tokenizer: "TargetTokenizer"
    ) -> None:
        self._data_provider = data_provider
        self._src_tokenizer = src_tokenizer
        self._tgt_tokenizer = tgt_tokenizer

    def __len__(self):
        return len(self._data_provider)

    def __getitem__(self, index: "int"):
        return self._data_provider[index]
    
    def from_indeces(self, indeces: "t.Iterable[int]") -> str:
        return self._tgt_tokenizer.decode(indeces).replace(START_TOKEN, "").replace(END_TOKEN, "")


def collate(batch: "list[tuple[t.Any, t.Any]]"):
    inputs = [pair[0] for pair in batch]
    inputs = pad_sequence(inputs, batch_first=False, padding_value=PAD_IDX)
    outputs = [pair[1] for pair in batch]
    outputs = pad_sequence(outputs, batch_first=False, padding_value=PAD_IDX)

    return inputs, outputs


def get_loader(
    dataset: "TasksDataset",
    batch_size=BATCH_SIZE,
    num_workers=8,
    shuffle=True,
    pin_memory=True,
):
    return DataLoader(
        dataset=dataset, 
        batch_size=batch_size, 
        num_workers=num_workers, 
        shuffle=shuffle, 
        pin_memory=pin_memory, 
        collate_fn=collate,
    )
