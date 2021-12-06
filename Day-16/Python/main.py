import sys

d = {}
tidy_d = {}
arr = []
flat = []
your = False
nearby = False

def check(num, cat):
    ranges = tidy_d[cat]
    for r in ranges:
        if num in range(*r):
            return True
    return False

for line in sys.stdin:
    if not your:
        line = line.strip().split(": ")
        if line == ['']:
            your = True
            input()
            continue
        cat = line[0]
        line = line[1].split(" or ")
        r1, r2 = list(map(int, line[0].split("-"))), list(map(int, line[1].split("-")))
        for r in (r1, r2):
            for i in range(r[0], r[1] + 1):
                d[i] = False
        tidy_d[cat] = [[r1[0], r1[1] + 1], [r2[0], r2[1] + 1]]
    elif not nearby:
        t = list(map(int, line.split(",")))
        input()
        input()
        nearby = True
    else:
        l = list(map(int, line.split(",")))
        flat.extend(l)
        arr.append(l)
print("Part 1:", sum(filter(lambda x: d.get(x, True), flat)))

arr = list(filter(lambda x: not any(map(lambda y: d.get(y, True), x)), arr))

tidy_valid = []
for cat in tidy_d.keys():
    valid = []
    for i in range(len(arr[0])):
        cols = list(map(lambda x: x[i], arr))
        if all(map(lambda x: check(x, cat), cols)):
            valid.append(i)
    tidy_valid.append([cat, valid])
tidy_valid.sort(key=lambda x: len(x[1]))
for i in range(len(tidy_valid) - 1, 0, -1):
    tidy_valid[i][1] = list(filter(lambda x: x not in tidy_valid[i - 1][1], tidy_valid[i][1]))
tidy_valid = dict(map(lambda x: [x[0], x[1][0]], tidy_valid))

res = 1
for k in tidy_valid:
    if "departure" in k:
        res *= t[tidy_valid[k]]
print("Part 2:", res)