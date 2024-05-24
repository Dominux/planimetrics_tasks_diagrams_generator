import typing as t

import torch

from models.constants import DEVICE
from settings import EMB_SIZE
from tokenizers.constants import END_IDX, PAD_IDX, START_IDX

if t.TYPE_CHECKING:
    from torch.utils.data import DataLoader

    from data_provider import DataProvider
    from data_loader import TasksDataset
    from tokenizers import SourceTokenizer, TargetTokenizer


def generate_square_subsequent_mask(sz):
    mask = (torch.triu(torch.ones((sz, sz), device=DEVICE)) == 1).transpose(0, 1)
    mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
    return mask

def create_mask(src, tgt):
    src_seq_len = src.shape[0]
    tgt_seq_len = tgt.shape[0]

    tgt_mask = generate_square_subsequent_mask(tgt_seq_len)
    src_mask = torch.zeros((src_seq_len, src_seq_len),device=DEVICE).type(torch.bool)

    src_padding_mask = (src == PAD_IDX).transpose(0, 1)
    tgt_padding_mask = (tgt == PAD_IDX).transpose(0, 1)
    return src_mask, tgt_mask, src_padding_mask, tgt_padding_mask

def train_epoch(model: "torch.nn.Module", loss_fn, optimizer, dataloader: "DataLoader"):
    model.train()
    losses = 0

    for src, tgt in dataloader:
        src = src.to(DEVICE)
        tgt = tgt.to(DEVICE)

        tgt_input = tgt[:-1, :]

        src_mask, tgt_mask, src_padding_mask, tgt_padding_mask = create_mask(src, tgt_input)

        logits = model(
            src, 
            tgt_input, 
            src_mask, 
            tgt_mask,
            src_padding_mask, 
            tgt_padding_mask, 
            src_padding_mask
        )

        optimizer.zero_grad()

        tgt_out = tgt[1:, :]
        loss = loss_fn(logits.reshape(-1, logits.shape[-1]), tgt_out.reshape(-1))
        loss.backward()

        optimizer.step()
        losses += loss.item()

    return losses / len(dataloader)

def validate(model, loss_fn, dataloader: "DataLoader"):
    model.eval()
    losses = 0

    for src, tgt in dataloader:
        src = src.to(DEVICE)
        tgt = tgt.to(DEVICE)

        tgt_input = tgt[:-1, :]

        src_mask, tgt_mask, src_padding_mask, tgt_padding_mask = create_mask(src, tgt_input)

        logits = model(
            src, 
            tgt_input, 
            src_mask, 
            tgt_mask,
            src_padding_mask, 
            tgt_padding_mask, 
            src_padding_mask
        )

        tgt_out = tgt[1:, :]
        loss = loss_fn(logits.reshape(-1, logits.shape[-1]), tgt_out.reshape(-1))
        losses += loss.item()

    return losses / len(dataloader)

# function to generate output sequence using greedy algorithm
def greedy_decode(model, src, src_mask, start_symbol):
    src = src.to(DEVICE)
    src_mask = src_mask.to(DEVICE)

    memory = model.encode(src, src_mask)
    ys = torch.ones(1, 1).fill_(start_symbol).type(torch.long).to(DEVICE)
    for _ in range(EMB_SIZE):
        memory = memory.to(DEVICE)
        tgt_mask = generate_square_subsequent_mask(ys.size(0)).type(torch.bool).to(DEVICE)
        out = model.decode(ys, memory, tgt_mask)
        out = out.transpose(0, 1)
        prob = model.generator(out[:, -1])
        _, next_word = torch.max(prob, dim=1)
        next_word = next_word.item()

        ys = torch.cat(
            [
                ys,
                torch.ones(1, 1).type_as(src.data).fill_(next_word)
            ], 
            dim=0
        )
        if next_word == END_IDX:
            break

    return ys

# actual function to translate input sentence into target language
def translate(
    model: "torch.nn.Module",
    src_sentence: "str", 
    src_tokenizer: "SourceTokenizer",
    tgt_tokenizer: "TargetTokenizer"
):
    model.eval()
    src = src_tokenizer.encode(src_sentence).view(-1, 1)
    num_tokens = src.shape[0]
    src_mask = torch.zeros(num_tokens, num_tokens).type(torch.bool)
    tgt_tokens = greedy_decode(
        model, 
        src, 
        src_mask,
        start_symbol=START_IDX
    ).flatten()
    return tgt_tokenizer.decode(tgt_tokens.cpu().numpy())

def evaluate(
    model, 
    dataset: "TasksDataset", 
    data_provider: "DataProvider",
    src_tokenizer: "SourceTokenizer",
    tgt_tokenizer: "TargetTokenizer" 
):
    right_translations_counter = 0

    for i in range(len(dataset)):
        src, tgt = data_provider[i]
        expected = tgt_tokenizer.clear(tgt)
       
        if translate(model, src, src_tokenizer, tgt_tokenizer) == expected:
            right_translations_counter += 1
    
    return right_translations_counter
