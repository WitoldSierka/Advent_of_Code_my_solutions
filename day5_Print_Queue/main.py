import math
import os

file_path = "input.txt"
#file_path = "test.txt"

#set_of_rules: dict[int, list] = {}
set_of_rules: list[list[int]] = []
set_of_pages: list[list[int]] = []

if not os.path.isfile(file_path):
    print("Error: file not found")
else:
    print("File found")
    with open(file_path, "r") as f:
        is_first_part = True
        for line in f:
            if line.isspace():
                is_first_part = False
                continue
            if is_first_part:
                temp: list[str] = line.split("|")
                rule = list(map(int, temp))
                set_of_rules.append(rule)
            else:
                temp = line.split(",")
                pages = list(map(int, temp))
                set_of_pages.append(pages)

total = 0
rulebook: dict[int, list[int]] = dict()

for rules in set_of_rules:
    key = rules[1]
    value = rules[0]
    if key not in rulebook:
        rulebook[key] = [value]
    else:
        rulebook[key].append(value)

unordered: list[list[int]] = list()

for pages in set_of_pages:
    pages_in_order: bool = True
    for i in range(len(pages) - 1):
        if pages[i] not in rulebook.keys():
            continue
        for j in range(i + 1, len(pages)):
            if pages[j] in rulebook.get(pages[i]):
                pages_in_order = False
                break
        if not pages_in_order:
            break
    if not pages_in_order:
        unordered.append(pages)
        continue
    middle = math.floor(len(pages) / 2)
    total += pages[middle]

total2 = 0

for pages in unordered:
    for i in range(len(pages) - 1):
        if pages[i] not in rulebook.keys():
            continue
        index_is_bad = True
        while index_is_bad:
            temp: list[int] = list()
            for j in range(i + 1, len(pages)):
                if j >= len(pages):
                    break
                if pages[i] not in rulebook.keys():
                    break
                if pages[j] in rulebook.get(pages[i]):
                    temp.append(pages[j])
                    pages.remove(pages[j]) #implying all pages are unique
            if len(temp) == 0:
                index_is_bad = False
                break
            pages[i:i] = temp
    middle = math.floor(len(pages) / 2)
    total2 += pages[middle]

print(f"Total part 1: {total}")
print(f"Total part 2: {total2}")