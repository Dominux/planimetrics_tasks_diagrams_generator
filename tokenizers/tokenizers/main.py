from tokenizers.bpe import BPETrainer


def main():
    bpe_tokenizer = BPETrainer(
        "/home/dominux/coding/who_cares/dataset_generator/dataset"
    ).train(250)

    # vectorization
    text = "На рисунке 302 MD = MW, MV = MF, ∠1 = 32°, ∠2 = 17°. а) Докажите, что треугольники DMV и WMF равны; б) найдите ∠DFW"

    vector = bpe_tokenizer.encode(text)
    print(vector)
    decoded_text = bpe_tokenizer.decode(vector)
    print(decoded_text)


if __name__ == "__main__":
    main()
