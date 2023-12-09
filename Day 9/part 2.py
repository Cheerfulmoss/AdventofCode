def reduce(sequences: list[list[int]]) -> list[list[int]]:
    while not all(number == sequences[-1][0] for number in sequences[-1]):
        new_sequence = []
        for index, number in enumerate(sequences[-1]):
            if not index:
                continue
            new_sequence.append(number - sequences[-1][index - 1])

        sequences.append(new_sequence)
    return sequences


def extension(reductions: list[list[int]]) -> int:
    rev_reds = reductions[::-1]
    for index, red in enumerate(rev_reds):
        if index == 0:
            continue
        red.insert(0, red[0] - rev_reds[index - 1][0])
    return reductions[0][0]


with open("input.txt", "r") as in_f:
    lines = [list(map(int, line.split(" "))) for line in in_f.readlines()]

sum_n = 0
for line in lines:
    reductions = reduce([line])
    sum_n += extension(reductions)

print(sum_n)
