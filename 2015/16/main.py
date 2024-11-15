import re

s = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

vals = ["children", "cats", "samoyeds", "pomeranians", "akitas", "vizslas", "goldfish", "trees", "cars", "perfumes"]

with open("input.txt", "r") as f:
    for line in f.readlines():
        cor = True
        for val in vals:
            r = re.search(f"{val}" + r": \d", line)
            if not r:
                continue
            if val == "cats" or val == "trees":
                if s[val] >= int(r.group()[-1]):
                    cor = False 
                    break
            elif val == "pomeranians" or val == "goldfish":
                if s[val] <= int(r.group()[-1]):
                    cor = False
                    break
            elif s[val] != int(r.group()[-1]):
                cor = False
                break
        if cor:
            print(line)
            break
