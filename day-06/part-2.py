import time

start_time = time.time()

map = []

with open("input.txt") as file:
    map = [[elem for elem in line] for line in file]


def find_start():
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                return i, j


directions_list = ["up", "right", "down", "left"]

directions = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}


def move(i, j, direction):
    i += directions[direction][0]
    j += directions[direction][1]

    return i, j


def turn_right(current_direction):
    current_index = directions_list.index(current_direction)

    new_index = (current_index + 1) % len(directions)

    return directions_list[new_index]


def is_out_of_bounds(i, j):
    return not 0 <= i < len(map) or not 0 <= j < len(map[0])


def check_for_loop(start_i, start_j, start_direction, obstruction):
    current_direction = start_direction
    current_i, current_j = start_i, start_j
    visited_positions = set()

    map[obstruction[0]][obstruction[1]] = "#"

    while True:
        # Check if the current position and direction form a loop (if we have been here before with same direction)
        if (current_i, current_j, current_direction) in visited_positions:
            map[obstruction[0]][obstruction[1]] = "."
            return True
        visited_positions.add((current_i, current_j, current_direction))

        # try to move
        new_i, new_j = move(current_i, current_j, current_direction)
        if is_out_of_bounds(new_i, new_j):
            break
        if map[new_i][new_j] == "#":
            # instead change direction
            current_direction = turn_right(current_direction)
        else:
            current_i, current_j = new_i, new_j

    map[obstruction[0]][obstruction[1]] = "."

    return False


start_i, start_j = find_start()
start_direction = "up"

obstacle_positions = 0
for i in range(len(map)):
    for j in range(len(map)):
        if (i, j) != (start_i, start_j) and map[i][j] == ".":
            if check_for_loop(start_i, start_j, start_direction, obstruction=(i, j)):
                obstacle_positions += 1


print(obstacle_positions)

print("--- %s seconds ---" % (time.time() - start_time))
