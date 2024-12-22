import time

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
    for _ in range(n):
        secret = get_next_num(secret)
    return secret


sum = 0
for n in numbers:
    sum += get_next_nums(n, 2000)

print(sum)

print("--- %s seconds ---" % (time.time() - start_time))
