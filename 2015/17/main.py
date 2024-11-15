import itertools

containers = []
valid = []
# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    for line in f.readlines():
        containers.append(int(line.strip())) 
for k in range(len(containers)):
    combinations = itertools.combinations(containers, k)
    for c in combinations:
        # if sum(c) == 25:
        if sum(c) == 150:
            valid.append(c)

print(len(valid))
min_len = min([len(i) for i in valid])
count = 0
for v in valid:
    if len(v) == min_len:
        count += 1
print(count)
