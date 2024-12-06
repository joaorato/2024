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
visited = []
visited.append(find_start())


def move(i, j, direction):
    i += directions[direction][0]
    j += directions[direction][1]

    return i, j


def turn_right(current_direction):
    current_index = directions_list.index(current_direction)

    new_index = (current_index + 1) % len(directions)

    return directions_list[new_index]


def is_out_of_bounds(i, j):
    return not 0 <= i < len(map) or not 0 <= j < len(map)


current_direction = "up"
current_i = visited[-1][0]
current_j = visited[-1][1]
while True:
    # try to move
    new_i, new_j = move(current_i, current_j, current_direction)
    if is_out_of_bounds(new_i, new_j):
        break

    if map[new_i][new_j] == "#":
        # instead change direction and try again
        current_direction = turn_right(current_direction)
        continue
    if (new_i, new_j) not in visited:
        visited.append((new_i, new_j))
    current_i = new_i
    current_j = new_j

print(len(visited))
print("--- %s seconds ---" % (time.time() - start_time))
