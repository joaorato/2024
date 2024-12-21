import time
from itertools import permutations
from functools import cache

start_time = time.time()

codes = []
with open("input.txt") as file:
    content = file.readlines()
    for line in content:
        codes.append(line.strip())

# 7 8 9
# 4 5 6
# 1 2 3
# _ 0 A
num_pad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "_": (3, 0),
    "0": (3, 1),
    "A": (3, 2),
}

# _ ^ A
# < v >
dir_pad = {"_": (0, 0), "^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


@cache
def find_valid_seqs(start, pos, empty):
    travel = (pos[0] - start[0], pos[1] - start[1])

    seq_i = ""
    if travel[0] > 0:
        for i in range(travel[0]):
            seq_i += "v"
    else:
        for i in range(abs(travel[0])):
            seq_i += "^"

    seq_j = ""
    if travel[1] > 0:
        for i in range(travel[1]):
            seq_j += ">"
    else:
        for i in range(abs(travel[1])):
            seq_j += "<"

    s = set(permutations(seq_i + seq_j))
    remove = set()

    for moves in s:
        p = start
        for m in moves:
            p = (p[0] + directions[m][0], p[1] + directions[m][1])
            # if a move goes to the empty space, we will discard this whole sequence
            if p == empty:
                remove.add(moves)
                break

    valid_seqs = s - remove

    return {f"{''.join(valid_seq)}A" for valid_seq in valid_seqs}


@cache
def find_length_of_sequence(code, level):
    if level == 25:
        pad = num_pad
    else:
        pad = dir_pad
    start_pos = pad["A"]
    length = 0
    for char in code:
        pos = pad[char]

        seqs = find_valid_seqs(start_pos, pos, pad["_"])
        if level > 0:
            length += min(find_length_of_sequence(seq, level - 1) for seq in seqs)
        else:
            # in the last level the moves are all equal in length
            length += len(list(seqs)[0])

        start_pos = pos

    return length


sum = 0
for code in codes:
    numeric_part = int(code[:3])
    length = find_length_of_sequence(code, 25)
    print("CODE: ", code)
    print("LEN: ", length)
    sum += length * numeric_part
print(sum)

print("--- %s seconds ---" % (time.time() - start_time))
