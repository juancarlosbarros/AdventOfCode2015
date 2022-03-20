numbers = list(map(int, list("1321131112")))

# part 1
def transform(start):
    length = len(start)
    pos = 0
    res = []
    while pos < length:
        n = 1
        while pos + n < length and start[pos+n] == start[pos]:
            n += 1
        res += [n, start[pos]]
        pos += n
    return res


def part1():
    numbers = list(map(int, list("1321131112")))
    for _ in range(50):
        numbers = transform(numbers)
        # print(numbers)
    print("Part 1:", len(numbers))


part1()
