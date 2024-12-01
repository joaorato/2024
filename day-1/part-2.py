left = []
right = []

with open("input.txt") as file:
    for line in file:
        row = line.split()
        left.append(int(row[0]))
        right.append(int(row[1]))

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
