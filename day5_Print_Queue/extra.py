import os

#file_path = "input.txt"
file_path = "test.txt"

if not os.path.exists(file_path):
    print(f"The '{file_path}' does not exist")
    if not os.path.isfile(file_path):
        print(f"'{file_path}' is not a file")


raw_set_of_rules = []
set_of_rules = []
raw_set_of_pages = []
set_of_pages = []

file = open("test.txt", "r")

for line in file:
    if not line.isspace():
        line = line.strip("\n")
        raw_set_of_rules.append(line)
    else:
        break

for line in file:
    line = line.strip("\n")
    raw_set_of_pages.append(line)

file.close()

total = 0

for rules in raw_set_of_rules:
    rules = rules.split("|")
    rules = list(map(int, rules))
    set_of_rules.append(rules)

for pages in raw_set_of_pages:
    pages = pages.split(",")
    pages = [int(el) for el in pages]
    set_of_pages.append(pages)
        
for pages in set_of_pages:
    pages_OK = True
    for i in range(1, len(pages)):
        for rule in set_of_rules:
            if rule[1] == pages[i]:
                for j in range(i + 1, len(pages)):
                    if rule[0] == pages[j]:
                        print("Wrong_Order", rule[0], pages[j])
                        pages_OK = False
                        break
            if not pages_OK:
                break
        if not pages_OK:
            break
                        

print(f"Result is {total}.")