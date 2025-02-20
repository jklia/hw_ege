with open('7496.txt') as f:
    f = f.readline().split('AF')
m = 10**6
for i in range(1, len(f)-199):
    a = len(''.join(f[i:i+200])) + 2*201
    m = min(m, a)
print(m)

