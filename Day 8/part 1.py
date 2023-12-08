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
count = 0
while node != "ZZZ":
    for move in sequence:
        node = nodes[node][int(move)]
        print(node)
        count += 1
        if node == "ZZZ":
            break

print(count)  # 16,897
