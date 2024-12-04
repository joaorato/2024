lines = []
with open("input.txt") as file:
    content = file.readlines()
    for line in content:
        lines.append(line.strip())

word = "MAS"

directions = [
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
                # we need to now find a crossing diagonal, meaning either we multiply by -1 the i or the j
                # first the i
                cross_i = i + di * (len(word) - 1)
                di2 = -1 * di
                if search_in_direction(cross_i, j, di2, dj):
                    count += 1
                    continue

                # now the j
                cross_j = j + dj * (len(word) - 1)
                dj2 = -1 * dj
                if search_in_direction(i, cross_j, di, dj2):
                    count += 1

print(count / 2)  # man I was missing this 2 for so long
