with open('7941.txt') as f:
    f = f.readline().split('FSRQ')
m = 0
for i in range(len(f)-81):
    a = len('FSRQ'.join(f[i:i+81]))
    m = max(m, a)
print(m)