import sys, re

rule = {}
freq = {}
for line in sys.stdin:
    cols = re.findall(r"[^\d\s][A-Za-z\s]*(?= bag)", line)
    if "contain" in cols[0]:
        cols[0] = cols[0][:cols[0].find(" bag")]
    rule[cols[0]] = cols[1:]
    freq[cols[0]] = list(map(int, filter(lambda x: x, re.findall(r"\d*", line))))

def check(col):
    if col not in rule:
        return False
    elif "shiny gold" in rule[col]:
        return True
    else:
        return any(list(map(check, rule[col])))

def nums(col):
    if col not in rule:
        return 1
    return 1 + sum([freq[col][i] * nums(rule[col][i]) for i in range(len(freq[col]))])

print("Part 1:", len(list(filter(check, rule.keys()))))
print("Part 2:", nums("shiny gold") - 1)