import string, random


# def get_random_letters(length: int) -> list[str]:
#     alphabet = list(string.ascii_uppercase)
#     random.shuffle(alphabet)
#     return alphabet[:length]

# TEMPLATE = "Основания {} {}{} = {} см, {}{} = {} см. Найти диагональ."

# FIGURES = {
#     'quadrilateral': 'четырехугольника',
#     'parallelogram': 'параллелограмма',
#     'trapezoid': 'трапеции',
#     'rectangle': 'прямоугольника',
#     'square': 'квадрата',
# }

# with open('lol.tsv', 'a') as f:

#     for _ in range(200):
#         letters = get_random_letters(4)

#         figure_type = random.choice(list(FIGURES))
#         diff_1 = random.randint(3, 25)
#         diff_2 = random.randint(2, 25)
#         diff_3 = random.randint(2, 25)

#         text = TEMPLATE.format(FIGURES[figure_type], letters[0], letters[1], diff_1, letters[2], letters[3], diff_2)
#         figure_output = f'[{{"type": "{figure_type}", "name": {"".join(letters)}}}]'
#         f.write(text + '\t' + figure_output + '\n')

# lines = []

# with open('lol.tsv') as f1, open('tasks.tsv') as f2:
#     lines.extend(f1.readlines())
#     lines.extend(f2.readlines())

# random.shuffle(lines)

# with open('kek.tsv', 'w') as f:
#     f.writelines(lines)

lol = 'YDOF}]\n'

with open('tasks.tsv') as f, open('lol.tsv', 'w') as output:
    for line in f:
        if line[:len(line) - len(lol)].endswith('"name": '):
            figure_name = line[len(line) - len(lol):len(line) - len(lol) + 4]
            line = line[:len(line) - len(lol)] + f'"{figure_name}"}}]\n'

        output.write(line)
