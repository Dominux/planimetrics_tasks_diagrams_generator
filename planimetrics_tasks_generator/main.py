from data_provider import DataProvider
from tokenizers.source_tokenizer.bpe_trainer import BPETrainer
from tokenizers.target_tokenizer.target_tokenizer import TargetTokenizer


def main():
    # 1. Building a data provider
    data_provider = DataProvider.build("dataset")

    # 2. Creating tokenizers
    src_tokenizer = BPETrainer().train(data_provider.iter_src())
    tgt_tokenizer = TargetTokenizer()


if __name__ == "__main__":
    main()
