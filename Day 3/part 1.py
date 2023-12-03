import string
import re

with open("input.txt", "r") as f_in:
    lines = f_in.readlines()

pattern = re.compile(r"(\d+)")

sum_n = 0
do_thing = False
line_nums = {}
line_syms = {}
used_nums = set()
for l_num, line in enumerate(lines):
    matches = pattern.findall(line)
    last_index_num = 0
    for match in matches:
        start = line.find(match, last_index_num)
        last_index_num = start + len(match)
        num_range = tuple(range(start, start + len(match)))
        line_nums[l_num, *num_range] = int(match)

    for index, char in enumerate(line.strip()):
        if not char.isdigit() and char != ".":
            line_syms[l_num, index] = char

print(line_nums)
print(line_syms)

for n_position, number in line_nums.items():
    adj = False
    for row, col in line_syms:
        if row == n_position[0]:
            if (col == n_position[1] - 1) or (
                    col == n_position[-1] + 1):
                adj = True
                break
        if abs(row - n_position[0]) == 1:
            if col in range(n_position[1] - 1, n_position[-1] + 2):
                adj = True
                break
    if adj:
        sum_n += number

print(sum_n)
