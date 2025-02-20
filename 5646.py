import re

with open('5646.txt') as f:
    f = f.readline().split('KK')
m = 0
pattern = r'43\d{2}78\d{3}34'
for i in f:
    if len(i) == 11:
        if re.fullmatch(pattern, i):
            m = max(m, int(i))
o = 1
m = str(m)
for j in range(11):
    if j%2 == 0:
        o = o*int(m[j])
print(m)
print(o)