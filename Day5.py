with open('Day5.txt') as f:
    datas = f.readlines()
f.closed


# part 1
def three_voyels(word):
    voyels = 0
    for lettre in word:
        if lettre in "aeiou":
            voyels += 1
            if voyels >= 3:
                return True
    return False


def double_lettre(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False


def does_not(word):
    forbiddens = ['ab', 'cd', 'pq', 'xy']
    for forbidden in forbiddens:
        if forbidden in word:
            return False
    return True


count1 = 0
for word in datas:
    if three_voyels(word) and double_lettre(word) and does_not(word):
        count1 += 1
print('partie 1: ', count1)


# part 2

def double_repetition(word):
    for i in range(len(word) - 3):
        pattern = word[i:i+2]
        if pattern in word[i + 2:]:
            return True
    return False


def repetition_one_between(word):
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            return True
    return False

count2 = 0
for word in datas:
    if double_repetition(word) and repetition_one_between(word):
        count2 += 1
print('partie 2: ', count2)
