from string import ascii_uppercase

alf = [str(i) for i in ascii_uppercase]
with open('6286.txt') as f:
    f = [i.strip() for i in f.readlines()]

o = []
for i in f:
    a = [0] * 26
    for j in range(len(i) - 1):
        if i[j] == 'X':
            a[alf.index(i[j+1])] += 1
    m = max(a)
    for g in range(26):
        if a[g] == m:
            o.append(alf[g])

n = list(set(o))
m = [o.count(i) for i in n]
print(max(m))