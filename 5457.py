from functools import reduce
from operator import mul
def deli(n):
    m = []
    s = 0
    u = 1
    for i in range(1, int(n**0.5)+2):
        if n%i == 0:
            if i not in m:
                m.append(i)
                s += i
                u = u*i
            if n//i not in m:
                m.append(n//i)
                s += n//i
                u = u*(n//i)
    m = list(m)
    m.sort(reverse=True)
    return m, s, u

def prost(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
k = 0
n = 2000001
while k < 6:
    m, s, u= deli(n)
    if len(m) > 30 and s%2 == 1 and u%2 == 1:
        for i in range(1, len(m)):
            if prost(m[i]):
                print(n, m[i])
                k += 1
                break
    n += 1