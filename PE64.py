import fractions as f
from time import time as t

def perfect_sq(a):

    if int(a**0.5)**2 == a:
        return True
    else:
        return False

strt = t()
ans = 0

'''
for i in range(2,10001):

    if perfect_sq(i) == False:
        l = []
        a = f.Fraction(float.as_integer_ratio(i**0.5)[0],float.as_integer_ratio(i**0.5)[1])

        while True:

            # Get integer part
            b = int(a.as_integer_ratio()[0]/a.as_integer_ratio()[1])
            l.append(b)

            if b != l[0]*2:

                # Get reciprocal of the difference between integer and fraction
                if a-l[-1] != 0:
                    c = f.Fraction(1,a-l[-1])

                    # Update current fraction
                    a = c

                else:
                    break

            else:
                break

        if (len(l)-1) % 2 == 1:
            myans += 1


    else:
        continue
        

'''
for i in range(2,10001):

    if perfect_sq(i) == False:
        mn = 0
        dn = 1
        a0 = int(i**0.5)
        an = a0

        l1 = [(a0,)]
        l2 = []

        while an != a0*2:

            mn = dn*an - mn
            dn = (i-(mn**2))/dn
            an = int((a0+mn)/dn)
            l2.append(an)

        l1.append(tuple(l2))
        if len(l1[1]) % 2 == 1:
            ans += 1

print(ans)
end = t()
print(end-strt)







