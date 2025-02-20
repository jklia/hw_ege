def deli(n):
    a = set()
    for i in range(1, n+1):
        if n%i == 0:
            a.add(i)
    if len(a) != 6:
        return []
    else:
        a = list(a)
        a.sort(reverse=True)
        return a[1:3]
for i in range(157898, 157991):
    b = deli(i)
    if b:
        print(b)
