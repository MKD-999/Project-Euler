import fractions as f
from time import time as t

strt = t()
l = []

tochk = '42857142857142857142857142857143'

for denom in range(999991, 1000000):

    length = len(str(denom))
    val = int(tochk[:length])
    for numer in range(val - 3, val + 3):
        if 0.42 <= numer / denom <= 0.43:
            l.append(f.Fraction(numer, denom))

l.sort()
ind = l.index(f.Fraction(3, 7))
print(l[ind - 1].numerator)

end = t()
print(end - strt)
