data = """
Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1
"""

carac = {ligne.split()[0][:-1]:(int(ligne.split()[2][:-1]), int(ligne.split()[4][:-1]), int(ligne.split()[6][:-1]), int(ligne.split()[8][:-1]), int(ligne.split()[10])) for ligne in data.strip().split("\n")}
print(carac)


def calcule_score(carac, *n):
    vect = []
    vectors = list(carac.values())
    for nb_carac in range(len(vectors[0])-1): # on évite les calories
        val = 0
        for nb_cookie in range(len(vectors)):
            val += n[nb_cookie] * vectors[nb_cookie][nb_carac]
        if val < 0:
            val = 0
        vect.append(val)
    score = 1
    for val in vect:
        score *= val
    return score

# part1
def part1():
    max = 0
    for n1 in range(101):
        for n2 in range (101-n1):
            for n3 in range(101-n1-n2):
                n4 = 100 - n1 - n2 - n3
                score = calcule_score(carac, n1, n2, n3, n4)
                if score > max:
                    max = score
    print("part1: ", max)


# part2
def part2():
    print(list(carac.values()))
    max = 0
    for n1 in range(101):
        for n2 in range (101-n1):
            for n3 in range(101-n1-n2):
                n4 = 100 - n1 - n2 - n3
                cal = 0
                for id_cookie in range(len(carac.values())):
                    n = n1, n2, n3, n4
                    cal += list(carac.values())[id_cookie][-1] * n[id_cookie]
                if cal == 500:
                    score = calcule_score(carac, n1, n2, n3, n4)
                    if score > max:
                        max = score
    print("part2: ", max)

# part1()
part2()
