def primesbtw(a,b):

    s = set()
    for i in range(a,b):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            s.add(i)
    return s

def prime(a):

    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 'n'
    else:
        return 'y'

def compute(*args):

    from itertools import combinations as combo
    l = [*args]
    combos = combo(l,2)
    for i in combos:

        s1 = ''
        s2 = ''
        for j in i:
            s1 += str(j)
        for j in reversed(i):
            s2 += str(j)

        if prime(int(s1)) == 'n' or prime(int(s2)) == 'n':
            return 'n'
    else:
        return 'y'



from time import time as t
strt = t()

primes = primesbtw(11,10000)
s = set()

for x in primes:
    for y in primes:
        if y > x:
            if prime(int(str(x)+str(y))) == 'y' and prime(int(str(y)+str(x))) == 'y':
                    for z in primes:
                        if z > x and z > y:
                            if compute(x,y,z) == 'y':
                                for a in primes:
                                    if a > x and a > y and a > z:
                                        if compute(x,y,z,a) == 'y':
                                            for b in primes:
                                                if b > x and b > y and b > z and b > a:
                                                    if compute(x,y,z,a,b) == 'y':
                                                        s.add(sum({x,y,z,a,b}))
                                                        print(min(s))
                                                        end = t()
                                                        print(end-strt)
                                                else:
                                                    continue

                                    else:
                                        continue

                        else:
                            continue
        else:
            continue


