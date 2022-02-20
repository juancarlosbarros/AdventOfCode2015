from collections import Counter
open('Day3.txt') as f:
    line = f.readline()
x = y = 0
cnt = Counter()
for symbol in line:
    if symbol == 'v':
        y += 1
    elif symbol == '^':
        y -= 1
    elif symbol == '<':
        x -= 1
    elif symbol == '>':
        x += 1
    cnt[(x, y)] += 1

print (cnt)