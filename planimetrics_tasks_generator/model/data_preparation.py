import torch

from tokenizers.constants import EOS_TOKEN
from tokenizers.base import BaseTokenizer
from model.constants import DEVICE


def tensor_from_sentence(tokenizer: BaseTokenizer, sentence: str) -> torch.Tensor:
    text = f"{sentence}{EOS_TOKEN}"
    indexes = tokenizer.encode(text)
    return torch.tensor(indexes, dtype=torch.long, device=DEVICE).view(-1, 1)


def tensors_from_pair(
    pair: tuple[str, str], tokenizers: tuple[BaseTokenizer, BaseTokenizer]
) -> tuple[torch.Tensor, torch.Tensor]:
    input_tensor = tensor_from_sentence(tokenizers[0], pair[0])
    output_tensor = tensor_from_sentence(tokenizers[1], pair[1])
    return (input_tensor, output_tensor)
