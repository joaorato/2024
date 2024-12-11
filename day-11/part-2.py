from collections import defaultdict
import time

start_time = time.time()


with open("input.txt") as file:
    input_stones = list(map(int, file.readline().split()))


stones = defaultdict(int)  # keep track of present stones

# sets are enough since the same processing will happen for all equal numbers
evens = set()
odds = set()

# split stones into even (will be split) and odd (will be multiplied)
for x in input_stones:
    stones[x] = 1
    if x == 0:
        continue
    if len(str(x)) % 2 == 0:
        evens.add(x)
    else:
        odds.add(x)

for _ in range(75):
    new_stones = defaultdict(int)
    new_evens = set()
    new_odds = set()

    # all 0s will become 1s
    if stones[0] > 0:
        new_stones[1] = stones[0]
        new_odds.add(1)

    for x in evens:
        x_str = str(x)
        mid = len(x_str) // 2
        first = int(x_str[:mid])
        second = int(x_str[mid:])

        new_stones[first] += stones[x]
        new_stones[second] += stones[x]

        # for any new numbers always check where they fall into for future blinks
        if len(str(first)) % 2 == 0:
            new_evens.add(first)
        elif first != 0:
            new_odds.add(first)

        if len(str(second)) % 2 == 0:
            new_evens.add(second)
        elif second != 0:
            new_odds.add(second)

    for x in odds:
        multiplied = x * 2024
        new_stones[multiplied] += stones[x]
        if len(str(multiplied)) % 2 == 0:
            new_evens.add(multiplied)
        else:
            new_odds.add(multiplied)

    evens = new_evens
    odds = new_odds
    stones = new_stones

# sum the occurrences of each number in the dict
stone_count = sum(stones.values())
print(stone_count)
print("--- %s seconds ---" % (time.time() - start_time))
