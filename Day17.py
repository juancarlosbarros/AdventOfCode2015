sizes = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]

# part 1


def distribution(sizes, repart, score, goal):
    Lsizes = len(sizes)
    Lrepart = len(repart)
    if Lrepart > Lsizes:
        bads(repart)
    elif score == goal:
        repart += (Lsizes - Lrepart) * [0]
        synthese(repart)
    elif score < goal and Lrepart < Lsizes:
        distribution(sizes, repart + [1], score + sizes[Lrepart], goal)
        distribution(sizes, repart + [0], score, goal)
    else:
        bads(repart)


def synthese(repart):
    global solutions
    solutions.append(repart)


def bads(repart):
    global garbage
    garbage.append(repart)


solutions = []
garbage = []
distribution(sizes, [], 0, 150)
hits = len(solutions)
looses = len(garbage)
print ( "Part1:", hits) # , " hits, ", looses, " bads. Total: ", hits + looses)

# Part2

nb_containers = [sum(repart) for repart in solutions]
min_containers = min(nb_containers)
part2 = nb_containers.count(min_containers)
print("Part2: ", part2) # , "ways of using ", min_containers, " containers (that's the minimum).")
