from time import perf_counter_ns

with open("input.txt", "r") as f_in:
# with open("test.txt", "r") as f_in:
    lines = f_in.readlines()

start_full = perf_counter_ns()
games = {}
for index, line in enumerate(lines):
    games[index + 1] = " ".join(line.strip().split())
end_games_dict = perf_counter_ns() - start_full
copies = {}

start_calc_paths = perf_counter_ns()
process = list(games.keys())

print(games)
print(process)

for game in process:
    score = 0
    line = games.get(game)
    winning_nums, card_nums = map(str.strip, line.split("|"))
    winning_nums, card_nums = winning_nums.split(" "), card_nums.split(" ")

    for winning_num in winning_nums:
        if winning_num in card_nums:
            score += 1
            if game + score < (max(games.keys()) + 1):
                process.append(game + score)

end_calc_paths = perf_counter_ns() - start_calc_paths

print(process)
print(len(process))  # 5,539,496
end_full = perf_counter_ns() - start_full

print(f"Total time: {end_full / 1_000_000_000} s")
print(f"Populate game dict: {end_games_dict / 1_000_000_000} s")
print(f"Resolve paths: {end_calc_paths / 1_000_000_000} s")
