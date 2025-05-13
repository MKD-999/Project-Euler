def prime(a):

    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 'NP'
    else:
        return 'P'

def cprime(a):

    a = str(a)
    for i in range(len(a)):
        val = a[i:len(a)] + a[0:i]
        val = int(val)
        b = prime(val)
        if b == 'NP':
            return 'NC'
    else:
        return 'C'

cnt = 0
for i in range(2,1000001):
    if prime(i) == 'P' and cprime(i) == 'C':
        cnt += 1

print(cnt)