import time

start_time = time.time()

with open("input.txt") as file:
    map = file.readline().strip()


new_map = []
for i in range(len(map)):
    if i % 2 == 0:
        for j in range(int(map[i])):
            new_map.append(int(i) // 2)
    else:
        for j in range(int(map[i])):
            new_map.append(".")


def find_leftmost_dot(i):
    for j in range(i):
        if new_map[j] == ".":
            return j, False
    return 0, True


we_stopped_at = -100000000
# until we have no dots before numbers
for i in range(len(new_map) - 1, -1, -1):
    if new_map[i] != ".":
        j, stop = find_leftmost_dot(i)
        if stop:
            we_stopped_at = i
            break
        new_map[j] = new_map[i]
        new_map[i] = "."

checksum = 0

for i in range(we_stopped_at + 1):
    if new_map[i] != ".":
        checksum += i * new_map[i]
print(checksum)

print("--- %s seconds ---" % (time.time() - start_time))
