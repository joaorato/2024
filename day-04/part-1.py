import time

start_time = time.time()

lines = []
with open("input.txt") as file:
    content = file.readlines()
    for line in content:
        lines.append(line.strip())

word = "XMAS"

directions = [
    (0, 1),  # right
    (0, -1),  # left
    (1, 0),  # down
    (-1, 0),  # up
    (1, 1),  # diagonal down-right
    (1, -1),  # diagonal down-left
    (-1, 1),  # diagonal up-right
    (-1, -1),  # diagonal up-left
]


def search_in_direction(start_i, start_j, di, dj):
    i, j = start_i, start_j
    for char in word:
        if (
            i >= len(lines)
            or i < 0
            or j >= len(lines[0])
            or j < 0
            or char != lines[i][j]
        ):
            return False
        i += di
        j += dj
    return True


count = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        for di, dj in directions:
            if search_in_direction(i, j, di, dj):
                count += 1

print("--- %s seconds ---" % (time.time() - start_time))
print(count)
