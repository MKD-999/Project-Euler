from primearray import prime_sieve
from time import time as t


def solution(limit: int) -> int:

    primes = prime_sieve(int(limit ** 0.5) + 1)

    answer = set()

    for x in primes:
        for y in primes:

            if x ** 2 + y ** 3 > limit:
                break

            else:
                for z in primes:

                    if x ** 2 + y ** 3 + z ** 4 < limit:
                        answer.add(x ** 2 + y ** 3 + z ** 4)

                    else:
                        break

    return len(answer)


strt = t()
print(solution(50_000_000))
end = t()
print(end - strt)
