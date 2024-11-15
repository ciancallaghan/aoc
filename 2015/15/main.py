import itertools

class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.cap = int(capacity)
        self.dur = int(durability)
        self.fla = int(flavor)
        self.tex = int(texture)
        self.cal = int(calories)

def main():
    ingredients = []
    # with open("test_input.txt", "r") as f:
    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.replace(":", "").replace(",", "").split()
            ing = Ingredient(line[0], line[2], line[4], line[6], line[8], line[10])
            ingredients.append(ing)

    all_recipes = itertools.combinations_with_replacement(ingredients, 100)
    best = 0
    best_cal = 0
    for recipe in all_recipes:
        cap, dur, fla, tex, cal = 0, 0, 0, 0, 0
        for i in ingredients:
            c = recipe.count(i)
            cap += i.cap * c
            dur += i.dur * c
            fla += i.fla * c
            tex += i.tex * c
            cal += i.cal * c
        if cap < 0 or dur < 0 or fla < 0 or tex < 0:
            val = 0
        else:
            val = cap * dur * fla * tex
        if val > best:
            best = val
        if cal == 500:
            if val > best_cal:
                best_cal = val
    print(best)
    print(best_cal)
           

main()
