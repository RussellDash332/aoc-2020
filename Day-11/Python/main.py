import sys

mapper = {"L": 0, "#": 1, ".": -1}
seats, seats2 = [], []
new_seats, new_seats2 = [], []

def neighbours(r, c, nr, nc):
    res = []
    if r >= 1:
        if c >= 1:
            res.append([r - 1, c - 1])
        if c < nc - 1:
            res.append([r - 1, c + 1])
        res.append([r - 1, c])
    if r < nr - 1:
        if c >= 1:
            res.append([r + 1, c - 1])
        if c < nc - 1:
            res.append([r + 1, c + 1])
        res.append([r + 1, c])
    if c >= 1:
        res.append([r, c - 1])
    if c < nc - 1:
        res.append([r, c + 1])
    return res

def find_occ(r, c, seats):
    nr, nc = len(seats), len(seats[0])
    ans = 0
    # up
    for i in range(r - 1, -1, -1):
        if seats[i][c] == 1:
            ans += 1
        if seats[i][c] != -1:
            break

    # down
    for i in range(r + 1, nr):
        if seats[i][c] == 1:
            ans += 1
        if seats[i][c] != -1:
            break
    # left
    for i in range(c - 1, -1, -1):
        if seats[r][i] == 1:
            ans += 1
        if seats[r][i] != -1:
            break
    # right
    for i in range(c + 1, nc):
        if seats[r][i] == 1:
            ans += 1
        if seats[r][i] != -1:
            break
    # up left
    ulr, ulc = r - 1, c - 1
    while ulr >= 0 and ulc >= 0:
        if seats[ulr][ulc] == 1:
            ans += 1
        if seats[ulr][ulc] != -1:
            break
        ulr -= 1
        ulc -= 1
    # down right
    drr, drc = r + 1, c + 1
    while drr < nr and drc < nc:
        if seats[drr][drc] == 1:
            ans += 1
        if seats[drr][drc] != -1:
            break
        drr += 1
        drc += 1
    # up right
    urr, urc = r - 1, c + 1
    while urr >= 0 and urc < nc:
        if seats[urr][urc] == 1:
            ans += 1
        if seats[urr][urc] != -1:
            break
        urr -= 1
        urc += 1
    # down left
    dlr, dlc = r + 1, c - 1
    while dlr < nr and dlc >= 0:
        if seats[dlr][dlc] == 1:
            ans += 1
        if seats[dlr][dlc] != -1:
            break
        dlr += 1
        dlc -= 1
    return ans

for line in sys.stdin:
    line = list(map(lambda x: mapper[x], list(line.strip())))
    seats.append(line.copy())
    new_seats.append(line.copy())
    seats2.append(line.copy())
    new_seats2.append(line.copy())

nr, nc = len(seats), len(seats[0])
from copy import deepcopy
while True:
    for i in range(nr):
        for j in range(nc):
            if seats[i][j] == 0 and len(list(filter(lambda x: seats[x[0]][x[1]] == 1, neighbours(i, j, nr, nc)))) == 0:
                new_seats[i][j] = 1
            elif seats[i][j] == 1 and len(list(filter(lambda x: seats[x[0]][x[1]] == 1, neighbours(i, j, nr, nc)))) >= 4:
                new_seats[i][j] = 0
    if new_seats == seats:
        break
    seats = deepcopy(new_seats)
print("Part 1:", sum(list(map(lambda x: len(list(filter(lambda y: y == 1, x))), new_seats))))

while True:
    for i in range(nr):
        for j in range(nc):
            occ = find_occ(i, j, seats2)
            if seats2[i][j] == 0 and occ == 0:
                new_seats2[i][j] = 1
            elif seats2[i][j] == 1 and occ >= 5:
                new_seats2[i][j] = 0
    if new_seats2 == seats2:
        break
    seats2 = deepcopy(new_seats2)
print("Part 2:", sum(list(map(lambda x: len(list(filter(lambda y: y == 1, x))), new_seats2))))