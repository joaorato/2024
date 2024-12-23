import time

start_time = time.time()

connections = []
with open("input.txt") as file:
    content = file.readlines()
    for line in content:
        pcs = line.strip().split("-")
        connections.append((pcs[0], pcs[1]))


connections_dict = {}
for a, b in connections:
    if a not in connections_dict:
        connections_dict[a] = set()
    if b not in connections_dict:
        connections_dict[b] = set()
    connections_dict[a].add(b)
    connections_dict[b].add(a)

triplets = set()
for a in connections_dict:
    for b in connections_dict[a]:
        if b > a:  # to avoid duplicate triplets like (a,b,c) and (b,a,c)
            for c in connections_dict[a]:
                if (
                    c > b and c in connections_dict[b]
                ):  # ensure all three are interconnected
                    triplets.add(tuple(sorted([a, b, c])))

triplets_with_t = []
for triplet in triplets:
    for computer in triplet:
        if computer.startswith("t"):
            triplets_with_t.append(triplet)
            break


print(len(triplets_with_t))
print("--- %s seconds ---" % (time.time() - start_time))
