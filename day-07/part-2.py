import time
from itertools import product

start_time = time.time()

tests = []
with open("input.txt") as file:
    content = file.readlines()
    for line in content:
        split = line.split(":")
        numbers = split[1].strip().split()
        tests.append((int(split[0]), list(map(int, numbers))))


def do_operation(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "*":
        return num1 * num2
    elif operator == "||":
        return int(f"{num1}{num2}")


possible_results = 0
operators = ["+", "*", "||"]

for case in tests:
    result = case[0]
    numbers = case[1]

    # get all possible sequences of operators with the length of the test case - 1
    operator_sequences = product(operators, repeat=len(numbers) - 1)

    for sequence in operator_sequences:
        res = numbers[0]
        for i in range(len(sequence)):
            res = do_operation(res, sequence[i], numbers[i + 1])
        if res == result:
            possible_results += res
            break

print(possible_results)
print("--- %s seconds ---" % (time.time() - start_time))
