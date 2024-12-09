import time

start_time = time.time()

with open("input.txt") as file:
    map = file.readline().strip()


new_map = []
file_blocks = []
for i in range(len(map)):
    if i % 2 == 0:
        start = len(new_map)
        for j in range(int(map[i])):
            new_map.append(int(i) // 2)
        file_blocks.append((i // 2, start, len(new_map) - 1))
    else:
        for j in range(int(map[i])):
            new_map.append(".")


def find_leftmost_free_segment(start, length):
    free_segment_start = None
    current_free_length = 0
    # don't find free segments to the right!
    for i in range(start):
        if new_map[i] == ".":
            if current_free_length == 0:
                free_segment_start = i
            current_free_length += 1
            if current_free_length == length:
                return free_segment_start
        else:
            current_free_length = 0
    return None


# start from the last block
for block in reversed(file_blocks):
    value, start, end = block
    length = end - start + 1
    free_segment_start = find_leftmost_free_segment(start, length)
    if free_segment_start is not None:
        # move the entire block to the leftmost free space
        for i in range(length):
            new_map[free_segment_start + i] = value
            new_map[start + i] = "."

checksum = 0

for i in range(len(new_map)):
    if new_map[i] != ".":
        checksum += i * new_map[i]
print(checksum)

print("--- %s seconds ---" % (time.time() - start_time))
