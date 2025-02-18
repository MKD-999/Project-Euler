import array as arr
import time as t


def prime_sieve(n: int) -> arr.array:
    primes = bytearray(n)
    primes[2] = 1

    for i in range(3, n, 2):
        primes[i] = 1

    for i in range(3, int(n ** 0.5) + 1, 2):  # Only odd nums can be prime
        for j in range(i ** 2, n, 2 * i):  # Takes care of multiples of odd nums
            primes[j] = 0  # Step is 2 * n as every second multiple of odd num is odd
            # 3 * 1 = 3 -> odd
            # 3 * 2 = 6
            # 3 * 3 = 9 -> odd
            # 3 * 4 = 12
            # 3 * 5 = 15 -> odd
    return arr.array('I', (i for i, prime in enumerate(primes) if prime))


strt = t.time()
prime_sieve(10 ** 7)
end = t.time()
print(end - strt)
