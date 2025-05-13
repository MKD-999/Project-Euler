from itertools import permutations as perm
from time import time
def primes(a):

    l = []
    for i in range(2,a+1):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break

        else:
            l.append(i)
    return l
strt = time()
pri = primes(18)

a = perm('0123456789')
ans = 0

for i in a:
    s = ''
    ind = 1
    for j in i:
        s += j

    l = []
    while ind + 2 < 10:
        val = s[ind:ind+3]
        ind += 1
        l.append(int(val))

    for value in l:
        index = l.index(value)
        tochk = pri[index]
        if value % tochk != 0:
            break

    else:
        ans += int(s)
print(ans)
fin = time()
print(fin-strt)