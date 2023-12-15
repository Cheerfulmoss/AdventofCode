
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



if __name__ == "__main__":
    inits = read_file("input.txt")
    # inits = read_file("test.txt")
    hashes = []
    for init in inits:
        hashes.append(cHash(0, init))
    print(hashes)
    print(sum(hashes))