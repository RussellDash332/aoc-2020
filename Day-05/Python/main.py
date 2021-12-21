import sys

ids = []
for line in sys.stdin:
    line = line.strip()
    r, c = 0, 0
    for i in range(7):
        r *= 2
        r += int(line[i] == "B")
    for i in range(3):
        c *= 2
        c += int(line[i - 3] == "R")
    ids.append(8 * r + c)
print("Part 1:", max(ids))
print("Part 2:", sum(range(min(ids), max(ids) + 1)) - sum(ids))