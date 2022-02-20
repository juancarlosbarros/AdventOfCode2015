from collections import Counter
with open('Day3.txt') as f:
    line = f.readline()
# part 1
x = y = 0
cnt1 = Counter()
for symbol in line:
    if symbol == 'v':
        y += 1
    elif symbol == '^':
        y -= 1
    elif symbol == '<':
        x -= 1
    elif symbol == '>':
        x += 1
    cnt1[(x, y)] += 1
print ('réponse 1:', len(cnt1))

# part 2
x = [0, 0]
y = [0, 0]
turn = 0
cnt2 = Counter()
for symbol in line:
    turn += 1
    turn %= 2
    if symbol == 'v':
        y[turn] += 1
    elif symbol == '^':
        y[turn] -= 1
    elif symbol == '<':
        x[turn] -= 1
    elif symbol == '>':
        x[turn] += 1
    cnt2[(x[turn], y[turn])] += 1

print ('réponse 2:', len(cnt2))