import sys

def num_active(x, y, z):
    ans = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                ans += d.get((x + dx, y + dy, z + dz), 0)
    return ans - d.get((x, y, z), 0)

def num_active2(x, y, z, w):
    ans = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dw in [-1, 0, 1]:
                    ans += d2.get((x + dx, y + dy, z + dz, w + dw), 0)
    return ans - d2.get((x, y, z, w), 0)

m = []
for line in sys.stdin:
    m.append(list(line.strip()))

d = {}
for i in range(len(m)):
    for j in range(len(m[0])):
        d[(i, j, 0)] = int(m[i][j] == "#")
for t in range(6):
    new_d = {}
    for x, y, z in d:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if d.get((x + dx, y + dy, z + dz), 0):
                        new_d[(x + dx, y + dy, z + dz)] = int(num_active(x + dx, y + dy, z + dz) in [2, 3])
                    else:
                        new_d[(x + dx, y + dy, z + dz)] = int(num_active(x + dx, y + dy, z + dz) == 3)
    d = new_d
print("Part 1:", sum(d.values()))

d2 = {}
for i in range(len(m)):
    for j in range(len(m[0])):
        d2[(i, j, 0, 0)] = int(m[i][j] == "#")
for t in range(6):
    new_d2 = {}
    for x, y, z, w in d2:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if d2.get((x + dx, y + dy, z + dz, w + dw), 0):
                            new_d2[(x + dx, y + dy, z + dz, w + dw)] = int(num_active2(x + dx, y + dy, z + dz, w + dw) in [2, 3])
                        else:
                            new_d2[(x + dx, y + dy, z + dz, w + dw)] = int(num_active2(x + dx, y + dy, z + dz, w + dw) == 3)
    d2 = new_d2
print("Part 2:", sum(d2.values()))