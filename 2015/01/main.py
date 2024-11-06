with open("input.txt", "r") as f:
    counter = 0
    pos = 0
    for i,c in enumerate(f.read()):
        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1

        if counter == -1 and pos == 0:
            pos = i + 1

print(counter)
print(pos)
