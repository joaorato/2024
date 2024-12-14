import time

start_time = time.time()

robots = []
with open("input.txt") as file:
    content = file.readlines()
    for line in content:
        p, v = line.split()
        pos = p.split("=")[1].split(",")
        pos_x = int(pos[0])  # -> to the right
        pos_y = int(pos[1])  # -> downwards
        vel = v.split("=")[1].split(",")
        vel_x = int(vel[0])
        vel_y = int(vel[1])
        robots.append([(pos_x, pos_y), (vel_x, vel_y)])


WIDTH = 101
HEIGHT = 103
SECONDS = 100


def move(pos, vel):
    start_x = pos[0]
    start_y = pos[1]
    vel_x = vel[0]
    vel_y = vel[1]

    pos_x_temp = start_x + SECONDS * vel_x
    pos_y_temp = start_y + SECONDS * vel_y

    new_pos_x = pos_x_temp % WIDTH
    new_pos_y = pos_y_temp % HEIGHT

    return new_pos_x, new_pos_y


map = {}
for robot in robots:
    robot[0] = move(robot[0], robot[1])
    map[robot[0]] = map.get(robot[0], 0) + 1


# quadrants are (WIDTH - 1) / 2 wide and (HEIGHT - 1) / 2 tall
half_width = int((WIDTH - 1) / 2)
half_height = int((HEIGHT - 1) / 2)

robot_count_1 = 0
for x in range(half_width):
    for y in range(half_height):
        robot_count_1 += map.get((x, y), 0)

robot_count_2 = 0
for x in range(half_width):
    for y in range(half_height + 1, HEIGHT):
        robot_count_2 += map.get((x, y), 0)

robot_count_3 = 0
for x in range(half_width + 1, WIDTH):
    for y in range(half_height):
        robot_count_3 += map.get((x, y), 0)

robot_count_4 = 0
for x in range(half_width + 1, WIDTH):
    for y in range(half_height + 1, HEIGHT):
        robot_count_4 += map.get((x, y), 0)


print(robot_count_1 * robot_count_2 * robot_count_3 * robot_count_4)
print("--- %s seconds ---" % (time.time() - start_time))
