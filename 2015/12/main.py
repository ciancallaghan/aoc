import json
import re

def get_val(input):
    vals = re.findall(r"-?\d+", input)
    if len(vals) == 0:
        return 0
    vals = [int(i) for i in vals]
    return sum(vals)

# Part 1
with open("input.json", "r") as f:
    print(get_val(f.readline()))

# Part 2
def parse_json(data, val):
    if isinstance(data, int):
        return val + data
    elif isinstance(data, str):
        if data.isnumeric():
            return val + int(data)
        else:
            return val
    elif isinstance(data, dict):
        if "red" in data.values():
            return val
        for d in data.values():
            val = parse_json(d, val)
    else:
        for d in data:
            val = parse_json(d, val)

    return val

with open("input.json", "r") as f:
    data = json.load(f)
    print(parse_json(data, 0))
    
