import sys

nums = []
for line in sys.stdin:
    nums.append(int(line))
for i in range(25, len(nums)):
    sums = {}
    for j in range(25):
        for k in range(j + 1, 25):
            sums[nums[i - j - 1] + nums[i - k - 1]] = True
    if nums[i] not in sums:
        invalid = nums[i]
        print("Part 1:", nums[i])
        break

for i in range(len(nums)):
    check = [nums[i]]
    for j in range(i + 1, len(nums)):
        check.append(nums[j])
        if sum(check) == invalid:
            print("Part 2:", min(check) + max(check))
            sys.exit(0)
