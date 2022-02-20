with open('Day6.txt') as f:
    datas = f.readlines()
f.closed


def set_on1(corner1, corner2):
    global lights1
    x1, y1 = map(int, corner1.split(','))
    x2, y2 = map(int, corner2.split(','))
    #print ('on', x1, y1, x2, y2)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights1[i][j] = 1

def set_off1(corner1, corner2):
    global lights1
    x1, y1 = map(int, corner1.split(','))
    x2, y2 = map(int, corner2.split(','))
    #print ('on', x1, y1, x2, y2)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights1[i][j] = 0

def set_toggle1(corner1, corner2):
    global lights1
    x1, y1 = map(int, corner1.split(','))
    x2, y2 = map(int, corner2.split(','))
    #print ('on', x1, y1, x2, y2)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights1[i][j] = 1 - lights1[i][j]


# part 1
lights1 = [[0 for _ in range(1000)] for _ in range (1000)]
datas = map(str.strip, datas)
datas = map(str.split, datas)
datas = map(lambda instructions: instructions[-4:], datas)
datas = map(lambda instructions: [instructions[0], instructions[1], instructions[3]], datas)
datas = list (datas)
# print (lights1)
for instr in datas:
    match instr[0]:
        case 'on':
            set_on1(instr[1], instr[2])
        case 'off':
            set_off1(instr[1], instr[2])
        case 'toggle':
            set_toggle1(instr[1], instr[2])
part1 = sum(light for line in lights1 for light in line)
print('Part1: ', part1)


def set_on2(corner1, corner2):
    global lights2
    x1, y1 = map(int, corner1.split(','))
    x2, y2 = map(int, corner2.split(','))
    #print ('on', x1, y1, x2, y2)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights2[i][j] += 1

def set_off2(corner1, corner2):
    global lights2
    x1, y1 = map(int, corner1.split(','))
    x2, y2 = map(int, corner2.split(','))
    #print ('on', x1, y1, x2, y2)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if lights2[i][j] > 0:
                lights2[i][j] -= 1

def set_toggle2(corner1, corner2):
    global lights2
    x1, y1 = map(int, corner1.split(','))
    x2, y2 = map(int, corner2.split(','))
    #print ('on', x1, y1, x2, y2)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            lights2[i][j] += 2


# part 2
lights2 = [[0 for _ in range(1000)] for _ in range (1000)]
for instr in datas:
    match instr[0]:
        case 'on':
            set_on2(instr[1], instr[2])
        case 'off':
            set_off2(instr[1], instr[2])
        case 'toggle':
            set_toggle2(instr[1], instr[2])
part2 = sum(light for line in lights2 for light in line)
print('Part2: ', part2)

