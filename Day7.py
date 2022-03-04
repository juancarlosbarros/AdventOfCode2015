from functools import cache
with open('Day7.part2.txt') as f:
    datas = f.readlines()
f.closed
# with open('Day7.txt') as f:
#     datas = f.readlines()
# f.closed

@cache
def calc(var):
    if type(var) == int:
        return var
    elif var.isdecimal():
        return int(var)
    instr = instructions[var]
    if len(instr) == 1:
        if instr[-1].isdecimal():
            return int(instr[-1])
        else:
            return calc(instr[-1])

        return calc(instr[-1])
    match instr[-2]:
        case 'NOT':
            res = ~ calc(instr[-1])
            if res < 0:
                res += 2**16
            return res
        case 'AND':
            return calc(instr[-1]) & calc(instr[-3])
        case 'OR':
            return calc(instr[-1]) | calc(instr[-3])
        case 'RSHIFT':
            res = calc(instr[-3]) >> int(instr[-1])
            if res < 0:
                res += 2**16
            return res
        case 'LSHIFT':
            res = calc(instr[-3]) << int(instr[-1])
            if res < 0:
                res += 2**16
            return res


# part 1
datas = map(str.strip, datas)
datas = map(str.split, datas)
datas = list(datas)
instructions = {instr[-1] : instr[:-2] for instr in datas}
# print (instructions)
# for instr in instructions.keys():
#     print(instr)
#     print(calc(instr))
part1 = calc('a')
print(part1)