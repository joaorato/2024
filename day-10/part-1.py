import time

start_time = time.time()

with open("input.txt") as file:
    map = [[int(elem) for elem in line.strip()] for line in file]

trail_heads = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            trail_heads.append((i, j))


def is_out_of_bounds(i, j):
    return not 0 <= i < len(map) or not 0 <= j < len(map)


def move(x, i, j):
    if x == 9:
        nines.add((i, j))
    new_val = x + 1
    if is_out_of_bounds(i, j):
        return
    try:
        if map[i][j + 1] == new_val:
            possible_paths.append((i, j + 1, new_val))
            move(new_val, i, j + 1)
    except IndexError:
        pass
    try:
        if map[i][j - 1] == new_val:
            possible_paths.append((i, j - 1, new_val))
            move(new_val, i, j - 1)
    except IndexError:
        pass
    try:
        if map[i + 1][j] == new_val:
            possible_paths.append((i + 1, j, new_val))
            move(new_val, i + 1, j)
    except IndexError:
        pass
    try:
        if map[i - 1][j] == new_val:
            possible_paths.append((i - 1, j, new_val))
            move(new_val, i - 1, j)
    except IndexError:
        pass


all_count = 0
for trail_head in trail_heads:
    i = trail_head[0]
    j = trail_head[1]
    possible_paths = []
    nines = set()
    move(map[i][j], i, j)
    print(len(nines))
    all_count += len(nines)

print(all_count)

print("--- %s seconds ---" % (time.time() - start_time))
