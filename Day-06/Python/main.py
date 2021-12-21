import sys

d, c, ans1, ans2 = {}, 0, 0, 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        ans1 += len(d)
        ans2 += len(list(filter(lambda x: d[x] == c, d.keys())))
        c, d = 0, {}
    else:
        for i in line:
            d[i] = d.get(i, 0) + 1
        c += 1

ans1 += len(d)
ans2 += len(list(filter(lambda x: d[x] == c, d.keys())))
print("Part 1:", ans1)
print("Part 2:", ans2)