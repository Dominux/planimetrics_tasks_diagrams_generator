import unittest

from tokenizers.bpe import BPETrainer


class TestTokenize(unittest.TestCase):
    def test_tokenize_prompts(self):
        bpe_tokenizer = BPETrainer(
            "/home/dominux/coding/who_cares/dataset_generator/dataset"
        ).train(250)

        # vectorization
        text = "На рисунке 302 MD = MW, MV = MF, ∠1 = 32°, ∠2 = 17°. а) Докажите, что треугольники DMV и WMF равны; б) найдите ∠DFW"

        vector = bpe_tokenizer.encode(text)
        decoded_text = bpe_tokenizer.decode(vector)

        assert text.lower() == decoded_text, print(text, decoded_text, sep="\n")

    def test_tokenize_svg(self):
        bpe_tokenizer = BPETrainer(
            "/home/dominux/coding/who_cares/dataset_generator/dataset"
        ).train(300, ".svg")

        # vectorization
        text = """
            <?xml version="1.0" encoding="UTF-8"?>
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="40" height="40" viewBox="-20.0 -20.0 40 40">
                <defs></defs>
                <path d="M0,0 L3,-8" stroke-width="0.2" stroke="black" />
                <path d="M0,0 L12,0" stroke-width="0.2" stroke="black" />
                <path d="M3,-8 L12,0" stroke-width="0.2" stroke="black" />
                <path d="M12,0 L15,-8" stroke-width="0.2" stroke="black" />
                <path d="M0,0 L15,-8" stroke-width="0.2" stroke="black" />
                <text x="0" y="1.6" font-size="1.5" dy="0em">M</text>
                <text x="1.7" y="-8" font-size="1.5" dy="0em">B</text>
                <text x="15.3" y="-8" font-size="1.5" dy="0em">Z</text>
                <text x="12" y="1.5" font-size="1.5" dy="0em">I</text>
                <text x="7.2" y="-4.8" font-size="1.5" dy="0em">Q</text>
                <path d="M4.3,-2.8 L4.7,-2" stroke-width="0.1" stroke="black" />
                <path d="M11,-6.4 L11.4,-5.6" stroke-width="0.1" stroke="black" />
                <path d="M5.3,-5.4 L5.7,-6.2" stroke-width="0.1" stroke="black" />
                <path d="M5.6,-5.1 L6,-5.9" stroke-width="0.1" stroke="black" />
                <path d="M9.3,-1.8 L9.7,-2.7" stroke-width="0.1" stroke="black" />
                <path d="M9.6,-1.5 L10,-2.4" stroke-width="0.1" stroke="black" />
                <text x="3.2" y="-4.9" font-size="1.2" dy="0em">1</text>
                <path d="M 2.5 -6.5 A 0.5 0.5 0 0 0 4.1 -7" fill="none" stroke-width="0.1" stroke="black"/>
                <text x="9.5" y="-0.3" font-size="1.2" dy="0em">2</text>
                <path d="M 10.7 0 A 0.5 0.5 0 0 1 10.9 -0.9" fill="none" stroke-width="0.1" stroke="black"/>
            </svg>
        """.strip().replace(
            "/n", ""
        )

        vector = bpe_tokenizer.encode(text)
        decoded_text = bpe_tokenizer.decode(vector)

        assert text.lower() == decoded_text, print(text, decoded_text, sep="\n")
