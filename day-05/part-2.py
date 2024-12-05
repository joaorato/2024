import time

start_time = time.time()

rules = []
orderings = []
with open("input.txt") as file:
    content = file.readlines()
    i = 0
    for line in content:
        if line == "\n":
            break
        rules.append(line.strip().split("|"))
        i += 1
    for x in range(i + 1, len(content)):
        orderings.append(content[x].strip().split(","))


def is_pair_valid(x, y):
    for rule in rules:
        if x == rule[0] and y == rule[1]:
            return True
    return False


orders_to_remove = []
for order in orderings:
    # brute force
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            if not is_pair_valid(order[i], order[j]):
                break
            else:
                continue
        else:
            continue
        break
    else:
        orders_to_remove.append(order)

invalid_orderings = [order for order in orderings if order not in orders_to_remove]

sum_invalid = 0
do_sum = False
for order in invalid_orderings:
    # brute force
    for i in range(len(order)):
        for j in range(i + 1, len(order)):
            if not is_pair_valid(order[i], order[j]):
                do_sum = True
                temp = order[i]
                order[i] = order[j]
                order[j] = temp
                j = i
                if j == len(order):
                    do_sum = False

    if do_sum:
        sum_invalid += int(order[len(order) // 2])

print("--- %s seconds ---" % (time.time() - start_time))
print(sum_invalid)
