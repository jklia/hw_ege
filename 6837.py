with open('6837.txt') as f:
    f = f.readline().split('XYZ')
m = 0
for i in f:
    if i != '':
        if i[0] == 'X':
            m = max(m, len(i) - 3)
        else:
            m = max(m, len(i))
print(m)