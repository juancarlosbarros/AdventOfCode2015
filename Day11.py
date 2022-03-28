start = "hxbxxyzz"

# part 1
def encode(word):
    res = []
    for char in word:
        res.append(ord(char))
    return res


def alpha(word):
    res = ""
    for char in word:
        res += chr(char)
    return res


def two_doubles(word):
    length = len(word)
    pos = 0
    while word[pos] != word[pos+1]:
        pos += 1
        if pos > length-4:
            return False
    pos += 2
    while word[pos] != word[pos+1]:
        pos += 1
        if pos > length-2:
            return False
    # print(alpha(word), " doubles True!!!")
    return True


def three_rise(word):
    length = len(word)
    pos = 0
    while pos < length - 2:
        if word[pos] + 1 == word[pos+1] and word[pos+1] + 1 == word[pos+2]:
                # print(alpha(word), " rise True!!!")
                return True
        else:
            pos += 1
    return False



def correct(word):
    if two_doubles(word) and three_rise(word):
        return True
    return False


def transform(word):
    length = len(word)
    for pos in range(length-1, -1, -1):
        char = word[pos]
        if char == 122:
            word[pos] = 97
            continue
        elif char in [104, 107, 110]:
            char += 1
            word[pos] = char
        char += 1
        word[pos] = char
        return word


def part1():
    word = encode(start)
    word = transform(word)
    while not correct(word):
        word = transform(word)
    print(alpha(word))

part1()
