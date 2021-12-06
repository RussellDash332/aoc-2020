import sys
from copy import deepcopy

rule = {}
rule_done = False
words = []
for line in sys.stdin:
    if not rule_done:
        line = line.strip().split(": ")
        if line == ['']:
            rule_done = True
        else:
            rule[int(line[0])] = line[1:]
    else:
        words.append(line.strip())


for i in rule:
    rule[i] = rule[i][0].split("|")
    if '"' in rule[i][0]:
        rule[i] = rule[i][0][1:-1]
    else:
        rule[i] = list(map(lambda x: list(map(int, x.split())), rule[i]))

def find_all(i):
    ru = rule[i]

    if type(ru) == str:
        return [ru]
    else:
        res = []
        for sublist in ru:
            temp = find_all(sublist[0])
            for num in sublist[1:]:
                t = []
                temp2 = find_all(num)
                for el in temp2:
                    t.extend(list(map(lambda x: x + el, temp)))
                temp = t
            res.extend(temp)
        return res

valid = find_all(0)
print("Part 1:", len(list(filter(lambda x: x in valid, words))))

ans = 0
ftt = find_all(42)
tto = find_all(31)
def check(word):
    i, j = 0, 0
    while word:
        have = False
        for m in ftt:
            if word.startswith(m):
                word = word[len(m):]
                i += 1
                have = True
        if not have:
            break
    while word:
        have = False
        for m in tto:
            if word.startswith(m):
                word = word[len(m):]
                j += 1
                have = True
        if not have:
            break
    return i > 0 and j > 0 and i > j and not word
print("Part 2:", len(list(filter(check, words))))