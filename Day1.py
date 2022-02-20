with open('Day1.txt') as f:
    datas = f.readline()
f.closed
# print(type(datas))

level = 0
for i in range(len(datas)):
    if datas[i] == '(':
        level += 1
    else:
        level -= 1
print(level)

level = 0
for i in range(len(datas)):
    if datas[i] == '(':
        level += 1
    else:
        level -= 1
        if level == -1:
            print(i+1)
            break
print(level)


