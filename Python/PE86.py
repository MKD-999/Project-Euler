import math


l1 = []
a = b = c = 1

for m in range(1, int(1000 ** 0.5)):
    for n in range(1, m):

        if math.gcd(m, n) == 1 and (m + n) % 2 == 1:

            a = int(2 * m * n)
            b = int((m ** 2) - (n ** 2))
            c = int((m ** 2) + (n ** 2))

            k = 1
            while all(x <= 100 for x in (k * a, k * b, k * c)):

                l1.append({k * a, k * b, k * c})
                k += 1

        else:
            continue

print(len(l1))
