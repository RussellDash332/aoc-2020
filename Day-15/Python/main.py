nums = list(map(int, input().split(",")))
mem = {}
rev = {}

for i in range(len(nums)):
    mem[nums[i]] = mem.get(nums[i], []) + [i]
    rev[i] = nums[i]
i = len(nums)
while True:
    if len(mem[rev[i - 1]]) == 1:
        rev[i] = 0
        mem[0] = (mem.get(0, []) + [i])[-2:]
    else:
        s = mem[rev[i - 1]][-1] - mem[rev[i - 1]][-2]
        rev[i] = s
        mem[s] = (mem.get(s, []) + [i])[-2:]
    if i + 1 == 2020:
        print("Part 1:", rev[i])
    if i + 1 == 30000000:
        print("Part 2:", rev[i])
        break
    i += 1