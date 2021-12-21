import sys

m = []
for line in sys.stdin:
    m.append(list(line.strip()))

def do_slope(dr, dd):
    c = len(m[0])
    y, x = 0, 0
    ans = 0
    while y < len(m):
        if m[y][x] == "#":
            ans += 1
        x = (x + dr) % c
        y += dd
    return ans

print("Part 1:", do_slope(3, 1))
t = 1
for slope in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    t *= do_slope(*slope)
print("Part 2:", t)