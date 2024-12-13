import time
import numpy as np

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
        return prize_x, prize_y

    button = machine[i].split("+")
    x = int(button[1].split(",")[0])
    y = int(button[2])

    return x, y


def solve_system(system):
    A, B = system
    try:
        solution = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        # handle when it cannot be solved
        solution = None
    return solution


cost = 0
for machine in machines:
    # button A
    x_A, y_A = parse_coords(machine, 0)

    # button B
    x_B, y_B = parse_coords(machine, 1)

    # prize
    x_P, y_P = parse_coords(machine, 2)

    system = np.array([[x_A, x_B], [y_A, y_B]]), np.array([x_P, y_P])

    solution = solve_system(system)

    if solution is not None:
        # ugly stuff, but it worked
        presses_A = round(solution[0], 10)
        presses_B = round(solution[1], 10)
    else:
        # print("System has no unique integer solution.")
        continue
    if (
        presses_A.is_integer()
        and presses_A <= 100
        and presses_B.is_integer()
        and presses_B <= 100
    ):
        # print(f"Solution for system: A = {presses_A}, B = {presses_B}")
        cost += presses_A * price_A + presses_B * price_B
        # print(f"Cost so far: {cost}")
    else:
        # print(
        #     f"why: {presses_A.is_integer()}, {presses_B.is_integer()}, {presses_B}"
        # )
        # print("System has no unique integer solution.")
        continue

print("Cost: ", cost)
print("--- %s seconds ---" % (time.time() - start_time))
