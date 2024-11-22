import itertools

class Item:
    def __init__(self, name, gold, damage, armor):
        self.name = name
        self.gold = int(gold)
        self.damage = int(damage)
        self.armor = int(armor)

# Shop setup
with open("items.txt", "r") as f:
    items = []
    batch = []
    for line in f.readlines():
        if line == "\n":
            items.append(batch)
            batch = []
            continue
        line = line.strip().split(",")
        i = Item(line[0].strip(), line[1].strip(), line[2].strip(), line[3].strip())
        batch.append(i)
    items.append(batch)
weapons = items[0]
armor = items[1]
rings = items[2]

# Possible gear combos
w = list(itertools.product(weapons))
wa = list(itertools.product(weapons, armor))
wr = list(itertools.product(weapons, rings))
wrr = itertools.product(weapons, rings, rings)
wrr = [x for x in wrr if x[1] != x[2]]
war = list(itertools.product(weapons, armor, rings))
warr = itertools.product(weapons, armor, rings, rings)
warr = [x for x in warr if x[2] != x[3]]
combos = w + wa + wr + wrr + war + warr

# Enemy setup
# with open("test_input.txt", "r") as f:
with open("input.txt", "r") as f:
    content = f.readlines()
    hp = int(content[0].strip().split(":")[-1])
    damage = int(content[1].strip().split(":")[-1])
    armor = int(content[2].strip().split(":")[-1])
    e = [hp, damage, armor]

best_gold = 10000000
worst_gold = 0
for c in combos:
    gold = sum([x.gold for x in c])
    # Player setup
    me = [100, 0, 0]
    me[1] = sum([x.damage for x in c])
    me[2] = sum([x.armor for x in c])
    # Enemy setup
    enemy = e.copy()
    # Gameplay Loop
    while True:
        enemy[0] -= max(1, me[1] - enemy[2])
        if enemy[0] <= 0:
            if gold < best_gold:
                best_gold = gold
            break
        me[0] -= max(1, enemy[1] - me[2])
        if me[0] <= 0:
            if gold >= worst_gold:
                worst_gold = gold
            break
print(best_gold)
print(worst_gold)
