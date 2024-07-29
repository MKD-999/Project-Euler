import fractions as f

l = [0]*101
k = 1

for i in range(101):

    if i % 3 == 1:
        l[i] = 2*k
        k += 1

    else:
        l[i] = 1

a = 2
numer = 1
denom = l[0]

print(a,1)

frac = f.Fraction(numer,denom)
print(frac + a,2)


denom = f.Fraction(numer,l[1]) + l[0]
frac1 = f.Fraction(numer,denom) + a
print(frac1,3)

ans = 0
for i in range(2,101):

    denom = f.Fraction(numer,l[i]) + l[i-1]

    if i - 3 >= 0:
        frac = f.Fraction(numer,denom) + l[i-2]
        for j in range(i-3,-1,-1):
            frac = f.Fraction(numer,frac) + l[j]
        frac1 = f.Fraction(numer,frac) + a
        print(frac1,i+2)

    else:
        frac = f.Fraction(numer,denom) + l[i-2]
        frac1 = f.Fraction(numer,frac) + a
        print(frac1,i+2)

    if i+2 == 100:
        val = str(frac1.numerator)
        for v in val:
            ans += int(v)
print()
print()
print(ans)
print(val)


