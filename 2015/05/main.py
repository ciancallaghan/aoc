import re

with open("input.txt", "r") as f:
    nice_strings = 0

    for line in f.readlines():
        if "ab" in line:
            continue
        elif "cd" in line:
            continue
        elif "pq" in line:
            continue
        elif "xy" in line:
            continue

        if (line.count("a") + line.count("e") + line.count("i") + line.count("o") + line.count("u")) < 3:
            continue

        if not re.search(r"(.)\1{1,}", line):
            continue

        nice_strings += 1

print(nice_strings)

with open("input.txt", "r") as f:
    nice_strings = 0

    for line in f.readlines():
        if not re.search(r"(.).\1", line):
            continue

        if not re.search(r"(..).*\1", line):
            continue

        nice_strings += 1

print(nice_strings)
