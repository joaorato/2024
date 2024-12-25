import time

start_time = time.time()

inputs = {}
connections = {}
with open("input.txt") as file:
    content = file.readlines()
    i = 0
    for line in content:
        if line == "\n":
            break
        input = line.strip().split(":")
        inputs[input[0]] = int(input[1])
        i += 1
    for x in range(i + 1, len(content)):
        connection = content[x].split("->")
        operation = tuple(connection[0].strip().split())
        if operation in connections.keys():
            connections[operation].append(connection[1].strip())
        else:
            connections[operation] = [connection[1].strip()]


swapped = []
c0 = None
for i in range(len(inputs) // 2):
    n = str(i).zfill(2)

    # full adder
    m1, n1, r1, z1, c1 = None, None, None, None, None

    # intermediate sum
    if (f"x{n}", "XOR", f"y{n}") in connections.keys():
        m1 = connections[(f"x{n}", "XOR", f"y{n}")][0]
    elif (f"y{n}", "XOR", f"x{n}") in connections.keys():
        m1 = connections[(f"y{n}", "XOR", f"x{n}")][0]

    # intermediate carry
    if (f"x{n}", "AND", f"y{n}") in connections.keys():
        n1 = connections[(f"x{n}", "AND", f"y{n}")][0]
    elif (f"y{n}", "AND", f"x{n}") in connections.keys():
        n1 = connections[(f"y{n}", "AND", f"x{n}")][0]

    # handle carry from previous stage
    if c0:
        # previous carry with intermediate sum
        if (c0, "AND", m1) in connections.keys():
            r1 = connections[(c0, "AND", m1)][0]
        elif (m1, "AND", c0) in connections.keys():
            r1 = connections[(m1, "AND", c0)][0]
        else:
            m1, n1 = n1, m1
            swapped.extend([m1, n1])
            if (c0, "AND", m1) in connections.keys():
                r1 = connections[(c0, "AND", m1)][0]
            elif (m1, "AND", c0) in connections.keys():
                r1 = connections[(m1, "AND", c0)][0]

        # final sum
        if (c0, "XOR", m1) in connections.keys():
            z1 = connections[(c0, "XOR", m1)][0]
        elif (m1, "XOR", c0) in connections.keys():
            z1 = connections[(m1, "XOR", c0)][0]

        if m1.startswith("z"):
            m1, z1 = z1, m1
            swapped.extend([m1, z1])

        if n1.startswith("z"):
            n1, z1 = z1, n1
            swapped.extend([n1, z1])

        if r1.startswith("z"):
            r1, z1 = z1, r1
            swapped.extend([r1, z1])

        # final carry
        if (r1, "OR", n1) in connections.keys():
            c1 = connections[(r1, "OR", n1)][0]
        elif (n1, "OR", r1) in connections.keys():
            c1 = connections[(n1, "OR", r1)][0]

    # handle final carry
    if c1 and c1.startswith("z") and c1 != "z45":
        c1, z1 = z1, c1
        swapped.extend([c1, z1])

    c0 = c1 if c0 else n1

print(",".join(sorted(swapped)))


print("--- %s seconds ---" % (time.time() - start_time))
