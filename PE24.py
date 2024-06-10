from itertools import permutations as perm

a = list(perm('0123456789'))
a.sort()
x = a[999999]
s = ''
for i in x:
    s += i

print(s)
