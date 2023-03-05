import random
import torch

from tokenizers.base import BaseTokenizer
from tokenizers.constants import EOS_TOKEN, SOS_TOKEN
from model.constants import DEVICE, MAX_LENGTH
from model.data_preparation import tensor_from_sentence


def evaluate(
    encoder,
    decoder,
    sentence: str,
    tokenizers: tuple[BaseTokenizer, BaseTokenizer],
    max_length=MAX_LENGTH,
):
    with torch.no_grad():
        input_tensor = tensor_from_sentence(tokenizers[0], sentence)
        input_length = input_tensor.size()[0]
        encoder_hidden = encoder.initHidden()

        encoder_outputs = torch.zeros(max_length, encoder.hidden_size, device=DEVICE)

        for ei in range(input_length):
            encoder_output, encoder_hidden = encoder(input_tensor[ei], encoder_hidden)
            encoder_outputs[ei] += encoder_output[0, 0]

        decoder_input = torch.tensor([[SOS_TOKEN]], device=DEVICE)  # SOS

        decoder_hidden = encoder_hidden

        decoded_words = []
        decoder_attentions = torch.zeros(max_length, max_length)

        for di in range(max_length):
            decoder_output, decoder_hidden, decoder_attention = decoder(
                decoder_input, decoder_hidden, encoder_outputs
            )
            decoder_attentions[di] = decoder_attention.data
            _topv, topi = decoder_output.data.topk(1)
            if topi.item() == EOS_TOKEN:
                decoded_words.append("<EOS>")
                break
            else:
                decoded_words.append(tokenizers[1].decode(topi.item()))

            decoder_input = topi.squeeze().detach()

        return decoded_words, decoder_attentions[: di + 1]


def evaluate_randomly(
    encoder,
    decoder,
    tokenizers: tuple[BaseTokenizer, BaseTokenizer],
    pairs: list[tuple[str, str]],
    n=10,
):
    for i in range(n):
        pair = random.choice(pairs)
        print(">", pair[0])
        print("=", pair[1])
        output_words, attentions = evaluate(
            encoder, decoder, pair[0], tokenizers=tokenizers
        )
        output_sentence = " ".join(output_words)
        print("<", output_sentence)
        print("")
