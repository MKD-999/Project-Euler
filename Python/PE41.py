from itertools import permutations as perm

def prime(a):
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 'n'

    else:
        return 'y'

l = '1234567'
a = perm(l)
for i in a:
    s = ''
    for j in i:
        s += j
    val = int(s)
    res = prime(val)
    if res == 'y':
        print(val)