import sys
from math import sqrt
from copy import deepcopy

d = {}
m = []
for line in sys.stdin:
    if not m:
        m.append(int(line.strip()[-5:-1]))
        m.append([])
    else:
        line = line.strip()
        if not line:
            d[m[0]] = m[1]
            m = []
        else:
            m[1].append(list(line))
d[m[0]] = m[1] # EOF

"""
 4      0
 <------>
6        7
^        ^
|  #...  |
|  .#..  |
|  ...#  |
|  .#..  |
v        v
2        3
 <------>
 5      1
"""

def get_borders(tile):
    temp = [tile[0], tile[-1], list(map(lambda x: x[0], tile)), list(map(lambda x: x[-1], tile))]
    return list(map(str().join, temp + list(map(lambda x: x[::-1], temp))))

b = {}
for k in d:
    b[k] = get_borders(d[k])
b2 = {}
for k in b:
    for i in range(8):
        b2[10 * k + i] = b[k][i]
b3 = {}
for i in b2:
    for j in b2:
        if (i // 10) != (j // 10) and b2[i] == b2[j]:
            b3[i] = j

pairs = set(map(lambda x: tuple(sorted([x[0] // 10, x[1] // 10])), b3.items()))
corner = []
for k in b:
    count = 0
    for p in pairs:
        if k in p:
            count += 1
    if count == 2:
        corner.append(k)
ans = 1
for t in corner:
    ans *= t
assert len(corner) == 4
print("Part 1:", ans)

b4, b5 = {}, {}
for i, j in pairs:
    b4[i] = b4.get(i, []) + [j]
    b4[j] = b4.get(j, []) + [i]
    b5[i], b5[j] = False, False

size = int(sqrt(len(d)))
image = []
for _ in range(size):
    image.append([0] * size)

sides = list(filter(lambda x: len(b4[x]) == 3, b4))
inside = list(filter(lambda x: len(b4[x]) == 4, b4))
image[0][0] = corner[0]
b5[corner[0]] = True
image[0][1] = b4[corner[0]][0]
b5[b4[corner[0]][0]] = True
image[1][0] = b4[corner[0]][1]
b5[b4[corner[0]][1]] = True

# Fill left and up sides
for i in range(1, size - 1):
    for s in sides + corner:
        if image[i][0] in b4[s] and not b5[s]:
            image[i + 1][0] = s
            b5[s] = True
        if image[0][i] in b4[s] and not b5[s]:
            image[0][i + 1] = s
            b5[s] = True
# Fill right and down sides
for i in range(size - 1):
    for s in sides + corner:
        if image[i][-1] in b4[s] and not b5[s]:
            image[i + 1][-1] = s
            b5[s] = True
        if image[-1][i] in b4[s] and not b5[s]:
            image[-1][i + 1] = s
            b5[s] = True
# Fill all inside
for i in range(1, size - 1):
    for j in range(1, size - 1):
        for s in inside:
            if image[i][j - 1] in b4[s] and image[i - 1][j] in b4[s] and not b5[s]:
                image[i][j] = s
                b5[s] = True

# Top row becomes this position
def transform(tile, pos):
    if pos == 0:
        return tile
    elif pos == 1:
        return tile[::-1] # flip vertical
    elif pos == 4:
        return list(map(lambda x: x[::-1], tile)) # flip horizontal
    elif pos == 5:
        return transform(transform(tile, 4), 1)
    elif pos == 2:
        return list(map(list, zip(*tile))) # transpose
    elif pos == 6:
        return transform(transform(tile, 2), 4)
    elif pos == 3:
        return transform(transform(tile, 4), 2)
    elif pos == 7:
        return transform(transform(tile, 6), 1)

adjusted = deepcopy(image)

check_d, check_r = {}, {}
for k in range(8):
    check_d[image[1][0] * 10 + k] = list(b2[image[1][0] * 10 + k])
    check_r[image[0][1] * 10 + k] = list(b2[image[0][1] * 10 + k])
for k in range(8):
    temp = image[0][0] * 10 + k
    temp_img = transform(d[temp // 10], temp % 10)
    cnt = 0
    if temp_img[-1] not in check_d.values():
        cnt += 1
    if list(map(lambda x: x[-1], temp_img)) not in check_r.values():
        cnt += 1
    if cnt == 0:
        adjusted[0][0] = temp
        break

# Left sides
for i in range(1, size):
    for j in range(8):
        temp = transform(d[image[i][0]], j)
        if temp[0] == transform(d[adjusted[i - 1][0] // 10], adjusted[i - 1][0] % 10)[-1]:
            adjusted[i][0] = image[i][0] * 10 + j
# Up sides
for i in range(1, size):
    for j in range(8):
        temp = transform(d[image[0][i]], j)
        if list(map(lambda x: x[0], temp)) == list(map(lambda x: x[-1], transform(d[adjusted[0][i - 1] // 10], adjusted[0][i - 1] % 10))):
            adjusted[0][i] = image[0][i] * 10 + j
# The rest
for i in range(1, size):
    for j in range(1, size):
        for k in range(8):
            temp = transform(d[image[i][j]], k)
            if temp[0] == transform(d[adjusted[i - 1][j] // 10], adjusted[i - 1][j] % 10)[-1] and \
                list(map(lambda x: x[0], temp)) == list(map(lambda x: x[-1], transform(d[adjusted[i][j - 1] // 10], adjusted[i][j - 1] % 10))):
                    adjusted[i][j] = image[i][j] * 10 + k

def deborder(tile):
    return list(map(lambda x: x[1:-1], tile[1:-1]))

for i in range(size):
    for j in range(size):
        temp = adjusted[i][j]
        adjusted[i][j] = deborder(transform(d[temp // 10], temp % 10))

# Counting Nessies
new_map = []
for _ in range (8 * size):
    new_map.append([])
for i in range(size):
    for j in range(size):
        for k in range(8):
            new_map[8 * i + k].extend(adjusted[i][j][k])

"""
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""

for k in range(8):
    trans_map = transform(new_map, k)
    cnt = 0
    for i in range(len(trans_map) - 2):
        for j in range(len(trans_map[0]) - 19):
            tags = [
                (0, 18), (1, 0), (1, 5), (1, 6), (1, 11),
                (1, 12), (1, 17), (1, 18), (1, 19), (2, 1),
                (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)
            ]
            found = True
            for di, dj in tags:
                if trans_map[i + di][j + dj] != "#":
                    found = False
                    break
            if found:
                cnt += 1
    if cnt != 0:
        break
trans_map = transform(new_map, k)
for i in range(len(trans_map) - 2):
    for j in range(len(trans_map[0]) - 19):
        tags = [
            (0, 18), (1, 0), (1, 5), (1, 6), (1, 11),
            (1, 12), (1, 17), (1, 18), (1, 19), (2, 1),
            (2, 4), (2, 7), (2, 10), (2, 13), (2, 16)
        ]
        found = True
        for di, dj in tags:
            if trans_map[i + di][j + dj] != "#":
                found = False
                break
        if found:
            for di, dj in tags:
                trans_map[i + di][j + dj] = "O"
print("Part 2:", sum(map(lambda x: x.count("#"), trans_map)))