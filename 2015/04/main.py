import hashlib

with open("input.txt", "r") as f:
    k = f.readline().strip()

    q = 0
    while not (hashlib.md5((k + str(q)).encode())).hexdigest().startswith("00000"):
        q += 1
    print(q)

    q = 0
    while not (hashlib.md5((k + str(q)).encode())).hexdigest().startswith("000000"):
        q += 1
    print(q)
