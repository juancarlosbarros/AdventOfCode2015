f = open("Day18.txt")
data = f.readlines()
print(len(data), "lignes lues.")


def encadrer(table):
    """
    Encadre les lampes avec une ligne et une colonne au bord
    pour simuler les valeurs éteintes des voisines inexistantes
    :param table:
    :return:
    """
    l = len(table[0])
    res = [l * ['.']] + table + [l * ['.']]
    res2 = [[lamp for lamp in ['.'] + line + ['.']] for line in res]
    return res2


lamps = [[lamp for lamp in line.strip()] for line in data]
large_lamps = encadrer(lamps)
# print(large_lamps)

def evolution(init_table, part = 1):
    """
    transform a state of lamps in the next one (square table!)
    :param init_table: init_state (with borders added with off lamps)
    :return: next state (with borders too)
    """
    l = len(init_table)
    next_table = [['.' for _ in range(l)] for _ in range(l)]
    for line_nb in range(1, l-1):
        for col_nb in range(1, l-1):
            nb_on = neighbours_on(line_nb, col_nb, init_table)
            if init_table[line_nb][col_nb] == '.':
                if nb_on == 3:
                    next_table[line_nb][col_nb] = '#'
            if init_table[line_nb][col_nb] == '#':
                if nb_on >= 2 and nb_on <= 3:
                    next_table[line_nb][col_nb] = '#'
    if part == 2:
        next_table[1][1] = '#'
        next_table[1][l-2] = '#'
        next_table[l-2][1] = '#'
        next_table[l-2][l-2] = '#'
    return next_table


def neighbours_on(l, c, table):
    """
    Count number of '#' neighbours to the position [l][c] in table
    :param l: nb of line
    :param c: nb of column
    :param table: table of '.' (off) and '#' (on)
    :return: number of on lamps ('#')
    """
    nb = 0
    for delta_l in range(-1, 2):
        for delta_c in range(-1, 2):
            if delta_l != 0 or delta_c != 0:
                if table[l + delta_l][c + delta_c] == '#':
                    nb += 1
    return nb

def affiche_table(table):
    for line in table:
        print(line)
    print()

def affiche_voisins_on(table):
    l = len(table)
    for line in range(1, l-1):
        for col in range(1, l-1):
            print(neighbours_on(line, col, table), end = ' ')
        print('\n')


def nb_on_table(table):
    nb = 0
    for line in table:
        for carac in line:
            if carac == '#':
                nb += 1
    return nb


# Part1:
next = large_lamps[:][:]
for i in range(100):
    # print('Step: ', i, '-> Nb on: ', nb_on_table(next))
    # affiche_table(next)
    next = evolution(next)
print('Part1, Step: ', i+1, '-> Nb on: ', nb_on_table(next))

# Part1:
next = large_lamps[:][:]
for i in range(100):
    # print('Step: ', i, '-> Nb on: ', nb_on_table(next))
    # affiche_table(next)
    next = evolution(next, 2)
print('Part2, Step: ', i+1, '-> Nb on: ', nb_on_table(next))
