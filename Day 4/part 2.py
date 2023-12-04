from time import perf_counter_ns

with open("input.txt", "r") as f_in:
# with open("test.txt", "r") as f_in:
    lines = f_in.readlines()


start_full = perf_counter_ns()
games = {}
for index, line in enumerate(lines):
    score = 0
    line = " ".join(line.strip().split())
    winning_nums, card_nums = map(str.strip, line.split("|"))
    winning_nums, card_nums = winning_nums.split(" ")[2:], card_nums.split(" ")
    for winning_num in winning_nums:
        if winning_num in card_nums:
            score += 1

    games[index + 1] = range(index + 2, index + score + 2)
end_game_paths = perf_counter_ns() - start_full

start_calc_paths = perf_counter_ns()
process = list(games.keys())

print(games)
print(process)

for game in process:
    card_copies = games.get(game)
    process.extend(card_copy)

end_calc_paths = perf_counter_ns() - start_calc_paths

print(len(process))  # 5,539,496
end_full = perf_counter_ns() - start_full

print(f"Total time: {end_full / 1_000_000_000} s")
print(f"Get game paths: {end_game_paths / 1_000_000_000} s")
print(f"Resolve paths: {end_calc_paths / 1_000_000_000} s")

