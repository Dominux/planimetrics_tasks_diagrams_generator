import unittest

from tokenizers.bpe import BPETrainer


class TestTokenize(unittest.TestCase):
    def test_tokenize(self):
        bpe_tokenizer = BPETrainer(
            "/home/dominux/coding/who_cares/dataset_generator/dataset"
        ).train(250)

        # vectorization
        text = "На рисунке 302 MD = MW, MV = MF, ∠1 = 32°, ∠2 = 17°. а) Докажите, что треугольники DMV и WMF равны; б) найдите ∠DFW"

        vector = bpe_tokenizer.encode(text)
        decoded_text = bpe_tokenizer.decode(vector)

        assert text == decoded_text, print(text, decoded_text, sep="\n")
