import sys

sys.setrecursionlimit(17000)


def explore_node(node: str, step_i: int, count: int) -> int:
    if node == "ZZZ":
        return count

    count += 1
    return explore_node(nodes[node][int(sequence[step_i])],
                        (step_i + 1) % len(sequence),
                        count)


with open("input.txt", "r") as in_f:
    lines = in_f.readlines()

trans_table = str.maketrans("RL", "10")

sequence = lines[0].strip().translate(trans_table)

nodes = {
    line.split(" = ")[0]:
        line.split(" = ")[1].replace("(", "").replace(")",
                                                      "").strip().split(", ")
    for line in lines[2:]
}

print(nodes)
print(sequence)

node = "AAA"
print(explore_node(node, 0, 0))
