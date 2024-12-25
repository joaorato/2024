import time
import numpy as np

start_time = time.time()

locks = []
keys = []
with open("input.txt") as file:
    for block in file.read().strip().split("\n\n"):
        rows = block.split("\n")
        block_num = np.zeros((len(rows), len(rows[0])), dtype=int)
        for i, row in enumerate(rows):
            for c, char in enumerate(row):
                if char == "#":
                    block_num[i][c] = 1

        # this only happens if the top row is #####
        if sum(block_num[0]) == len(block_num[0]):
            locks.append(block_num)
        else:
            keys.append(block_num)

fits = 0
for lock in locks:
    for key in keys:
        not_fit = np.where(lock + key >= 2)
        if len(not_fit[0]) > 0:
            continue
        fits += 1
print(fits)
print("--- %s seconds ---" % (time.time() - start_time))
