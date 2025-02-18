import array as arr
from time import time as t


def primes_below(n: int) -> arr.array:
    primes = bytearray(n)
    primes[2] = 1

    for i in range(3, n, 2):
        primes[i] = 1

    for i in range(3, int(n ** 0.5) + 1, 2):
        for j in range(i ** 2, n, 2 * i):
            primes[j] = 0

    return arr.array('I', [i for i, prime in enumerate(primes) if prime])


strt = t()
n = 10
primes = primes_below(100)
# I settled for 100 once I checked that 100 alone can be written in 40899 ways
# using prime numbers

# Same logic as previous one but the only
# change is that the difference which we check in the outer loop
# can only be prime numbers

while True:
    l = [0] * (n + 1)
    l[0] = 1

    for i in primes:
        if i < n:
            for j in range(i, n + 1):
                l[j] += l[j - i]

        else:
            break

    if max(l) >= 5000:
        print(l.index(max(l)))
        break

    else:
        n += 1

end = t()
print("------- %s seconds -------" % (end - strt))
