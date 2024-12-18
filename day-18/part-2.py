import time
import heapq

start_time = time.time()

bytes = []
with open("input.txt") as file:
    content = file.readlines()
    i = 0
    for line in content:
        coords = line.strip().split(",")
        bytes.append((int(coords[0]), int(coords[1])))
        i += 1

GRID_SIZE = 71
grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
start_dir = directions[">"]


def is_valid(pos, bad_bytes):
    return (
        0 <= pos[0] < GRID_SIZE and 0 <= pos[1] < GRID_SIZE
    ) and pos not in bad_bytes


def dijkstra(bad_bytes):
    start = (0, 0)
    end = (GRID_SIZE - 1, GRID_SIZE - 1)
    q = [(0, start, start_dir, {start})]  # distance/cost, pos, dir, path
    visited = set()
    while len(q) > 0:
        dist, pos, dir, path = heapq.heappop(q)  # pop shortest distance/cost
        if pos in visited:
            continue
        visited.add(pos)

        if pos == end:
            return dist

        # check all available dirs
        for dirs in directions.values():
            if dirs[0] == -dir[0] and dirs[1] == -dir[1]:
                # we don't turn 180
                continue
            new_pos = (pos[0] + dirs[0], pos[1] + dirs[1])
            cost = 1

            # discard if we've been or is # or is out of bounds
            if not is_valid(new_pos, bad_bytes) or new_pos in visited:
                continue

            new_path = path.copy()
            new_path.add(new_pos)
            heapq.heappush(q, (dist + cost, new_pos, dirs, new_path))
    return None


bad_bytes = set()
for i in range(len(bytes)):
    bad_bytes.add(bytes[i])
    # we have already done up to 1024 and the puzzle was valid,
    # so skip for performance
    if i < 1024:
        continue
    last_cost = dijkstra(bad_bytes)
    if last_cost is None:
        print(f"{bytes[i][0]},{bytes[i][1]}")
        break

print("--- %s seconds ---" % (time.time() - start_time))
