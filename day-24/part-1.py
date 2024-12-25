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

known = set(inputs)
unknown = set()


def find_value(connections, known, inputs):
    for operation, output in connections.items():
        if operation[0] in known and operation[2] in known:
            for o in output:
                known.add(o)
                if operation[1] == "AND":
                    inputs[o] = inputs[operation[0]] & inputs[operation[2]]
                elif operation[1] == "OR":
                    inputs[o] = inputs[operation[0]] | inputs[operation[2]]
                elif operation[1] == "XOR":
                    inputs[o] = inputs[operation[0]] ^ inputs[operation[2]]
                if o in unknown:
                    unknown.remove(o)
        else:
            for o in output:
                unknown.add(o)

    if len(unknown) > 0:
        find_value(connections, known, inputs)


find_value(connections, known, inputs)

z = ""
digit = 0

for key, value in sorted(inputs.items()):
    if (
        key.startswith("z")
        and key.split("z")[1].isdigit()
        and int(key.split("z")[1]) == digit
    ):
        z = str(value) + z
        digit += 1

print(z)
print(int(z, 2))

print("--- %s seconds ---" % (time.time() - start_time))
