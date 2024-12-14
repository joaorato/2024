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


# now we move second by second
def move(pos, vel):
    start_x = pos[0]
    start_y = pos[1]
    vel_x = vel[0]
    vel_y = vel[1]

    pos_x_temp = start_x + vel_x
    pos_y_temp = start_y + vel_y

    new_pos_x = pos_x_temp % WIDTH
    new_pos_y = pos_y_temp % HEIGHT

    return new_pos_x, new_pos_y


def printRobots(map):
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            if (x, y) in map:
                line += str(map[(x, y)])
            else:
                line += "."
        print(line)


second = 0
while True:
    second += 1
    map = {}
    overlaps = False
    for robot in robots:
        robot[0] = move(robot[0], robot[1])
        if robot[0] in map:
            map[robot[0]] += 1
            overlaps = True
        else:
            map[robot[0]] = 1
    if not overlaps:
        printRobots(map)
        print("second: ", second)
        break

print("--- %s seconds ---" % (time.time() - start_time))
