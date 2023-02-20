from tokenizers.bpe import BPETrainer


def main():
    bpe_tokenizer = BPETrainer(
        "/home/dominux/coding/who_cares/dataset_generator/dataset"
    ).train(250)
    print(bpe_tokenizer._vocab)


if __name__ == "__main__":
    main()
