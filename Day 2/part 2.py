valid_games = []

with open(f"input.txt", "r") as f_in:
    for line in f_in:
        invalid = False
        line = line.strip()
        game_id = line.split(":")[0]
        sets = line.removeprefix(f"{game_id}:").strip().split(";")

        lims = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        for outcomes in sets:
            for outcome in outcomes.split(","):
                count, colour = outcome.strip().split(" ")
                if (int_c := int(count)) > lims[colour]:
                    lims[colour] = int_c
        valid_games.append(lims["red"] * lims["green"] * lims["blue"])

print(sum(valid_games))
