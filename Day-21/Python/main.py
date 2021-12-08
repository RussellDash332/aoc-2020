import sys

possible = {} # allergen -> set of ingredients
possible2 = {} # ingredient -> set of allergens
full_log = []
for line in sys.stdin:
    line = line.split(" (contains ")
    ings = line[0].split()
    full_log.extend(ings)
    alls = line[1].strip()[:-1].split(", ")
    for al in alls:
        possible[al] = possible.get(al, []) + ings
    for ing in ings:
        possible2[ing] = possible2.get(ing, []) + alls
full_alls = set(possible.keys())
full_ings = set(possible2.keys())

for k in possible:
    temp = {}
    for i in possible[k]:
        temp[i] = possible[k].count(i)
    possible[k] = temp
for k in possible2:
    temp = {}
    for i in possible2[k]:
        temp[i] = possible2[k].count(i)
    possible2[k] = temp

match = {}
for _ in range(len(full_alls)):
    for al in full_alls:
        cnts = possible.get(al, {}).values()
        if len(list(filter(lambda x: x == max(cnts), cnts))) == 1:
            ing = list(filter(lambda x: x[1] == max(cnts), possible[al].items()))[0][0]
            del possible[al]
            del possible2[ing]
            for k in possible:
                if ing in possible[k]:
                    del possible[k][ing]
            for k in possible2:
                if al in possible2[k]:
                    del possible2[k][al]
            match[al] = ing

print("Part 1:", len(list(filter(lambda x: x in possible2, full_log))))
print("Part 2:", ",".join(list(map(lambda x: x[1], sorted(match.items(), key=lambda y: y[0])))))