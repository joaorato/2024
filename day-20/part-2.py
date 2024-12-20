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


def dijkstra(grid):
    q = [(0, start, start_dir, {start})]  # distance/cost, pos, dir, path
    visited = {start: 0}
    while len(q) > 0:
        dist, pos, dir, path = heapq.heappop(q)  # pop shortest distance/cost
        if pos in visited and visited[pos] < dist:
            continue

        if pos == end:
            return visited

        # check all available dirs
        for dirs in directions.values():
            if dirs[0] == -dir[0] and dirs[1] == -dir[1]:
                # we don't turn 180
                continue
            new_pos = (pos[0] + dirs[0], pos[1] + dirs[1])

            # discard if we've been or is wall
            if grid[new_pos[0]][new_pos[1]] == "#" or new_pos in visited:
                continue
            if new_pos not in visited or visited[new_pos] > dist + 1:
                visited[new_pos] = dist + 1
                new_path = path.copy()
                new_path.add(new_pos)
                heapq.heappush(q, (dist + 1, new_pos, dirs, new_path))
    return visited


point_dists = dijkstra(grid)

count = 0
for point in point_dists:
    for i in range(-20, 21):
        for j in range(-20, 21):
            if i == j == 0 or abs(i) + abs(j) > 20:
                continue
            new_point = (point[0] + i, point[1] + j)
            # if the new point is in the original path
            if new_point in point_dists:
                # how much it costs to go from point to new_point following the original path
                initial_cost = point_dists[point] - point_dists[new_point]

                # how much it costs to go from point to new_point in a straight line
                cheat_cost = abs(point[0] - new_point[0]) + abs(point[1] - new_point[1])
                if (initial_cost - cheat_cost) >= 100:
                    count += 1
print(count)


print("--- %s seconds ---" % (time.time() - start_time))
