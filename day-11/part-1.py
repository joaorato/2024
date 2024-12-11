import time

start_time = time.time()

with open("input.txt") as file:
    stones = file.readline().split()


def split_stone_at(index, old_stone):
    firstpart, secondpart = (
        old_stone[: len(old_stone) // 2],
        str(int(old_stone[len(old_stone) // 2 :])),  # removing trailing 0s
    )

    stones[index] = firstpart
    stones.insert(index + 1, secondpart)


for i in range(25):
    enum_stones = stones
    bypass = -1  # we need to not iterate on the new splitted index
    for idx, stone in enumerate(enum_stones):
        if idx == bypass:
            continue
        if stone == "0":
            stones[idx] = "1"
        elif len(stone) % 2 == 0:
            split_stone_at(idx, stone)
            bypass = idx + 1
        else:
            stones[idx] = str(int(stone) * 2024)

print(len(stones))
print("--- %s seconds ---" % (time.time() - start_time))
