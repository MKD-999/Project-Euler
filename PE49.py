from itertools import permutations as perm

def prime(a):

    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 'n'
    else:
        return 'y'

finl = []
for i in range(1487,10000,2):

    if prime(i) == 'y':
        l = set()
        for j in perm(str(i)):
            s = ''
            for k in j:
                s += k
            if prime(int(s)) == 'y':

                l.add(int(s))
        l1 = list(l)
        l1.sort()
        finl.append(l1)


rllyfinal = []
for i in finl:
        l1 = []
        for j in range(len(i)):
            for k in range(j+1,len(i)):
                diff = i[k] - i[j]
                if i[k] + diff in i:
                    l1.append([i[j],i[k],i[k] + diff])

        if len(l1) > 0:
            if l1 not in rllyfinal:
                rllyfinal.append(l1)
ans = rllyfinal[1]
s = ''
for i in ans:
    for j in i:
        s += str(j)

print(s)

