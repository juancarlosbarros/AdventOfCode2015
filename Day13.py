from itertools import permutations

with open('Day13.txt') as f:
    datas = f.readlines()
f.closed
happiness = {(s.split()[0], s.split()[10][:-1]):(s.split()[2], int(s.split()[3])) for s in datas}
for pair in happiness:
    if happiness[pair][0] == 'gain':
        happiness[pair] = happiness[pair][1]
    else:
        happiness[pair] = - happiness[pair][1]
people = set([pair[0] for pair in happiness.keys()])

happiness1 = {}
for pers in people:
    happiness1[('me', pers)] = 0
    happiness1[(pers, 'me')] = 0

people2 = people.union({'me'})
happiness2 = happiness | happiness1

# part 1
def total_hapiness(disposition, happiness = happiness):
    disposition.append(disposition[0])
    res = 0
    for i in range(len(disposition) - 1):
        res += happiness[disposition[i],disposition[i+1]]
        res += happiness[disposition[i+1],disposition[i]]
    return res


def part1():
    print(happiness)
    print(people)
    score_min = 1e10
    score_max = 0
    for disposition in permutations(people):
        score = total_hapiness(list(disposition))
        print(disposition, score)
        if score < score_min:
            score_min = score
            print("min: ", score_min, score, disposition)
        if score > score_max:
            score_max = score
            print("max: ", score_max, score, disposition)
    print("min : ", score_min)
    print("max : ", score_max)

def part2():
    print(happiness2)
    print(people2)
    score_min = 1e10
    score_max = 0
    for disposition in permutations(people2):
        score = total_hapiness(list(disposition), happiness2)
        print(disposition, score)
        if score < score_min:
            score_min = score
            print("min: ", score_min, score, disposition)
        if score > score_max:
            score_max = score
            print("max: ", score_max, score, disposition)
    print("min : ", score_min)
    print("max : ", score_max)


part2()
