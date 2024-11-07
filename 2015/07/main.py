circuit = dict()
evaluated = dict()
with open("input.txt", "r") as f:
    data = f.readlines()
    for line in data:
        line = line.strip().split(" -> ")
        circuit[line[1]] = line[0]
 
def evaluate(wire):
    if wire in evaluated:
        return int(evaluated[wire])
    if wire.isnumeric():
        return int(wire)

    ops = circuit[wire].split()
    if len(ops) == 1:
        evaluated[wire] = evaluate(ops[0])
    else:
        if ops[0] == "NOT":
            evaluated[wire] = ~evaluate(ops[1]) & 0xFFFF
        if ops[1] == "AND":
            evaluated[wire] = evaluate(ops[0]) & evaluate(ops[2])
        if ops[1] == "OR":
            evaluated[wire] = evaluate(ops[0]) | evaluate(ops[2])
        if ops[1] == "LSHIFT":
            evaluated[wire] = evaluate(ops[0]) << evaluate(ops[2])
        if ops[1] == "RSHIFT":
            evaluated[wire] = evaluate(ops[0]) >> evaluate(ops[2])

    return evaluated[wire]

print(evaluate("a"))

circuit = dict()
evaluated = dict()
with open("input.txt", "r") as f:
    data = f.readlines()
    for line in data:
        line = line.strip().split(" -> ")
        circuit[line[1]] = line[0]

evaluated = {"b": "956"}
print(evaluate("a"))
