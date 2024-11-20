import string, random


def get_random_letters(length: int) -> list[str]:
    alphabet = list(string.ascii_uppercase)
    random.shuffle(alphabet)
    return alphabet[:length]

output_lines = []

with open("planimetrics_tasks_generator/datasets/lmao.tsv") as f:
    for i, line in enumerate(f):
        line = line[0].capitalize() + line[1:-2]
        line_splitted = line.split("треугольника")

        for _ in range(2):
            letters = get_random_letters(6)
            t1, t2 = "".join(letters[:3]), "".join(letters[3:])

            line = line_splitted[0] + "треугольника " + t1 + line_splitted[1] + "треугольника " + t2 + line_splitted[2] + f'\t[{{"figure": "triangle", "name": "{t1}"}}, {{"figure", "triangle", "name": "{t2}"}}]\n'
            output_lines.append(line)

        # line = line_splitted[0] + "треугольника" + " ABC" + line_splitted[1] + "треугольника" + " DEF" + line_splitted[2] + '\t[{"figure": "triangle", "name": "ABC"}, {"figure", "triangle", "name": "DEF"}]'
        # output_f.write(line + '\n')

random.shuffle(output_lines)

with open("planimetrics_tasks_generator/datasets/triangels_new.tsv", "w") as f:
    f.writelines(output_lines)
