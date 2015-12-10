import re

instructions = open("input", 'r').readlines()

# create a 1 million light array of 1000 x 1000
lights = [[0 for i in range(0, 1000)] for i in range(0, 1000)]
lightson = 0

def parse_inst(instruction):
    numbers = re.findall(r'\d+', instruction)
    return (int(numbers[0]), int(numbers[1])), (int(numbers[2]), int(numbers[3]))

def toggle(range_total):
    range_begin, range_end = range_total
    for i in range(range_begin[0], range_end[0]+1):
        for p in range(range_begin[1], range_end[1]+1):
            if lights[i][p] == 1:
                lights[i][p] = 0
            else:
                lights[i][p] = 1

def turnon(range_total):
    range_begin, range_end = range_total
    for i in range(range_begin[0], range_end[0]+1):
        for p in range(range_begin[1], range_end[1]+1):
            lights[i][p] = 1

def turnoff(range_total):
    range_begin, range_end = range_total
    for i in range(range_begin[0], range_end[0]+1):
        for p in range(range_begin[1], range_end[1]+1):
            lights[i][p] = 0

for instruction in instructions:
    if instruction.startswith("toggle"):
        toggle(parse_inst(instruction))
    if instruction.startswith("turn off"):
        turnoff(parse_inst(instruction))
    if instruction.startswith("turn on"):
        turnon(parse_inst(instruction))

for i in lights:
    for p in i:
        if p == 1:
            lightson += 1

print("{} light on".format(lightson))