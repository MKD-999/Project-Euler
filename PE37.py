def prime(a):
    if a == 1:
        return 'n'

    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 'n'

    return 'y'
ans = 0
for i in range(11,1000000):

        a = prime(i)
        if a == 'y':
            final = True
            b = str(i)
            l = list(b)
            for j in range(len(l)-1):
                l2 = l[j+1:]
                val = ''
                for k in l2:
                    val += k

                val = int(val)
                fin = prime(val)
                if fin == 'n':
                    final = False
                    break

            if final == True:
                for j in range(len(l)-1,0,-1):
                    l2 = l[:j]
                    val = ''
                    for k in l2:
                        val += k

                    val = int(val)
                    fin = prime(val)
                    if fin == 'n':
                        final = False
                        break

                if final == True:
                    ans += i

print(ans)


