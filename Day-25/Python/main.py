import time
cpk = int(input())
dpk = int(input())
m = 20201227

# 7**a == cpk mod 20201227
# 7**b == dpk mod 20201227
# find 7**(ab) mod 20201227
debug = False

p, s = 0, 1
a, b = -1, -1
while p <= m:
    if p % 10000 == 0 and debug:
        print("Checkpoint p =", p, "s =", s)
    if s % m == cpk:
        a = p
        if debug:
            print("Found a =", a) # 538014
            time.sleep(3)
    if s % m == dpk:
        b = p
        if debug:
            print("Found b =", b) # 5497777
            time.sleep(3)
    if a > 0 and b > 0:
        break
    p += 1
    s = (s * 7) % m
f = 1
for i in range(a):
    if i % 10000 == 0 and debug:
        print("Checking", i, f)
    f = (f * s) % m
print("Part 1:", f)
print("Part 2: THE END!")