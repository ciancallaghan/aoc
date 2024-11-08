def calc(input: str, start, end):
    if start == end:
        # print(input)
        print(len(input))
        return

    out = ""
    if len(input) == 1:
        out = f"1{input[0]}"
    elif len(input) == 2:
        if input[0] == input[1]:
            out = f"2{input[0]}"
        else:
            out = f"1{input[0]}1{input[1]}"
    else:
        count = 1
        i = 0
        while i < len(input)-1:
            if input[i] != input[i+1]:
                out += f"{count}{input[i]}"
                count = 1
            else:
                count += 1
            i += 1
        out += f"{count}{input[i]}"

    calc(out, start+1, end)

# Part 1
calc("1321131112", 0, 40)
# Part 2
calc("1321131112", 0, 50)
