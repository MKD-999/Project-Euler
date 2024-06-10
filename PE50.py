from time import time

def primes(a):

    l = []
    for i in range(2,a):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            l.append(i)
    return l

def prime(a):
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 'n'
    else:
        return 'y'

strt = time()
a = primes(1000000)
i = 0
s = 0
cnt = 0
l = []

while i < len(a):
    for j in range(i,len(a)):

        s += a[j]
        cnt += 1
        if s < 1000000:
            if prime(s) == 'y':
                l.append([s, cnt])

        else:
            break

    i += 1
    cnt = 0
    s = 0



lens = []
for i in l:
    lens.append(i[1])

ind = lens.index(max(lens))
print(l[ind])

fin = time()
print(fin-strt)

