def read_file(file: str):
    with open(file, "r") as in_f:
        lines = in_f.readlines()

    inits = []
    for line in lines:
        line = line.strip()
        inits.extend(line.split(","))

    return inits


def cHash(pre: int, string: str) -> int:
    curr = pre
    for char in string:
        curr += ord(char)
        curr *= 17
        curr %= 256

    return curr


def boxify(inits: list[str]):
    boxes = {}

    for seq in inits:
        if "=" in seq:
            word, lens = seq.split("=")
            boxes.setdefault(cHash(0, word), {})[word] = lens
        elif "-" in seq:
            word = seq.strip("-")
            if ((cont := boxes.get(whash := cHash(0, word))) and
                    cont.get(word)):
                if len(boxes[whash]) == 1:
                    boxes.pop(whash)
                    continue
                boxes[whash].pop(word)

    return boxes


def verify_da_boxify(boxes: dict[int, dict[str, int]]):
    ver_val = 0
    for box, contents in boxes.items():
        box += 1
        for slot, f_len in enumerate(contents.values()):
            ver_val += int(f_len) * (slot + 1) * box
    return ver_val


if __name__ == "__main__":
    inits = read_file("input.txt")
    # inits = read_file("test.txt")

    boxes = boxify(inits)
    print(verify_da_boxify(boxes))  # 236,358
    print(boxes)
