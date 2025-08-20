import copy
import os

file_path = "input.txt"
#file_path = "test.txt"
#file_path = "test2.txt"

lab: list[list[str]] = []

if not os.path.isfile(file_path):
    print(f"Error: File '{file_path}' not found.")
else:
    with open(file_path, "r") as f:
        for line in f:
            lab.append(list(line.strip("\n")))
        f.close()

class Guard:
    x: int = 0
    y: int = 0
    obstacle: list[str] = ["#", "0"]
    direction: str = "^"

guard = Guard()
found = False

for y in range(len(lab)):
    for x in range(len(lab[y])):
        if lab[y][x] == guard.direction:
            guard.x = x
            guard.y = y
            found = True
            break
    if found:
        break

total = 0
all_steps = 0
within_lab = True
START_POSITION: dict = {'x': guard.x, 'y': guard.y, 'direction': guard.direction}
put_obstacle = False
collision_with_old_obstacle = False
collision_with_old_path = False
obstacle_coords = [0,0]

def guard_move(lvl: list[list[str]]) -> None:
    global guard, within_lab, put_obstacle, steps_taken, collision_with_old_obstacle, obstacle_coords, collision_with_old_path
    if guard.direction == "^":
        if guard.y - 1 < 0:
            within_lab = False
        elif lvl[guard.y - 1][guard.x] in guard.obstacle:
            guard.direction = ">"
        elif put_obstacle:
            if "A" in lvl[guard.y - 1][guard.x]:
                collision_with_old_obstacle = True
                return
            elif not (lvl[guard.y - 1][guard.x] == "."):
                collision_with_old_path = True
                return
            lvl[guard.y - 1][guard.x] = "0"
            obstacle_coords = [guard.x, guard.y - 1]
            guard.direction = ">"
            put_obstacle = False
        else:
            steps_taken += 1
            guard.y -= 1
    elif guard.direction == ">":
        if guard.x + 1 >= len(lab[0]):
            within_lab = False
        elif lvl[guard.y][guard.x + 1] in guard.obstacle:
            guard.direction = "v"
        elif put_obstacle:
            if "A" in lvl[guard.y][guard.x + 1]:
                collision_with_old_obstacle = True
                return
            elif not (lvl[guard.y][guard.x + 1] == "."):
                collision_with_old_path = True
                return
            lvl[guard.y][guard.x + 1] = "0"
            obstacle_coords = [guard.x + 1, guard.y]
            guard.direction = "v"
            put_obstacle = False
        else:
            steps_taken += 1
            guard.x += 1
    elif guard.direction == "<":
        if guard.x - 1 < 0:
            within_lab = False
        elif lvl[guard.y][guard.x - 1] in guard.obstacle:
            guard.direction = "^"
        elif put_obstacle:
            if "A" in lvl[guard.y][guard.x - 1]:
                collision_with_old_obstacle = True
                return
            elif not (lvl[guard.y][guard.x - 1] == "."):
                collision_with_old_path = True
                return
            lvl[guard.y][guard.x - 1] = "0"
            obstacle_coords = [guard.x - 1, guard.y]
            guard.direction = "^"
            put_obstacle = False
        else:
            steps_taken += 1
            guard.x -= 1
    else: #guard.direction == "v": - no need to check that.
        if guard.y + 1 >= len(lab):
            within_lab = False
        elif lvl[guard.y + 1][guard.x] in guard.obstacle:
            guard.direction = "<"
        elif put_obstacle:
            if "A" in lvl[guard.y + 1][guard.x]:
                collision_with_old_obstacle = True
                return
            elif not (lvl[guard.y + 1][guard.x] == "."):
                collision_with_old_path = True
                return
            lvl[guard.y + 1][guard.x] = "0"
            obstacle_coords = [guard.x, guard.y + 1]
            guard.direction = "<"
            put_obstacle = False
        else:
            steps_taken += 1
            guard.y += 1

steps_taken = 0
temp_lab = copy.deepcopy(lab)

while within_lab:
    if not temp_lab[guard.y][guard.x] == "X":
        temp_lab[guard.y][guard.x] = "X"
        total += 1
    guard_move(lab)
    all_steps += 1

total2 = 0
put_obstacle = False

for i in range(all_steps):
    guard.x = START_POSITION['x']
    guard.y = START_POSITION['y']
    guard.direction = START_POSITION['direction']
    steps_taken = 0
    temp_lab = copy.deepcopy(lab)
    obstacle_was_put = False
    put_obstacle = False
    within_lab = True
    collision_with_old_obstacle = False
    collision_with_old_path = False
    obstacle_coords = [0,0]
    while within_lab:
        if steps_taken == i and not obstacle_was_put:
            obstacle_was_put = True
            put_obstacle = True
        guard_move(temp_lab)
        if collision_with_old_obstacle or collision_with_old_path:
            break
        if obstacle_was_put and within_lab:
            if guard.direction in temp_lab[guard.y][guard.x]:
                total2 += 1
                print(f"Loop occurrence nr {total2} found in {i}/{all_steps} possibilities.")
                lab[obstacle_coords[1]][obstacle_coords[0]] = "A"
                break
        if temp_lab[guard.y][guard.x] == ".":
            temp_lab[guard.y][guard.x] = guard.direction
        else:
            temp_lab[guard.y][guard.x] += guard.direction



print(f"Total part 1: {total}")
print(f"Total part 2: {total2}")