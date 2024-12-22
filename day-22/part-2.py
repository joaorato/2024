import time
from collections import Counter

start_time = time.time()

numbers = []
with open("input.txt") as file:
    content = file.readlines()
    for line in content:
        numbers.append(int(line.strip()))


def get_next_num(secret):
    num = secret * 64
    num = num ^ secret
    num = num % 16777216
    num2 = int(num / 32)
    num2 = num2 ^ num
    num2 = num2 % 16777216
    num3 = num2 * 2048
    num3 = num3 ^ num2
    num3 = num3 % 16777216

    return num3


def get_next_nums(secret, n):
    price_changes = []
    seen = set()
    for _ in range(n):
        last = secret % 10  # getting the last digit
        secret = get_next_num(secret)
        price_changes.append(secret % 10 - last)  # difference in price

        # always look at the last 4 price changes
        if len(price_changes) >= 4:
            seq = tuple(price_changes[-4:])
            if seq not in seen and secret % 10 != 0:
                seen.add(seq)
                # this sequence can only be used once per buyer (first time it sees it)
                prices[seq] += secret % 10
    return


prices = Counter()
for n in numbers:
    get_next_nums(n, 2000)

print(prices.most_common()[0][1])  # 0 to get the most common, 1 to get the count

print("--- %s seconds ---" % (time.time() - start_time))
