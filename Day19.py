import time
import functools

f = open("Day19.txt")
data = f.readlines()
print(len(data), "lignes lues.")
data = [line.strip().split() for line in data]
atoms = {line[0] for line in data if len(line) > 1}
new_atoms = {line[-1] for line in data if len(line) > 1}

transfs_tot = {atom: [] for atom in atoms}
for transf in data:
    if len(transf) > 1:
        transfs_tot[transf[0]].append(transf[-1])

transfs_init = {atom: [] for atom in atoms}
for transf in data:
    if len(transf) > 1:
        if transf[-1][:3] == 'CRn':
            transfs_init[transf[0]].append(transf[-1])

transfs_non_init = {atom: [] for atom in atoms}
for transf in data:
    if len(transf) > 1:
        if transf[-1][:3] != 'CRn':
            transfs_non_init[transf[0]].append(transf[-1])

transfs_inv = {new_atom: [] for new_atom in new_atoms}
for transf in data:
    if len(transf) > 1 and transf[0] != 'e':
        transfs_inv[transf[-1]] = transf[0]

medic = data[-1][0]
len_medic = len(medic)
print("atoms: ", atoms)
print("transfs: ", transfs_tot)
print("medic: ", medic)
UPPERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERS = UPPERS.lower()
"""
def transformation(medic, ):
    return molecules
"""

# Part 1
i = 0
molecules = set()
stable_atoms = set()
stable_structure = []
while i < len(medic):
    delta = 1
    if medic[i] in UPPERS:
        if i+1 == len(medic) or medic[i + 1] in UPPERS:
            atom = medic[i]
        elif medic[i + 1] in LOWERS:
            delta += 1
            atom = medic[i] + medic[i + 1]
        else:
            raise RuntimeError("bad datas...")
        if atom in atoms:
            molecules = molecules | {medic[:i] + transf + medic[i + delta:] for transf in transfs_tot[atom]}
        else:  # for Part 2 !
            stable_atoms = stable_atoms | {atom}
            stable_structure.append(atom)
    i += delta
print("Part 1: ", len(molecules))


# Part 2 a
# A partir d'un ensemble de molécules faisable en n étapes,
# construire l'ensemble des molécules faisables en n+1 étapes
# Dès qu'on trouve le médicament dans un ensemble, s'arrêter...
def Part2a():
    def print_stats_len(molecules):
        lenghts = [len(mol) for mol in molecules]
        print("length... min: ", min(lenghts), "max: ", max(lenghts))


    @functools.cache
    def is_acceptable(molecule):
        if 'C' in molecule[1:]:
            # dico[molecule] = False
            return False
        if molecule.count('Rn') > 34:
            # dico[molecule] = False
            return False
        if molecule.count('Ar') > 34:
            # dico[molecule] = False
            return False
        if molecule.count('Y') > 7:
            # dico[molecule] = False
            return False
        if len(molecule) > len_medic:
            # dico[molecule] = False
            return False
        # dico[molecule] = True
        return True


    def transformation(old_molecules, transfs):
        new_molecules = set()
        for molecule in old_molecules:
            i = 0
            while i < len(molecule):
                delta = 1
                if molecule[i] in UPPERS or molecule[i] == 'e':
                    if i+1 == len(molecule) or molecule[i + 1] in UPPERS:
                        atom = molecule[i]
                    elif molecule[i + 1] in LOWERS:
                        delta += 1
                        atom = molecule[i] + molecule[i + 1]
                    else:
                        raise RuntimeError("bad datas...")
                    if atom in atoms:
                        for transf in transfs[atom]:
                            new_molecule = molecule[:i] + transf + molecule[i + delta:]
                            if new_molecule not in old_molecules and is_acceptable(new_molecule):
                                new_molecules = new_molecules | {new_molecule}
                i += delta
        return new_molecules


    print("stable_atoms: ", list(stable_atoms) )
    print("stable_structure: ", stable_structure)
    for stable_atom in stable_atoms:
        print(stable_atom, stable_structure.count(stable_atom))

    new_molecules = {"e"}
    new_molecules = transformation(new_molecules, transfs_tot)
    new_molecules = transformation(new_molecules, transfs_init)
    i = 2
    top = time.time()
    while medic not in new_molecules:
        print(i, " substitution(s)", len(new_molecules), "molecules, ", time.time()-top, "s")
        # stats_len(new_molecules)
        new_molecules = transformation(new_molecules, transfs_non_init)
        i += 1
    print("C'est bon!", i)

# Part 2 b
# partir de la fin et remonter le temps
def Part2b():
    def transformation_inv(new_molecules, transfs_inv):
        old_molecules = set()
        for molecule in new_molecules:
            for new_atom, old_atom in transfs_inv.items():
                if new_atom in molecule:
                    index = -1
                    for i in range(molecule.count(new_atom)):
                        index = molecule.find(new_atom, index+1)
                        old_molecule = molecule[:index] + old_atom + molecule[index+len(new_atom):]
                        old_molecules = old_molecules | {old_molecule}
        return old_molecules


    old_molecules = {medic}
    i = 0
    while 'e' not in old_molecules:
        old_molecules = transformation_inv(old_molecules, transfs_inv)
        i += 1
        print(i, " transformations")
        print(len(old_molecules))

Part2a()
# Part2b()
