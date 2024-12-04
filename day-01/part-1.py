left = []
right = []

with open("input.txt") as file:
    for line in file:
        row = line.split()
        left.append(int(row[0]))
        right.append(int(row[1]))

left.sort()
right.sort()

total_distance = 0
for l_num, r_num in zip(left, right):
    total_distance += abs(l_num - r_num)

print(total_distance)
