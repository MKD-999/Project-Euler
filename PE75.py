import math
from collections import Counter
from time import time as t

strt = t()

l1 = []
a = b = c = 1

for m in range(1, int(1500000 ** 0.5)):
    for n in range(1, m):

        if math.gcd(m, n) == 1 and (m + n) % 2 == 1:

            a = int(2 * m * n)
            b = int((m ** 2) - (n ** 2))
            c = int((m ** 2) + (n ** 2))

            k = 1
            while k * (a + b + c) <= 1500000:
                l1.append(k * (a + b + c))
                k += 1

        else:
            continue

ans = 0
count = Counter(l1)

for i in count:
    if count[i] == 1:
        ans += 1

print(ans)
end = t()
print("------- %s seconds -------" % (end - strt))
