from sympy.ntheory.modular import crt

n = int(input())
line = input().strip().split(",")
ids = list(map(int, filter(lambda x: x != "x", line)))
k = min(ids, key=lambda x: -n % x)
print("Part 1:", k * (-n % k))

m, v = [], []
for i in range(len(line)):
    if line[i] != "x":
        m.append(int(line[i]))
        v.append(-i)
print("Part 2:", crt(m, v)[0])