
with open("input.txt", "r") as f_in:
    lines = {line.split(" ")[0]: int(line.split(" ")[1])
             for line in f_in.readlines()}

orderings = "AKQJT98765432"

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
    for card in orderings:
        card_count = hand.count(card)
        if card_count == 2:
            pairs += 1
        cards[card] = card_count

    if (c := max(cards.values())) == 5:
        key = "five"
    elif c == 4:
        key = "four"
    elif c == 3 and pairs:
        key = "full"
    elif c == 3:
        key = "three"
    elif pairs == 1:
        key = "one"
    elif pairs == 2:
        key = "two"
    elif c == 1:
        key = "high"

    cats[key].append(hand)


winnings = 0
mult = len(lines)
for hands in cats.values():
    hands.sort(key=lambda word: [orderings.index(c) for c in word])
    for hand in hands:
        winnings += lines[hand] * mult
        mult -= 1

print(winnings)  # 248,812,215
