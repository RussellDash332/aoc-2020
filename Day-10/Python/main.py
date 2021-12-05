import sys

j = []
for line in sys.stdin:
    j.append(int(line))
j.sort()

d1, d3 = 1, 1
for i in range(1, len(j)):
    if j[i] - j[i - 1] == 1:
        d1 += 1
    elif j[i] - j[i - 1] == 3:
        d3 += 1
print("Part 1:", d1 * d3)

dp = [0] * (max(j) + 1)
dp[0] = 1
for i in j:
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print("Part 2:", dp[-1])