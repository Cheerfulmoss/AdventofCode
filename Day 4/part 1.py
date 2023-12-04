with open("input.txt", "r") as f_in:
# with open("test.txt", "r") as f_in:
    lines = f_in.readlines()

total = 0
for index, line in enumerate(lines):
    scored = False
    score = 0
    line = line.strip()
    numbers = line.split(":")[-1].strip()
    winning_nums, card_nums = map(str.strip, numbers.split("|"))
    winning_nums = " ".join(winning_nums.split()).split(" ")
    card_nums = " ".join(card_nums.split()).split(" ")

    for winning_num in winning_nums:
        if winning_num in card_nums:
            if not scored:
                score = 1
                scored = True
                continue
            score = score << scored

    total += score
    print(card_nums, winning_nums, score)

print(total)
