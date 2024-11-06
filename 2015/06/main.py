light_grid = [[False for i in range(1000)] for j in range(1000)]
light_grid = [[0 for i in range(1000)] for j in range(1000)]

with open("input.txt", "r") as f:
    data = f.read().strip()
    data = data.replace("turn on", "on")
    data = data.replace("turn off", "off")
    data = data.split("\n")
    for line in data:
        line = line.split()
        s = [int(a) for a in line[1].split(",")]
        e = [int(a) for a in line[3].split(",")]
        for i in range(s[0], e[0]+1):
            for j in range(s[1], e[1]+1):
                if line[0] == "on":
                    # light_grid[i][j] = True
                    light_grid[i][j] += 1
                elif line[0] == "off":
                    # light_grid[i][j] = False
                    if (light_grid[i][j] - 1) >= 0:
                        light_grid[i][j] -= 1
                elif line[0] == "toggle":
                    # light_grid[i][j] = not light_grid[i][j]
                    light_grid[i][j] += 2

on_lights = 0
for line in light_grid:
    on_lights += sum(line)
    # on_lights += line.count(True)
print(on_lights)
