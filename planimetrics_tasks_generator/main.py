from data_loader import TasksDataset, get_loader
from data_provider import DataProvider
from settings import TEST_FRACTION, VAL_FRACTION
from tokenizers.source_tokenizer.bpe_trainer import BPETrainer
from tokenizers.target_tokenizer.target_tokenizer import TargetTokenizer


def main():
    # 1. Building a data provider
    data_provider = DataProvider.build("dataset")

    # 2. Creating tokenizers
    src_tokenizer = BPETrainer().train(data_provider.iter_src())
    tgt_tokenizer = TargetTokenizer()

    # 3. Dividing data onto train, validation and test
    train_data, val_data, test_data = data_provider.train_val_test(VAL_FRACTION, TEST_FRACTION)

    # 4. Creating data_loaders
    train_dataset = TasksDataset(train_data, src_tokenizer, tgt_tokenizer)
    train_dataloader = get_loader(train_dataset)

    val_dataset = TasksDataset(val_data, src_tokenizer, tgt_tokenizer)
    val_dataloader = get_loader(val_dataset)

    test_dataset = TasksDataset(test_data, src_tokenizer, tgt_tokenizer)


if __name__ == "__main__":
    main()
