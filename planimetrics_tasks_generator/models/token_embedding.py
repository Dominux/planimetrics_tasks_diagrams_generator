import math

import torch


# helper Module to convert tensor of input indices into corresponding tensor of token embeddings
class TokenEmbedding(torch.nn.Module):
    def __init__(self, vocab_size: int, emb_size):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, emb_size)
        self.emb_size = emb_size

    def forward(self, tokens: torch.Tensor):
        return self.embedding(tokens.long()) * math.sqrt(self.emb_size)
