import fractions

s = 1
for i in range(11,100):
    for j in range(12,100):
        if i < j:
            for k in str(i):
                if k in str(j):
                    if k != '0':
                        frac1 = fractions.Fraction(i,j)
                        a = list(str(i))
                        b = list(str(j))
                        a.remove(k)
                        b.remove(k)
                        val1 = ''
                        val2 = ''
                        for l in a:
                            val1 += l
                        for m in b:
                            val2 += m

                        val1 = int(val1)
                        val2 = int(val2)
                        if val2 != 0:
                            frac2 = fractions.Fraction(val1,val2)
                            if frac2 == frac1:
                                s *= frac2
print(s.denominator)