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


def is_bad_level(a):
    return np.any((a == 0) | (a > 3))


safe = 0

for row in levels:
    if is_sorted_up(row):
        dists = calculate_distances(row)
        if not is_bad_level(dists):
            safe += 1
            continue
        else:
            for i in range(len(row)):
                modified_row = np.concatenate([row[:i], row[i + 1 :]])
                modified_dists = calculate_distances(modified_row)
                if not is_bad_level(modified_dists):
                    safe += 1
                    break
    elif is_sorted_down(row):
        dists = calculate_distances(row)
        if not is_bad_level(dists):
            safe += 1
            continue
        else:
            for i in range(len(row)):
                modified_row = np.concatenate([row[:i], row[i + 1 :]])
                modified_dists = calculate_distances(modified_row)
                if not is_bad_level(modified_dists):
                    safe += 1
                    break
    else:
        for i in range(len(row)):
            modified_row = np.concatenate([row[:i], row[i + 1 :]])

            if is_sorted_up(modified_row) or is_sorted_down(modified_row):
                dists = calculate_distances(modified_row)

                if not is_bad_level(dists):
                    safe += 1
                    break

print("--- %s seconds ---" % (time.time() - start_time))
print(safe)
