from pathlib import Path

from model.constants import DEVICE
from model.decoders import EncoderRNN, AttnDecoderRNN
from model.train import train_iters
from model.evaluation import evaluate_randomly
from tokenizers.base import BaseTokenizer
from tokenizers.bpe import BPETrainer
from math_tasks_generator import generator as dataset_generator
from tokenizers.constants import SOS_TOKEN, EOS_TOKEN
from tokenizers.figure.figure_trainer import FigureTrainer


def generate_dataset() -> Path:
    dataset_generator.MainGenerator().generate()
    return dataset_generator.MainGenerator.path


def create_tokenizers(
    path: Path, iter_amount: int = 300
) -> tuple[BaseTokenizer, BaseTokenizer, list[tuple[str, str]]]:
    """
    returns input tokenizer, output tokenizer and a list of pairs
    """
    input_tokenizer = BPETrainer(path).train(iter_amount)
    output_tokenizer = FigureTrainer(path).train()

    pairs = [
        (input_tokenizer.all_sentences[i], output_tokenizer.all_sentences[i])
        for i in range(len(input_tokenizer.all_sentences))
    ]

    # Asserting a bit
    assert input_tokenizer.encode(SOS_TOKEN) == output_tokenizer.encode(SOS_TOKEN)
    assert input_tokenizer.encode(EOS_TOKEN) == output_tokenizer.encode(EOS_TOKEN)

    return (input_tokenizer, output_tokenizer, pairs)


def main():
    """
    Training and visualizing progress
    """
    # Generating dataset
    path = generate_dataset()

    # Creating tokenizers
    input_tokenizer, output_tokenizer, pairs = create_tokenizers(path)
    tokenizers = (input_tokenizer, output_tokenizer)

    hidden_size = 256
    encoder = EncoderRNN(input_tokenizer.vocab_amount, hidden_size).to(DEVICE)
    attn_decoder = AttnDecoderRNN(
        hidden_size, output_tokenizer.vocab_amount, dropout_p=0.1
    ).to(DEVICE)

    # Running training
    train_iters(
        tokenizers,
        pairs,
        encoder,
        attn_decoder,
        100,
        print_every=500,
    )

    # Evaluating
    evaluate_randomly(encoder, attn_decoder, tokenizers=tokenizers, pairs=pairs)


if __name__ == "__main__":
    main()
