from time import time as t


def prime_factors(a):
    prime_factors = []
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53]

    for i in primes:
        if a % i == 0:
            prime_factors.append(i)
            if a // i not in prime_factors:
                if a // i != 1:
                    prime_factors.append(a // i)

    return prime_factors


def totient(a):
    final = 1
    for i in prime_factors(a):
        final *= (1 - (1 / i))

    final *= a

    return final


strt = t()
tochk = 0
ans = 0

for i in range(2, 1000001):

    if (i / totient(i)) > tochk:
        tochk = i / totient(i)
        ans = i

end = t()

print(ans)
print(tochk)
print(end - strt)
