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
        char_count = 0
        for j, char in enumerate(row.strip()):
            if char == "@":
                grid[(i, char_count)] = char
                grid[(i, char_count + 1)] = "."
            elif char == "O":
                grid[(i, char_count)] = "["
                grid[(i, char_count + 1)] = "]"
            else:
                grid[(i, char_count)] = char
                grid[(i, char_count + 1)] = char
            char_count += 2

    move_str = ""
    for x in range(skip + 1, len(content)):
        move_str += content[x].strip()
    moves = list(move_str)

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


# a lot of duplicated code with can_move() but couldn't find a better way
def do_move(pos, dir):
    # check what is in the new position
    new_pos = tuple(map(sum, zip(pos, dir)))
    char = grid.get(new_pos)
    if char == ".":
        return True
    elif char == "#":
        return False
    new_new_pos = tuple(map(sum, zip(new_pos, dir)))
    if dir == (-1, 0) or dir == (1, 0):
        if (
            char == "["
            and do_move(new_pos, dir)
            and do_move(tuple(map(sum, zip(new_pos, (0, 1)))), dir)
        ):
            new_pos_right = tuple(map(sum, zip(new_pos, (0, 1))))
            char_right = grid.get(new_pos_right)
            new_new_pos_right = tuple(map(sum, zip(new_pos_right, dir)))

            grid.update({new_new_pos: char})
            grid.update({new_pos: "."})
            grid.update({new_new_pos_right: char_right})
            grid.update({new_pos_right: "."})
            return True

        if (
            char == "]"
            and do_move(new_pos, dir)
            and do_move(tuple(map(sum, zip(new_pos, (0, -1)))), dir)
        ):
            new_pos_left = tuple(map(sum, zip(new_pos, (0, -1))))
            char_left = grid.get(new_pos_left)
            new_new_pos_left = tuple(map(sum, zip(new_pos_left, dir)))

            grid.update({new_new_pos: char})
            grid.update({new_pos: "."})
            grid.update({new_new_pos_left: char_left})
            grid.update({new_pos_left: "."})
            return True
    else:
        if do_move(new_pos, dir):
            grid.update({new_new_pos: char})
            grid.update({new_pos: "."})
            return True

    return False


def can_move(pos, dir):
    # check what is in the new position
    new_pos = tuple(map(sum, zip(pos, dir)))
    char = grid.get(new_pos)
    if char == ".":
        return True
    elif char == "#":
        return False
    # if we move vertically we need to be careful with "shifted" boxes
    if dir == (-1, 0) or dir == (1, 0):
        if (
            char == "["
            and can_move(new_pos, dir)
            and can_move(
                tuple(map(sum, zip(new_pos, (0, 1)))), dir
            )  # if char can be moved and the correspondent "]" too
        ):
            return True
        if (
            char == "]"
            and can_move(new_pos, dir)
            and can_move(
                tuple(map(sum, zip(new_pos, (0, -1)))), dir
            )  # if char can be moved and the correspondent "[" too
        ):
            return True
    else:
        if can_move(new_pos, dir):
            return True
    return False


def find_start():
    for coords, char in grid.items():
        if char == "@":
            return coords


def draw_grid():
    line = ""
    x = 0
    for coord, char in grid.items():
        if coord[0] == x:
            line += char
        else:
            print(line)
            x = coord[0]
            line = char
    print(line)


robot_pos = find_start()
i = 0
for move in moves:
    i += 1
    # draw_grid()
    dir = directions[move]
    if can_move(robot_pos, dir):
        do_move(robot_pos, dir)
        new_robot_pos = tuple(map(sum, zip(robot_pos, dir)))
        grid.update({new_robot_pos: "@"})
        grid.update({robot_pos: "."})
        robot_pos = new_robot_pos

    # print(i, move)


score = 0
for coords, char in grid.items():
    if char == "[":
        score += 100 * coords[0]
        score += coords[1]


print(score)
print("--- %s seconds ---" % (time.time() - start_time))
