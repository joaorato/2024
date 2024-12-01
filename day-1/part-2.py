left = []
right = []

with open("input.txt") as file:
    for line in file:
        row = line.split()
        left.append(row[0])
        right.append(row[1])

left = [int(item) for item in left]
right = [int(item) for item in right]

left.sort()
right.sort()

sim_score = 0
for l_num in left:
    number_score = 0
    for r_num in right:
        if l_num == r_num:
            number_score += 1
    sim_score += l_num * number_score

print(sim_score)
