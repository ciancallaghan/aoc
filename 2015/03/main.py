with open("input.txt", "r") as f:
    lat = 0
    lon = 0
    coords = {(0, 0)}

    for c in f.read():
        if c == ">":
            lon += 1
        elif c == "<":
            lon -=1
        elif c == "^":
            lat += 1
        elif c == "v":
            lat -= 1
        coords.add((lat, lon))

print(len(coords))

with open("input.txt", "r") as f:
    slat = 0
    slon = 0
    rlat = 0
    rlon = 0
    coords = {(0,0)}
    for i, c in enumerate(f.read().strip()):
        if i % 2 == 0:
            if c == ">":
                slon += 1
            elif c == "<":
                slon -= 1
            elif c == "^":
                slat += 1
            elif c == "v":
                slat -= 1
        else:
            if c == ">":
                rlon += 1
            elif c == "<":
                rlon -= 1
            elif c == "^":
                rlat += 1
            elif c == "v":
                rlat -= 1
        coords.add((slon, slat))
        coords.add((rlon, rlat))

print(len(coords))
