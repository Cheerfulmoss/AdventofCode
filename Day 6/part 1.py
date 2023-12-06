


with open("input.txt", "r") as f_in:
# with open("test.txt", "r") as f_in:
    lines = f_in.readlines()

times = list(map(int, " ".join(lines[0].split(":")[-1].split()).split(" ")))
distances = list(map(int, " ".join(lines[1].split(":")[-1].split()).split(" ")))

counts = 1
for index, time in enumerate(times):
    speed = 1
    new_time = time - 1
    while speed * new_time <= distances[index]:
        speed += 1
        new_time -= 1
    max_hold = new_time

    while speed * new_time > distances[index]:
        speed += 1
        new_time -= 1
    min_hold = new_time + 1

    counts *= max_hold - min_hold + 1
    print(min_hold, max_hold, times)


print(counts)