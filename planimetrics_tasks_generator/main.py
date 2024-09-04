from timeit import default_timer as timer

import torch

from data_loader import TasksDataset, get_loader
from data_provider import TrianglesTasksDataProvider
from models import Seq2SeqTransformer, train_epoch, validate, evaluate, translate
from settings import (
    EMB_SIZE, 
    FFN_HID_DIM, 
    LEARNING_RATE,
    MANUAL_SEED, 
    NHEAD, 
    NUM_DECODER_LAYERS, 
    NUM_ENCODER_LAYERS, 
    NUM_EPOCHS, 
    TEST_FRACTION, 
    VAL_FRACTION
)
from tokenizers.constants import PAD_IDX
from tokenizers.source_tokenizer.bpe_trainer import BPETrainer
from tokenizers.target_tokenizer.target_tokenizer import TargetTokenizer


def main():
    # 0. Setting manual seed
    torch.manual_seed(MANUAL_SEED)

    # 1. Building a data provider
    data_provider = TrianglesTasksDataProvider.build("datasets/tasks.txt")

    # 2. Creating tokenizers
    src_tokenizer = BPETrainer().train(data_provider.iter_src())
    tgt_tokenizer = TargetTokenizer()
    
    # 3. Dividing data onto train, validation and test
    train_data, val_data, test_data = data_provider.train_val_test(VAL_FRACTION, TEST_FRACTION)

    # 3.1. Augmenting data
    train_data.augment_data(10)
    val_data.augment_data(10)
    test_data.augment_data()

    # 4. Creating data_loaders
    train_dataset = TasksDataset(train_data, src_tokenizer, tgt_tokenizer)
    train_dataloader = get_loader(train_dataset)

    val_dataset = TasksDataset(val_data, src_tokenizer, tgt_tokenizer)
    val_dataloader = get_loader(val_dataset)

    test_dataset = TasksDataset(test_data, src_tokenizer, tgt_tokenizer)

    experiments = []

    for epochs_number in [10, 12, 14, 16, 18, 20]:
        epochs_experiment = []

        for _ in range(5):

            # 5. Initializing models
            transformer = Seq2SeqTransformer(
                NUM_ENCODER_LAYERS, 
                NUM_DECODER_LAYERS, 
                EMB_SIZE,
                NHEAD, 
                len(src_tokenizer), 
                len(tgt_tokenizer), 
                FFN_HID_DIM
            )

            # 6. Setting loss function and optimizer
            loss_fn = torch.nn.CrossEntropyLoss(ignore_index=PAD_IDX)
            optimizer = torch.optim.Adam(
                transformer.parameters(), 
                lr=LEARNING_RATE, 
                betas=(0.9, 0.98), 
                eps=1e-9
            )

            # 7. Learning
            for epoch in range(1, epochs_number + 1):
                start_time = timer()
                train_loss = train_epoch(transformer, loss_fn, optimizer, train_dataloader)
                end_time = timer()
                val_loss = validate(transformer, loss_fn, val_dataloader)
                print(f"Epoch: {epoch}, Train loss: {train_loss:.4f}, Val loss: {val_loss:.4f}, Epoch time = {(end_time - start_time):.2f}s")

            # 8. Testing
            right_translations = evaluate(transformer, test_dataset, test_data, src_tokenizer, tgt_tokenizer)
            print(f"Evaluation score: {right_translations / len(test_dataset)} ({right_translations}/{len(test_dataset)} right translations)")

            src = "Сторона ZY треугольника ZYH равна 14 мм, сторона YH вдвое больше стороны ZY, а сторона HZ на 21 мм меньше стороны YH. Найдите периметр треугольника ZYH."
            expected_tgt = 'zyh'

            output = translate(transformer, src, src_tokenizer, tgt_tokenizer)
            print(f"input: {src}, expected: {expected_tgt}, got: {output}")

            score = right_translations / len(test_dataset)
            epochs_experiment.append(score)
        
        experiments.append(epochs_experiment)

    with open('experiments.csv', 'w') as f:
        for epoch in experiments:
            line = ','.join(str(_) for _ in epoch)
            f.write(f'{line}\n')


if __name__ == "__main__":
    main()
