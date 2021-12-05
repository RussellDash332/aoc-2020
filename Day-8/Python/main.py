import sys

cmds = []
for line in sys.stdin:
    line = line.split()
    cmds.append([line[0], int(line[1])])

visited = {}
pos, acc = 0, 0
while not visited.get(pos, False):
    visited[pos] = True
    if cmds[pos][0] == "jmp":
        pos = max(0, pos + cmds[pos][1])
    elif cmds[pos][0] == "acc":
        acc += cmds[pos][1]
        pos += 1
    else:
        pos += 1
print("Part 1:", acc)

def check(p):
    if cmds[p][0] == "acc":
        return False
    visited = {}
    pos, acc = 0, 0
    while pos not in visited:
        if pos >= len(cmds):
            return (True, acc)
        visited[pos] = True
        k = cmds[pos][0]
        if pos == p:
            if k == "jmp":
                k = "nop"
            else:
                k = "jmp"
        if k == "jmp":
            pos = max(0, pos + cmds[pos][1])
        elif k == "acc":
            acc += cmds[pos][1]
            pos += 1
        else:
            pos += 1
    return False
for i in range(len(cmds)):
    r = check(i)
    if r:
        print("Part 2:", r[1])