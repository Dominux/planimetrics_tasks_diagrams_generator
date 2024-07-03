import torch

from math_tasks_generator.base import MathTaskUnit
import math_tasks_generator.math_tasks
from tokenizers.base import BaseTokenizer
from tokenizers.constants import SPECIAL_TOKENS, START_IDX, END_IDX


TASKS_NUMBERS = [str(t._math_task._task_number) for t in MathTaskUnit.__subclasses__()]
DEFAULT_VOCAB = [*SPECIAL_TOKENS, *TASKS_NUMBERS]


class TargetTokenizer(BaseTokenizer):
    index2word = DEFAULT_VOCAB
    word2index = {s: i for i, s in enumerate(DEFAULT_VOCAB)}

    def __len__(self) -> int:
        return len(self.index2word)
    
    def encode(self, text: str):
        return torch.tensor((START_IDX, self.word2index[text], END_IDX))

    def decode_index(self, index: int) -> str:
        return self.index2word[index]
