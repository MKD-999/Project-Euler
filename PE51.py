from itertools import permutations as perm
from time import time

def prime(a):
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 'n'
    return 'y'

'''
strt = time()
l = []
toapp = 1
while toapp < 10:
    for i in range(1,10):
        for k in range(1,10):
                val = '___' + str(toapp) + str(i) + str(k)
                perms = perm(val)
                for j in perms:
                    if list(j) not in l:
                        l.append(list(j))
    toapp += 1

final = []
for i in l:
    cnt = 0
    toapp = 0
    fin = []
    while toapp < 10:
        val = ''
        for j in i:
            if j == '_':
                j = str(toapp)
                val += j
            else:
                val += str(j)
        toapp += 1
        if int(val[-1]) % 2 != 0:
            if int(val[-1]) % 5 != 0:
                if int(val) > 100000:
                    if prime(int(val)) == 'y':
                        cnt += 1
                    fin.append([val,cnt])
                    

    final.append(fin)

for i in final:
    for j in i:
        if int(j[0]) > 100000:
            if j[1] == 8:
                print(i)
end = time()
print(end-strt)


'''
def primes_btw(a,b):

    l = []
    for i in range(a,b):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            l.append(i)

    return l

def recur(a):
    for i in (str(a)):
        if str(a).count(i) == 3:
            return ['y',i]

    return 'n'

def mask(a):

    if recur(a)[0] == 'y':
        a = str(a)
        tochng = str(recur(a)[1])
        for i in a:
            if i == tochng:
                a = a.replace(i,'_')
        toapp = 0
        fin = []
        cnt = 0
        while toapp < 10:
            dupa = a
            dupa = dupa.replace('_',str(toapp))
            if int(dupa) > 100000:
                if prime(int(dupa)) == 'y':
                    cnt += 1
                fin.append([dupa,cnt])
            toapp += 1
        return fin

strt = time()
a = primes_btw(100000,1000000)
vals = []
for i in a:
    if recur(i)[0] == 'y':
        if recur(i)[1]  in ['0','1','2']:
            a = mask(i)
            for j in a:
                if j[1] == 8:
                    print(a)

end = time()
print(end-strt)