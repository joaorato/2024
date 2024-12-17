import time

start_time = time.time()

with open("input.txt") as file:
    registerA = int(file.readline().split(":")[-1].strip())
    registerB = int(file.readline().split(":")[-1].strip())
    registerC = int(file.readline().split(":")[-1].strip())
    file.readline()  # new line
    instructions = list(map(int, file.readline().split(":")[-1].strip().split(",")))


def get_combo_operand(operand, regA):
    if operand <= 3 and operand >= 0:
        return operand
    global registerB, registerC
    if operand == 4:
        return regA
    if operand == 5:
        return registerB
    if operand == 6:
        return registerC
    if operand == 7:
        raise


def op0(operand, regA):
    combo_operand = get_combo_operand(operand, regA)
    return int(regA / 2**combo_operand)


def op1(literal_operand):
    global registerB
    registerB = registerB ^ literal_operand


def op2(operand, regA):
    combo_operand = get_combo_operand(operand, regA)
    global registerB
    registerB = combo_operand % 8


def op3(regA):
    if regA == 0:
        return False
    return True  # use it like if op3: jump


def op4():
    global registerB, registerC
    registerB = registerB ^ registerC


def op5(operand, regA):
    combo_operand = get_combo_operand(operand, regA)
    return combo_operand % 8  # value to output


def op6(operand, regA):
    combo_operand = get_combo_operand(operand, regA)
    global registerB
    registerB = int(regA / 2**combo_operand)


def op7(operand, regA):
    combo_operand = get_combo_operand(operand, regA)
    global registerC
    registerC = int(regA / 2**combo_operand)


functions = [op0, op1, op2, op3, op4, op5, op6, op7]


def run_program(instructions, regA):
    global registerB, registerC
    registerB = 0
    registerC = 0
    out = []
    i = 0
    while i < len(instructions):
        op = instructions[i]
        operand = instructions[i + 1]
        if op == 0:
            regA = op0(operand, regA)
        elif op == 1:
            op1(operand)
        elif op == 2:
            op2(operand, regA)
        elif op == 3:
            if op3(regA):
                i = operand - 2
        elif op == 4:
            op4()
        elif op == 5:
            out.append(op5(operand, regA))
        elif op == 6:
            op6(operand, regA)
        elif op == 7:
            op7(operand, regA)
        i += 2
        # we can stop in the first output now
        if len(out) > 0:
            return out
    return out


instructions_reversed = instructions[::-1]


def find_regA(regA=0, depth=0):
    if depth == len(instructions_reversed):
        return regA
    # 8 because regA is only getting divided by 8 in each run
    # when we find a valid value, we skip over by times 8 and continue
    for i in range(8):
        output = run_program(instructions, regA * 8 + i)
        if output and output[0] == instructions_reversed[depth]:
            print(output, regA * 8 + i)
            if result := find_regA((regA * 8 + i), depth + 1):
                return result


print(find_regA())

print("--- %s seconds ---" % (time.time() - start_time))
