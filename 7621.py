def deli(n):
    m = 0
    for i in range(2, n):
        if n%i == 0:
            m += i
            m += n//i
            return str(m)
    return '0'
k = 0
n = 800001
while k < 5:
    m = deli(n)
    if m[-1] == '4':
        print(n, m)
        k += 1
    n += 1