import time

start_time = time.time()

wanted_designs = []
with open("input.txt") as file:
    available_designs = file.readline().strip().split(", ")
    file.readline()  # new line
    content = file.readlines()
    for line in content:
        wanted_designs.append(line.strip())


def get_possible_designs(wanted, available, cache={}):
    # if we reached the end of the wanted design
    if wanted == "":
        return 1
    # if we have already checked it before
    if wanted in cache:
        return cache[wanted]

    count = 0
    for av in available:
        # recursion with sub-design
        if wanted.startswith(av):
            subdesign = wanted[len(av) :]
            count += get_possible_designs(subdesign, available, cache)

    cache[wanted] = count
    return count


possible_designs = 0
for design in wanted_designs:
    possible_designs += get_possible_designs(design, available_designs)


print(possible_designs)
print("--- %s seconds ---" % (time.time() - start_time))
