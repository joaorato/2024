import time

start_time = time.time()

wanted_designs = []
with open("input.txt") as file:
    available_designs = file.readline().strip().split(", ")
    file.readline()  # new line
    content = file.readlines()
    for line in content:
        wanted_designs.append(line.strip())


def is_design_possible(wanted, available, cache={}):
    # if we reached the end of the wanted design
    if wanted == "":
        return True
    # if we have already checked it before
    if wanted in cache:
        return cache[wanted]

    count = 0
    for av in available:
        # recursion with sub-design
        if wanted.startswith(av):
            subdesign = wanted[len(av) :]
            count += is_design_possible(subdesign, available, cache)

    cache[wanted] = count > 0
    return count > 0


possible_designs = 0
for design in wanted_designs:
    possible_designs += is_design_possible(design, available_designs)


print(possible_designs)
print("--- %s seconds ---" % (time.time() - start_time))
