import fractions as f
from time import time as t


def perfect_sq(a):
    if int(a ** 0.5) ** 2 == a:
        return True
    else:
        return False


strt = t()
ans = 0
chk = 0

for i in range(2, 1001):

    if perfect_sq(i) == False:
        mn = 0
        dn = 1
        a0 = int(i ** 0.5)
        an = a0

        l1 = [a0]
        l2 = []

        while an != a0 * 2:
            mn = dn * an - mn
            dn = (i - (mn ** 2)) / dn
            an = int((a0 + mn) / dn)
            l2.append(an)

        if len(l2) % 2 == 0:
            l2.pop(-1)

            for j in l2:
                l1.append(j)

            numer = 1
            if len(l1) >= 3:
                denom = l1[-1] + l1[-2]

                frac = f.Fraction(numer, denom)

                for j in range(-3, -len(l1), -1):
                    denom = l1[j] + frac
                    frac = f.Fraction(numer, denom)

                frac += l1[0]
                if frac.numerator > chk:
                    chk = frac.numerator
                    ans = i

            else:
                denom = l1[-1]
                frac = f.Fraction(numer, denom) + l1[-2]

                if frac.numerator > chk:
                    chk = frac.numerator
                    ans = i


        else:
            l2 *= 2
            l2.pop(-1)

            for j in l2:
                l1.append(j)

            numer = 1
            if len(l1) >= 3:
                denom = l1[-1] + l1[-2]

                frac = f.Fraction(numer, denom)

                for j in range(-3, -len(l1), -1):
                    denom = l1[j] + frac
                    frac = f.Fraction(numer, denom)

                frac += l1[0]
                if frac.numerator > chk:
                    chk = frac.numerator
                    ans = i

            else:
                denom = l1[-1]
                frac = f.Fraction(numer, denom) + l1[-2]

                if frac.numerator > chk:
                    chk = frac.numerator
                    ans = i

print(ans)
end = t()
print(end - strt)
