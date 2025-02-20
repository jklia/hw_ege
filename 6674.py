with open('6674.txt') as f:
    f = f.readline().split('Z')
m = 10**6
for i in range(1, len(f)-118):
    a = len(''.join(f[i:i+119])) + 120
    m = min(m, a)
print(m)