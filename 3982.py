dva = []
i = 1
while 2**i <= 300000000:
    dva.append(2**i)
    i += 2

sem = []
i = 0
while 7**i <= 300000000:
    sem.append(7**i)
    i += 2

for m in range(len(dva)):
    for n in range(len(sem)):
        if 100000000 <= dva[m] * sem[n] <= 300000000:
            print(dva[m] * sem[n], m*2+1 + n*2)