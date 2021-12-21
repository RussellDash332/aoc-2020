import sys

passport = {}
ans1, ans2 = 0, 0
for line in sys.stdin:
    line = line.strip().split()
    if not line:
        passport["cid"] = 0
        if len(passport) == 8:
            ans1 += 1
            ans2 += int(("1920" <= passport["byr"] <= "2002") and \
                ("2010" <= passport["iyr"] <= "2020") and \
                ("2020" <= passport["eyr"] <= "2030") and \
                (
                    (passport["hgt"][-2:] == "cm" and "150" <= passport["hgt"][:-2] <= "193") or \
                    (passport["hgt"][-2:] == "in" and "59" <= passport["hgt"][:-2] <= "76")
                ) and \
                (
                    passport["hcl"][0] == "#" and \
                    sum(map(lambda x: int(x in [str(i) for i in range(10)] + ["a", "b", "c", "d", "e", "f"]), passport["hcl"][1:]))
                ) and \
                (passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and \
                (len(passport["pid"]) == 9)
                )
        passport = {}
    else:
        for data in line:
            data = data.split(":")
            passport[data[0]] = data[1]
print("Part 1:", ans1)
print("Part 2:", ans2)