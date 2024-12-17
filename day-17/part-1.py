import time

start_time = time.time()

with open("input2.txt") as file:
    registerA = int(file.readline().split(":")[-1].strip())
    registerB = int(file.readline().split(":")[-1].strip())
    registerC = int(file.readline().split(":")[-1].strip())
    file.readline()  # new line
    instructions = list(map(int, file.readline().split(":")[-1].strip().split(",")))


def get_combo_operand(operand):
    if operand <= 3 and operand >= 0:
        return operand
    global registerA, registerB, registerC
    if operand == 4:
        return registerA
    if operand == 5:
        return registerB
    if operand == 6:
        return registerC
    if operand == 7:
        raise


def op0(operand):
    combo_operand = get_combo_operand(operand)
    global registerA
    registerA = int(registerA / 2**combo_operand)


def op1(literal_operand):
    global registerB
    registerB = registerB ^ literal_operand


def op2(operand):
    combo_operand = get_combo_operand(operand)
    global registerB
    registerB = combo_operand % 8


def op3():
    global registerA
    if registerA == 0:
        return False
    return True  # use it like if op3: jump


def op4():
    global registerB, registerC
    registerB = registerB ^ registerC


def op5(operand):
    combo_operand = get_combo_operand(operand)
    return combo_operand % 8  # value to output


def op6(operand):
    combo_operand = get_combo_operand(operand)
    global registerA, registerB
    registerB = int(registerA / 2**combo_operand)


def op7(operand):
    combo_operand = get_combo_operand(operand)
    global registerA, registerC
    registerC = int(registerA / 2**combo_operand)


functions = [op0, op1, op2, op3, op4, op5, op6, op7]
out = ""
i = 0
not_found = True
while not_found:
    while i < len(instructions):
        op = instructions[i]
        operand = instructions[i + 1]
        if op == 0:
            op0(operand)
        elif op == 1:
            op1(operand)
        elif op == 2:
            op2(operand)
        elif op == 3:
            if op3():
                i = operand - 2
        elif op == 4:
            op4()
        elif op == 5:
            out += str(op5(operand)) + ","
        elif op == 6:
            op6(operand)
        elif op == 7:
            op7(operand)
        i += 2
print(out[:-1])

print("--- %s seconds ---" % (time.time() - start_time))
