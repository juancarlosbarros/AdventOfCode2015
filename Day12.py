f = open("Day12.txt")
data = f.readline()
print(len(data), "caractères lus.")


# part1

def nombre(texte, pos):
    res = int(texte[0])
    delta = 1
    while texte[delta].isnumeric():
        res *= 10
        res += int(texte[delta])
        delta += 1
    if pos<0:
        res *= -1
        pos *= -1
    return res, pos + delta


def part1(texte):
    length = len(texte)
    nombres = []
    pos = 0
    while pos < length-1:
        if texte[pos] == '-':
            pos += 1
            if texte[pos].isnumeric():
                next, pos = nombre(texte[pos:], -pos)
                nombres.append(next)
        elif texte[pos].isnumeric():
            next, pos = nombre(texte[pos:], pos)
            nombres.append(next)
        else:
            pos += 1
    print(sum(nombres))
    print(nombres)

def purge(texte):
    if ':"red"' not in texte:
        return texte
    else:
        pos = texte.find(':"red"')
        # end = texte.find("}", pos)
        start = pos-1
        level = 1
        while start >= 0:
            if texte[start] == "{":
                level -= 1
            elif texte[start] == "}":
                level += 1
            if level == 0:
                break
            start -= 1
        end = pos + 6
        level = 1
        while end < len(texte)-1:
            if texte[end] == "{":
                level += 1
            elif texte[end] == "}":
                level -= 1
            if level == 0:
                break
            end += 1
        res = texte[:start] + '0' + texte[end+1:]
        return purge(res)


def part2():
    purged_text = purge(data)
    print(data)
    print(purged_text)
    part1(purged_text)



part1(data)
part2()
