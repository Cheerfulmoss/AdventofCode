valid_games = []
lims = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


with open(f"input.txt", "r") as f_in:
    for line in f_in:
        invalid = False
        line = line.strip()
        game_id = line.split(":")[0]
        sets = line.removeprefix(f"{game_id}:").strip().split(";")
        for outcomes in sets:
            for outcome in outcomes.split(","):
                count, colour = outcome.strip().split(" ")
                if int(count) > lims[colour]:
                    invalid = True
                    break
            if invalid:
                break
        if not invalid:
            valid_games.append(int(game_id.split(" ")[-1]))


print(sum(valid_games))
