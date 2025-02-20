def deli(n):
    a = set()
    for i in range(1, n+1):
        if n%i == 0:
            a.add(i)
        if len(a)>2:
            return 0
    if list(a) == [1, n]:
        return n
    else:
        return 0
k = 1
for i in range(2943444, 2943529):
    b = deli(i)
    if b != 0:
        print(k, b)
        k += 1
