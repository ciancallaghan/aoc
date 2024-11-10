class Reindeer:
    def __init__(self, name, speed, time, rest):
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest
        self.travel = 0
        self.points = 0

# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    reindeer = []
    for line in f.readlines():
        line = line.split()
        reindeer.append(Reindeer(line[0], int(line[3]), int(line[6]), int(line[-2])))        

# t = 1
# t = 11
# t = 1000
t = 2503

# Part1
max_dist = 0
for r in reindeer:
    full = t // (r.time + r.rest)
    r.travel += full * r.time * r.speed
    rem = t % (r.time + r.rest)
    if rem < r.time:
        r.travel += rem * r.speed
    else:
        r.travel += r.time * r.speed
    if r.travel >= max_dist:
        max_dist = r.travel
print(max_dist)

# Part 2
for r in reindeer:
    r.travel = 0

for i in range(t):
    for r in reindeer:
        rem = i % (r.time + r.rest)
        if rem < r.time:
            r.travel += r.speed
    max_travel = max([a.travel for a in reindeer])
    for r in reindeer:
        if r.travel == max_travel:
            r.points += 1

print(max([a.points for a in reindeer]))
