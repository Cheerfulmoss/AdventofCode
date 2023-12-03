import string
import re

with open("input.txt", "r") as f_in:
    lines = f_in.readlines()

pattern = re.compile(r"(\d+)")

sum_n = 0
do_thing = False
line_nums = {}
line_syms = {}
for l_num, line in enumerate(lines):
    matches = pattern.findall(line)
    last_index_num = 0
    for match in matches:
        start = line.find(match, last_index_num)
        last_index_num = start + len(match)
        num_range = (start, start + len(match) - 1)
        line_nums[l_num, *num_range] = int(match)

    for index, char in enumerate(line.strip()):
        if not char.isdigit() and char != ".":
            line_syms[l_num, index] = char

print(line_nums)
print(line_syms)

ratios = {}
for n_position, number in line_nums.items():
    for (row, col), symbol in line_syms.items():
        if (row == n_position[0] and
                ((col == n_position[1] - 1) or (
                    col == n_position[2] + 1)) and symbol == "*"):
            ratios.setdefault((row, col), [])
            ratios[row, col].append(number)
            break
        if (abs(row - n_position[0]) == 1 and
                (col in range(n_position[1] - 1, n_position[2] + 2) and
                    symbol == "*")):
            ratios.setdefault((row, col), [])
            ratios[row, col].append(number)
            break

print(ratios)
for loc, nums in ratios.items():
    if len(nums) > 1:
        sum_n += nums[0] * nums[1]

print(sum_n)  # 80,179,647
