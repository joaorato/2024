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
    return {(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)}


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


def perimeter(region):
    perim = 0
    for choords in region:
        for neighbour in neighbours(choords):
            perim += (
                neighbour not in region
            )  # if the neighbour is not in region sum 1 (it's the edge of the region)
    return perim


print(sum(len(region) * perimeter(region) for region in regions))


print("--- %s seconds ---" % (time.time() - start_time))
