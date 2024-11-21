import re

translations = []
with open("input.txt", "r") as f:
# with open("test_input.txt", "r") as f:
# with open("test_input2.txt", "r") as f:
    content = f.readlines()
    text = content[-1].strip()
    content = content[:-2]
    for line in content:
        line = line.strip().split()
        translations.append((line[0], line[-1]))

# Part 1
# vars = []
# for t in translations:
#     a = t[0]
#     locs = re.finditer(a, text)
#     if locs:
#         for loc in locs:
#             s,e = loc.span()
#             txt = list(text)
#             vars.append("".join(txt[:s] + list(t[1]) + txt[e:]))
# print(len(set(vars)))

# Part 2
translations = sorted(translations, key=lambda translations: len(translations[1]), reverse=True)
txt = text
count = 0
while txt != "e":
    for t in translations:
        a = t[1]
        locs = re.search(a, txt)
        if locs:
            s,e = locs.span()
            txt = list(txt)
            txt = "".join(txt[:s] + list(t[0]) + txt[e:])
            break
    count += 1
print(count)
