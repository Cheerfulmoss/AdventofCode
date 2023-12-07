
with open("input.txt", "r") as f_in:
# with open("test.txt", "r") as f_in:
    lines = {line.split(" ")[0]: int(line.split(" ")[1])
             for line in f_in.readlines()}

orderings = "AKQT98765432J"

cats = {
    "five": [],
    "four": [],
    "full": [],
    "three": [],
    "two": [],
    "one": [],
    "high": [],
}

for hand in lines:
    cards = {}
    pairs = 0
    joker = False
    if "J" in hand:
        joker = True
    for card in orderings:
        card_count = hand.count(card)
        if card_count == 2:
            pairs += 1
        cards[card] = card_count

    if (c := max(cards.values())) == 5:
        key = "five"
    elif c == 4:
        key = "four"
        if joker:
            key = "five"
    elif c == 3 and pairs:
        key = "full"
        if joker:
            key = "five"
    elif c == 3:
        key = "three"
        if joker:
            if (j := cards["J"]) == 1:
                key = "four"
            elif j == 2:
                key = "five"
    elif pairs == 2:
        key = "two"
        if joker:
            if (j := cards["J"]) == 1:
                key = "full"
            if j == 2:
                key = "four"
    elif pairs == 1:
        key = "one"
        if joker:
            if (j := cards["J"]) == 1 or j == 2:
                key = "three"
            elif j == 3:
                key = "five"
    elif c == 1:
        key = "high"
        if joker:
            if (j := cards["J"]) == 1:
                key = "one"
            elif j == 2:
                key = "three"
            elif j == 3:
                key = "four"
            elif j == 4:
                key = "five"
    cats[key].append(hand)

winnings = 0
mult = len(lines)
for hands in cats.values():
    hands.sort(key=lambda word: [orderings.index(c) for c in word])
    for hand in hands:
        winnings += lines[hand] * mult
        mult -= 1

print(winnings, cats)  # 250,057,090
