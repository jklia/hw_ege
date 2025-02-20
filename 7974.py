import re
pat = re.compile(r'1[02468]2157[13579]*4')

for i in range(0, 10**10, 133):
    if re.fullmatch(pat, str(i)):
        print(i, i//133)