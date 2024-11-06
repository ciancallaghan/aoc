with open("input.txt", "r") as f:
    total = 0
    ribbon_total = 0
    for line in f.readlines():
        # l,w,h
        line = line.strip().split("x")
        line = [int(i) for i in line]
        # size [l*w, w*h, h*l]
        sizes = [line[0]*line[1], line[1]*line[2], line[0]*line[2]]
        surface_area = 2 * sizes[0] + 2 * sizes[1] + 2 * sizes[2] + min(sizes)
        total += surface_area

        line.sort()
        ribbon_length = line[0]*2 + line[1]*2
        bow_length = line[0] * line[1] * line[2]
        ribbon_total += (ribbon_length + bow_length)

print(total)
print(ribbon_total)
