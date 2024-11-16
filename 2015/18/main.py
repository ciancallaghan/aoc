# ll = 6
ll = 100
new_grid = []

# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    for c in f.read().strip():
        if not c or c == "\n":
            continue
        new_grid.append(c)

new_grid[0] = "#"
new_grid[ll-1] =  "#"
new_grid[ll*ll-1] = "#"
new_grid[ll*ll-ll] = "#"

for i in range(100):
# for i in range(5):
    light_grid = new_grid.copy()
    new_grid = []
    for i, l in enumerate(light_grid):
        ons = 0
        if i-1 >= 0 and i%ll != 0:
            if light_grid[i-1] == "#":
                ons +=1
        if i-ll+1 >= 0 and i%ll != (ll-1):
            if light_grid[i-ll+1] == "#":
                ons += 1
        if i-ll >= 0:
            if light_grid[i-ll] == "#":
                ons += 1
        if i-ll-1 >= 0 and i%ll != 0:
            if light_grid[i-ll-1] == "#":
                ons += 1
        if i+1 < len(light_grid) and i%ll != (ll-1):
            if light_grid[i+1] == "#":
                ons += 1
        if i+ll-1 < len(light_grid) and i%ll !=  0:
            if light_grid[i+ll-1] == "#":
                ons += 1
        if i+ll < len(light_grid):
            if light_grid[i+ll] == "#":
                ons += 1
        if i+ll+1 < len(light_grid) and i%ll != (ll-1):
            if light_grid[i+ll+1] == "#":
                ons += 1

        if l == "#" and (ons == 2 or ons == 3):
            new_grid.append("#")
        elif ons == 3:
            new_grid.append("#")
        else:
            new_grid.append(".")
    new_grid[0] = "#"
    new_grid[ll-1] =  "#"
    new_grid[ll*ll-1] = "#"
    new_grid[ll*ll-ll] = "#"

print(new_grid.count("#"))
# print(new_grid)
