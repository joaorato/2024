import time
from functools import cache

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


@cache
def find_largest_network(nodes=frozenset()):  # frozenset is hashable
    best = nodes
    for start in connections_dict:
        # set difference -> if there is any node in the network that is not connected to start
        if nodes - connections_dict[start]:
            continue
        # set union and recursion
        new = find_largest_network(nodes | {start})
        if len(new) > len(best):
            best = new
    return best


largest_network = sorted(find_largest_network())
print(",".join(largest_network))


print("--- %s seconds ---" % (time.time() - start_time))
