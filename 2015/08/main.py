with open("input.txt", "r") as f:
    decode_res = 0
    encode_res = 0
    for line in f.readlines():
        line = line.strip()

        d = line[1:-1].encode("utf-8").decode("unicode-escape")
        decode_res += (len(line) - len(d))

        e = line.encode("unicode-escape")
        encode_res += (len(e) + e.count(b'"') + 2 - len(line))

    print(decode_res)
    print(encode_res)
