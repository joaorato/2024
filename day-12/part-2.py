import time

start_time = time.time()


map = {}
with open("input.txt") as file:
    for i, row in enumerate(file.readlines()):
        for j, char in enumerate(row.strip()):
            map[(i, j)] = char


# regions are only defined by neighbours at north, south, east, west
def neighbours(choords):
    i, j = choords
    return [
        (i + 1, j),
        (i, j + 1),
        (i - 1, j),
        (i, j - 1),
    ]  # I had to make this a list for this part


visited = set()
regions = []

for choords, char in map.items():
    if choords in visited:
        continue
    region = set()

    to_explore = [choords]
    while to_explore:
        # add coordinate pair to region and set its neighbours
        # to be explored if they have the same char
        c = to_explore.pop()
        region.add(c)
        for neighbour in neighbours(c):
            if neighbour in region:
                continue
            if map.get(neighbour) == char:
                to_explore.append(neighbour)

    regions.append(region)

    visited.update(region)


def num_of_sides(region):
    corners = 0
    for choords in region:
        n = neighbours(choords)
        if n[0] not in region and n[1] not in region:  # bottom-right corner
            corners += 1
        if n[1] not in region and n[2] not in region:  # right-up corner
            corners += 1
        if n[2] not in region and n[3] not in region:  # up-left corner
            corners += 1
        if n[3] not in region and n[0] not in region:  # left-bottom corner
            corners += 1

        # what if the corners are "inverted"? we need to check diagonals, neighbours are not enough
        i, j = choords
        # up-left not in region but up and left are
        if (i - 1, j - 1) not in region and n[2] in region and n[3] in region:
            corners += 1
        # up-right not in region but up and right are
        if (i - 1, j + 1) not in region and n[2] in region and n[1] in region:
            corners += 1
        # bottom-right not in region but right and bottom are
        if (i + 1, j + 1) not in region and n[1] in region and n[0] in region:
            corners += 1
        # bottom-left not in region but bottom and left are
        if (i + 1, j - 1) not in region and n[0] in region and n[3] in region:
            corners += 1

    return corners


print(sum(len(region) * num_of_sides(region) for region in regions))


print("--- %s seconds ---" % (time.time() - start_time))
