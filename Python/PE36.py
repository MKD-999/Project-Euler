def palin(a):

    a = str(a)
    if len(a) == 1:
        return 'y'

    elif len(a) % 2 == 0:
        mid1 = int(len(a)/2)
        mid2 = mid1 + 1
        l = list(a)

        if l[mid1-1] != l[mid2-1]:
            return 'n'
        else:
            val1 = ''
            val2 = ''
            for i in range(mid1-1):
                val = l[i]
                val1 += val
            for i in range(len(a)-1,mid2-1,-1):
                val = l[i]
                val2 += val
            if val1 == val2:
                return 'y'

    else:
        mid = int((len(a)/2) + 0.5)
        l = list(a)
        val1 = ''
        val2 = ''
        for i in range(mid-1):
            val = l[i]
            val1 += val

        for i in range(len(a)-1,mid-1,-1):
            val = l[i]
            val2 += val

        if val1 == val2:
            return 'y'

def drome(a):

    s = ''
    if len(str(a)) == 1:
        fin = bin(a)
        l = list(fin)
        l.pop(0)
        l.pop(0)
        rll = ''
        for i in l:
            rll += i

        final = palin(rll)
        if final == 'y':
            return 'y'

    while a != 1:
        rem = str(a % 2)
        s += rem
        if int(rem) == 0:
            a //= 2
        else:
            a = (a-1)//2
        if a == 1:
            s += '1'
    l = list(s)
    l.reverse()
    fin = ''
    for i in l:
        fin += i

    final = palin(fin)
    if final == 'y':
        return 'y'
    else:
        return 'n'

s = 0
for i in range(1,1000000):
    a = palin(i)
    if a == 'y':
        b = drome(i)
        if b == 'y':
            s += i

print(s)









