import numpy as np
import time

start_time = time.time()

levels = []

with open("input.txt") as file:
    for line in file:
        row = np.array(line.split(), dtype=int)
        levels.append(row)


def is_sorted_up(a):
    return np.all(a[:-1] <= a[1:])


def is_sorted_down(a):
    return np.all(a[:-1] >= a[1:])


def calculate_distances(a):
    return np.absolute(a[1:] - a[:-1])


safe = 0
for row in levels:
    if is_sorted_up(row):
        dists = calculate_distances(row)
        if not np.any((dists == 0) | (dists > 3)):
            safe += 1
    elif is_sorted_down(row):
        dists = calculate_distances(row)
        if not np.any((dists == 0) | (dists > 3)):
            safe += 1
    else:
        continue

print("--- %s seconds ---" % (time.time() - start_time))
print(safe)
