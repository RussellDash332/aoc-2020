import sys

dirs = ['e', 'se', 'sw', 'w', 'nw', 'ne']
pos = []
m = {}
for line in sys.stdin:
    temp = []
    line = line.strip()
    while line:
        if line[0] in dirs:
            temp.append(line[0])
            line = line[1:]
        else:
            temp.append(line[:2])
            line = line[2:]
    pos.append(temp)

for steps in pos:
    x, y = 0, 0
    for s in steps:
        if s == 'e':
            x += 2
        elif s == 'w':
            x -= 2
        elif s == 'se':
            x += 1
            y -= 2
        elif s == 'sw':
            x -= 1
            y -= 2
        elif s == 'nw':
            x -= 1
            y += 2
        else: # ne
            x += 1
            y += 2
    m[(x, y)] = 1 - m.get((x, y), 0)
print("Part 1:", sum(m.values()))

def neighbours(x, y):
    res = [(x - 2, y), (x + 2, y)]
    for dx in [-1, 1]:
        for dy in [-2, 2]:
            res.append((x + dx, y + dy))
    return res

for d in range(100):
    # print("Simulating Day", d + 1)
    new_m = {}
    for k in m:
        n = neighbours(*k)
        check = sum(map(lambda x: m.get(x, 0), n))
        if (m[k] == 1 and check not in [1, 2]) or \
            (m[k] == 0 and check == 2):
            new_m[k] = 1 - m[k]
        else:
            new_m[k] = m[k]
        for x, y in n:
            n2 = neighbours(x, y)
            check = sum(map(lambda x: m.get(x, 0), n2))
            if (m.get((x, y), 0) == 1 and check not in [1, 2]) or \
                (m.get((x, y), 0) == 0 and check == 2):
                new_m[(x, y)] = 1 - m.get((x, y), 0)
            else:
                new_m[(x, y)] = m.get((x, y), 0)
    m = new_m
print("Part 2:", sum(m.values()))