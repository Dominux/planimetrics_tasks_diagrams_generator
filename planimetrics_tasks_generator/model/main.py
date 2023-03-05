from tokenizers.base import BaseTokenizer
from tokenizers.bpe import BPETrainer
from model.decoders import EncoderRNN, AttnDecoderRNN


def create_tokenizers() -> tuple[BaseTokenizer, BaseTokenizer, list[tuple[str, str]]]:
    """
    returns input tokenizer, output tokenizer and a list of pairs
    """
    ...


def main():
    """
    Training and visualizing progress
    """
    # Creating tokenizers
    input_tokenizer, output_tokenizer, pairs = create_tokenizers()

    hidden_size = 256
    encoder1 = EncoderRNN(input_lang.n_words, hidden_size).to(device)
    attn_decoder1 = AttnDecoderRNN(hidden_size, output_lang.n_words, dropout_p=0.1).to(
        device
    )

    trainIters(encoder1, attn_decoder1, 75000, print_every=5000)


if __name__ == "__main__":
    main()
