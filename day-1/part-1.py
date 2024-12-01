left = []
right = []

with open("input.txt") as file:
    for line in file:
        row = line.split()
        left.append(row[0])
        right.append(row[1])

left.sort()
right.sort()

left = [int(item) for item in left]
right = [int(item) for item in right]

total_distance = 0
for l_num, r_num in zip(left, right):
    total_distance += abs(l_num - r_num)

print(total_distance)
