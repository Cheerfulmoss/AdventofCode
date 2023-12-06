import re


with open("input.txt", "r") as f_in:
# with open("test.txt", "r") as f_in:
    lines = f_in.readlines()

time = int(re.sub(r"\s+", "", lines[0].split(":")[-1]))
distance = int(re.sub(r"\s+", "", lines[1].split(":")[-1]))

speed = 1
new_time = time - 1
while speed * new_time <= distance:
    speed += 1
    new_time -= 1
max_hold = new_time

while speed * new_time > distance:
    speed += 1
    new_time -= 1
min_hold = new_time + 1

counts = max_hold - min_hold + 1
print(min_hold, max_hold)


print(counts)