n = 500000000
def f(n):
    a = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            a.add(i)
            a.add(n//i)
        if len(a)>3:
            return []
    a.add(1)
    a.add(n)
    return list(a)
o = 0
k = 1
while o < 5:
    g = n+k
    b = f(g)
    if b:
        del b[b.index(g)]
        print(k, max(b))
        o += 1
    k += 1
