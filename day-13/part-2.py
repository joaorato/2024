import time

start_time = time.time()

machines = []
with open("input.txt") as file:
    content = file.readlines()
    for i in range(0, len(content), 4):
        machine = []
        machine.append(content[i].strip())
        machine.append(content[i + 1].strip())
        machine.append(content[i + 2].strip())
        machines.append(machine)

price_A = 3
price_B = 1


def parse_coords(machine, i):
    if i == 2:
        prize = machine[i].split("=")
        prize_x = int(prize[1].split(",")[0])
        prize_y = int(prize[2])
        return prize_x + 10000000000000, prize_y + 10000000000000

    button = machine[i].split("+")
    x = int(button[1].split(",")[0])
    y = int(button[2])

    return x, y


cost = 0
for machine in machines:
    # button A
    x_A, y_A = parse_coords(machine, 0)

    # button B
    x_B, y_B = parse_coords(machine, 1)

    # prize
    x_P, y_P = parse_coords(machine, 2)

    # Scratch numpy solver, was impossible to make it work with integers I'm not sure why
    # This ends up being simple after using pen and paper
    presses_A = (y_P * x_B - x_P * y_B) / (y_A * x_B - x_A * y_B)
    presses_B = (x_P - presses_A * x_A) / x_B

    # Check if a and b are integers
    if presses_A.is_integer() and presses_B.is_integer():
        cost += presses_A * price_A + presses_B * price_B


print("Cost: ", cost)
print("--- %s seconds ---" % (time.time() - start_time))
