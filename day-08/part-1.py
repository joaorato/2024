import time
from itertools import combinations

start_time = time.time()

map = []

with open("input.txt") as file:
    map = [[elem for elem in line.strip()] for line in file]


def is_out_of_bounds(i, j):
    return not 0 <= i < len(map) or not 0 <= j < len(map)


anti_nodes = set()


def create_anti_node(i1, j1, i2, j2):
    # 1,8; 2,5 -> -1,3 and (1, -3)
    di = i1 - i2
    dj = j1 - j2

    anti_node1 = (i1 + di, j1 + dj)
    anti_node2 = (i2 - di, j2 - dj)

    if not is_out_of_bounds(*anti_node1):
        anti_nodes.add(anti_node1)
    if not is_out_of_bounds(*anti_node2):
        anti_nodes.add(anti_node2)


# save coordenates of each character
char_coords = {}

for i in range(len(map)):
    for j in range(len(map[i])):
        char = map[i][j]
        if char != ".":
            if char not in char_coords:
                char_coords[char] = []
            char_coords[char].append((i, j))

# look into each character's coordinates for the possible pairs
char_pairs = {}
for char, coords in char_coords.items():
    if len(coords) > 1:
        char_pairs[char] = list(combinations(coords, 2))

for pairs in char_pairs.values():
    for pair in pairs:
        a = pair[0]
        b = pair[1]
        create_anti_node(a[0], a[1], b[0], b[1])


print(len(anti_nodes))
print("--- %s seconds ---" % (time.time() - start_time))
