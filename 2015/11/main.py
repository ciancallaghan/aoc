import re

input = "hepxcrrq"

def get_pass(input):
    input = list(input)[::-1]
    valid = False
    while not valid:
        rule1 = False
        rule2 = False
        for i in range(len(input)):
            if ord(input[i]) < ord("z"):
                # Rule 2
                if ord(input[i]) + 1 == ord("i") or ord(input[i]) + 1 == ord("l") or ord(input[i]) + 1 == ord("o"):
                    input[i] = chr(ord(input[i]) + 2)
                else:
                    input[i] = chr(ord(input[i]) + 1)
                break
            else:
                for j in range(i+1):
                    input[j] = "a"

        # Rule 1
        x = "".join(input[::-1])
        for i in range(len(x)-2):
            if ord(x[i])+1 == ord(x[i+1]) and ord(x[i+1])+1 == ord(x[i+2]):
                rule1 = True

        # Rule 3
        if len(re.findall(r"(\w)\1", x)) > 1:
            rule2 = True

        # Valid
        if rule1 and rule2:
            valid = True
    return x

part1 = get_pass("hepxcrrq")
print(part1)
part2 = get_pass(part1)
print(part2)
