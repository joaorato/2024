import time

start_time = time.time()

grid = {}
moves = []
with open("input.txt") as file:
    skip = 0
    content = file.readlines()
    for i, row in enumerate(content):
        if row == "\n":
            skip = i
            break
        for j, char in enumerate(row.strip()):
            grid[(i, j)] = char

    move_str = ""
    for x in range(skip + 1, len(content)):
        move_str += content[x].strip()
    moves = list(move_str)

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def push_box(pos, dir):
    # check what is in the new position
    new_pos = tuple(map(sum, zip(pos, dir)))
    char = grid.get(new_pos)
    if char == ".":
        grid.update({pos: "."})
        grid.update({new_pos: "O"})
        return True
    elif char == "#":
        return False
    elif char == "O":
        if push_box(new_pos, dir):
            grid.update({pos: "."})
            grid.update({new_pos: "O"})
            return True


def do_move(pos, dir):
    # check what is in the new position
    new_pos = tuple(map(sum, zip(pos, dir)))
    char = grid.get(new_pos)
    if char == ".":
        grid.update({pos: "."})
        grid.update({new_pos: "@"})
        return new_pos
    elif char == "#":
        return pos
    elif char == "O":
        if push_box(new_pos, dir):
            grid.update({pos: "."})
            grid.update({new_pos: "@"})
            return new_pos
        else:
            return pos


def find_start():
    for coords, char in grid.items():
        if char == "@":
            return coords


robot_pos = find_start()
for move in moves:
    robot_pos = do_move(robot_pos, directions[move])

score = 0
for coords, char in grid.items():
    if char == "O":
        score += 100 * coords[0]
        score += coords[1]

print(score)
print("--- %s seconds ---" % (time.time() - start_time))
