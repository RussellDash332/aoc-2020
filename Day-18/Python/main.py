import sys

def calculate(exp):
    stack = []
    stack2 = []
    for i in exp:
        if i != ")":
            stack.append(i)
        else:
            while stack[-1] != "(":
                stack2.append(stack.pop())
            stack.pop()
            stack.append(calculate(stack2[::-1]))
            stack2.clear()
    ans = stack[0]
    for i in range(1, len(stack), 2):
        ans = str(eval(ans + stack[i] + stack[i + 1]))
    return ans

def calculate2(exp):
    stack = []
    stack2 = []
    for i in exp:
        if i != ")":
            stack.append(i)
        else:
            while stack[-1] != "(":
                stack2.append(stack.pop())
            stack.pop()
            stack.append(calculate2(stack2[::-1]))
            stack2.clear()
    stack2 = []
    for i in range(len(stack)):
        if not stack2 or stack2[-1] != "+":
            stack2.append(stack[i])
        else:
            tmp = stack[i] + stack2.pop() + stack2.pop()
            stack2.append(str(eval(tmp)))
    return str(eval(str().join(stack2)))

ans1, ans2 = 0, 0
for line in sys.stdin:
    res = list(line.replace(" ", "").strip())
    ans1 += int(calculate(res))
    ans2 += int(calculate2(res))
print("Part 1:", ans1)
print("Part 2:", ans2)