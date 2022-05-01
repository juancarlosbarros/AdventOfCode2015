f = open("Day16.txt")
data = f.readlines()
# print(len(data), "caractères lus.")
Sues = {line.strip().split()[1][:-1]:{line.strip().split()[2][:-1]:int(line.strip().split()[3][:-1]), line.strip().split()[4][:-1]:int(line.strip().split()[5][:-1]), line.strip().split()[6][:-1]:int(line.strip().split()[7])} for line in data}

ticker_tape = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
# ticker_tape = {'children': 3, 'cats': 7, 'samoyeds': 9, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 9, 'trees': 3, 'cars': 0, 'perfumes': 1}


def check_Sue_Part1(param_Sue, ticker_tape):
    for key, value in ticker_tape.items():
        wrong = key in param_Sue and param_Sue[key] != value
        if wrong:
            return False
    return True


def check_Sue_Part2(param_Sue, ticker_tape):
    for key, value in ticker_tape.items():
        if key == 'cats' or key == 'trees':
            wrong = key in param_Sue and param_Sue[key] <= value
        elif key == 'pomeranians' or key == 'goldfish':
            wrong = key in param_Sue and param_Sue[key] >= value
        else:
            wrong = key in param_Sue and param_Sue[key] != value

        if wrong:
            return False
    return True


# part1
print('Part 1:')
for Sue, param_Sue in Sues.items():
    if check_Sue_Part1(param_Sue, ticker_tape):
        print(Sue)

# part2
print('Part 2:')
for Sue, param_Sue in Sues.items():
    if check_Sue_Part2(param_Sue, ticker_tape):
        print(Sue)
