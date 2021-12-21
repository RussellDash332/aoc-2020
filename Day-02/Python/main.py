import sys

ans1 = 0
ans2 = 0
for line in sys.stdin:
    r, c, s = line.strip().split()
    a, b = list(map(int, r.split("-")))
    if a <= s.count(c[0]) <= b:
        ans1 += 1
    ans2 += int(s[a - 1] == c[0]) ^ int(s[b - 1] == c[0])
print("Part 1:", ans1)
print("Part 2:", ans2)