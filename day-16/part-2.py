import time
import heapq

start_time = time.time()

with open("input.txt") as file:
    content = file.readlines()
    grid = [[char for char in line.strip()] for line in content]

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
start_dir = directions[">"]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "E":
            end = (i, j)


def find_all():
    q = [(0, start, start_dir, {start})]  # distance/cost, pos, dir, path
    visited = {}
    tiles = {}
    best_cost = float("inf")
    while len(q) > 0:
        dist, pos, dir, path = heapq.heappop(q)  # pop shortest distance/cost

        # now we need to keep track of dir and dist so we can continue paths, if they are not bad
        if (pos, dir) in visited:
            if visited[(pos, dir)] < dist:
                continue
        visited[(pos, dir)] = dist

        # now if we reach the end we add the tiles to that cost value
        if pos == end:
            best_cost = dist
            if best_cost not in tiles:
                tiles[best_cost] = set()
            tiles[best_cost].update(path)

        # check all available dirs
        for dirs in directions.values():
            if dirs[0] == -dir[0] and dirs[1] == -dir[1]:
                # we don't turn 180
                continue
            new_pos = (pos[0] + dirs[0], pos[1] + dirs[1])
            is_straight = abs(dirs[0]) == abs(dir[0]) and abs(dirs[1]) == abs(dir[1])
            cost = 1
            if not is_straight:
                cost += 1000

            # discard if we've been or is wall
            if grid[new_pos[0]][new_pos[1]] == "#" or new_pos in visited:
                continue

            new_path = path.copy()
            new_path.add(new_pos)
            heapq.heappush(q, (dist + cost, new_pos, dirs, new_path))

    return tiles


paths = find_all()
lowest = float("inf")
for cost, path in paths.items():
    if cost < lowest:
        lowest = cost
print(len(paths[lowest]))

print("--- %s seconds ---" % (time.time() - start_time))
