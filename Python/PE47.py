from time import time

def prime(a):
     for i  in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 'n'

     else:
         return 'y'



def primefact(a):

    if prime(a) == 'y':
        return [a]

    l = []

    for i in range(2,int(a**0.5)+1):
        if prime(i) == 'y':
            if a % i == 0:
                l.append(i)
                a //= i
    if a != 1:
        if prime(a) == 'y':
            l.append(a)

        else:
            l1 = set(primefact(a))
            return set(l).union(l1)

    return set(l)

strt = time()
cnt = True
i = 210

while cnt:

    if len(primefact(i)) == 4:
        if len(primefact(i+1)) == 4:
            if len(primefact(i+2)) == 4:
                if len(primefact(i+3)) == 4:
                    print(i, i+1, i+2, i+3)
                    break

    i += 1

fin = time()
print(fin-strt)