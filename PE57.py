import fractions as f

numer = 1
denom = 2
cnt = 0

for i in range(1000):

    frac = f.Fraction(numer/denom) + 1
    denom = frac + 1

    if len(str(frac.numerator)) > len(str(frac.denominator)):
        cnt += 1
print(cnt)


