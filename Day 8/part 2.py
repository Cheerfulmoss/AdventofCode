import math

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

sel_nodes = [node for node in nodes if node.endswith("A")]
steps = [None] * len(sel_nodes)

count = 0
while not all(node.endswith("Z") for node in sel_nodes):
    for move in sequence:
        move_made = False
        for index, node in enumerate(sel_nodes):
            if node.endswith("Z"):
                continue
            sel_nodes[index] = nodes[node][int(move)]
            if not move_made:
                move_made = not move_made
                count += 1
            if sel_nodes[index].endswith("Z") and steps[index] is None:
                steps[index] = count

print(steps)
print(math.lcm(*steps))  # 16,563,603,485,021
