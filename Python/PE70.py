from time import time as t


def primes_below(a):
    primes = []

    for i in range(2, a + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)

    return primes


def prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    else:
        return True


strt = t()

primes = primes_below(5 * 10 ** 3)
tochk = 10 ** 7
ans = 0

for i in primes:
    for j in primes:
        if i != j:
            if i * j < 10 ** 7:
                if sorted(list(str(i * j))) == sorted(list(str((i - 1) * (j - 1)))):
                    if (i * j) / ((i - 1) * (j - 1)) < tochk:
                        tochk = (i * j) / ((i - 1) * (j - 1))
                        ans = i * j

print(ans, tochk)
end = t()
print('------- %s seconds -------' % (end - strt))
