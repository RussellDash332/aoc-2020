import sys

y = []
for line in sys.stdin:
    y.append(int(line))

for i in range(len(y)):
    for j in range(i, len(y)):
        if y[i] + y[j] == 2020:
            print("Part 1:", y[i] * y[j])
        for k in range(j, len(y)):
            if y[i] + y[j] + y[k] == 2020:
                print("Part 2:", y[i] * y[j] * y[k])