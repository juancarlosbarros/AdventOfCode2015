with open('Day8.txt') as f:
    datas = f.read()
f.closed
string = datas

# part 1
def part1():
    # print(datas)
    # print(string)
    print("len datas:", len(datas), "len repr(datas):", len(repr(datas)))
    pos = 0
    diff = 0
    longueur = 0
    sp_car = ""
    while pos < len(string):
        s=string[pos]
        match string[pos]:
            case '\\':
                match string[pos+1]:
                    case '\\':
                        diff += 1
                        longueur += 1
                        pos += 2
                    case '"':
                        diff += 1
                        longueur += 1
                        pos += 2
                    case 'x':
                        sp_car += chr(int(string[pos+2:pos+4], 16))
                        diff += 3
                        longueur += 1
                        pos += 4
            case '\n':
                pos += 1
            case '"':
                diff += 1
                pos += 1
            case '\'':
                pos += 1
            case _:
                pos += 1
                longueur += 1
    print('Caratères spéciaux:', sp_car)
    print("longuer : ", longueur, "différence : ", diff)


# part2
def part2():
    lines = datas.split('\n')
    # print(datas)
    # print(repr(datas))
    diff = 0
    for line in lines:
        diff += 4
        pos = 1
        while pos < len(line)-1:
            s=line[pos]
            if s == '\\' or s == '"':
                diff += 1
            pos += 1
    print("différence : ", diff)



# part1()
part2()

