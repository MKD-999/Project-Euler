# Trial 1

# Given a number, we first start  prime factorizing the number
# We add the numbers, if we overshoot the number itself, we factorize further
# Since we are given the cardinality of the set, we can then determine how many 1s are needed to satisfy the condition
# Then we perform a check to see if the content adds up to the number


# What we need is a function that returns the number of factors of a number that we want
# For eg - If we were to give 100 as input to the function like this - [100]
# Its iterations will be -
# [2, 50]
# [2, 2, 25]
# [2, 2, 5, 5]

# But what if we need other factors which are not prime ?
# Like -
# [4, 25]
# [10, 10] etc ?

# Sometimes in order to get non - prime factors, we need to use non - primes

# We can try to implement a tree structure in order to use recursion
# It works like this - 
#                100
#               /   \
#              2     50
#                   /  \
#                  2    25
#                      /  \
#                     5    5
# So at every step we know the factors we are working with & those we have already seen
# Now I can clearly see the different ways to write the same number in terms of its factors

# Another example -
#           12
#          /  \
#         2    6
#             /  \
#            2    3

# In both the above examples, we have to consider the fact that whenever the power of a prime factor > 1
# in any factorization, we have to consider all the cases in which they can be represented

# For eg - 8 can be written as
# 2 x 2 x 2
# 2 x 4
# For bigger numbers there would be more ways. So we have to check for all the ways that the " k " value allows for
# As the constraint is 12000 -> We go upto 2 ^ 13 approx
# That would be 13 ways totally ONLY for 2
# Then combining with the other factors & doing the check would increase the time complexity


# Now the question of storing the factors at each step
# We can start with the original combo of the prime factor & non - prime factor that is given by n // prime

# If n = 12,
# factors = [[2, 6]]
# Factorizing 6, we have factors = [[2, 6], [2, 3]]

# If n = 28,
# factors = [[2, 14]]
# Factorizing 14, we have factors = [[2, 14], [2, 7]]

# If n = 120
# factors = [[2, 60]] -> [[2, 60], [2, 30], [2, 15], [3, 5]]
# This would be
#                120
#               /   \
#              2     60
#                   /  \
#                  2    30
#                      /  \
#                     2    15
#                         /  \
#                        3    5

# We now loop over the factors list & at every iteration of the loop we replace the number with its factors
# If we are at [2, 60] it now becomes [2, 2, 30] & then [2, 2, 2, 15] & then [2, 2, 2, 3, 5]
# We now have to take the different combinations of these factors
# Like [4, 30], [8, 15], [24, 5], [6, 20], [12, 10]
# This involves both grouping powers of same factors and different ways of combining the different factors

# Trial 2
# After trying to implement the above logic, I found it rather difficult to get the combinations of the
# different factors at each step. Also, most of the steps do not yield more than 1 fresh set
# Most of the fresh sets are derived from the last set which is the most basic prime factorization set

# So we might as well use that & derive all the factors from that
# This is the algo now

# 1. Generate all prime numbers upto a certain upper ceiling
# 2. Loop through numbers & check whether primes below the sqrt of the number & check if they are factors
# 3. We get the prime factorization
# 4. Get all the different combos for the powers & generate the different factors
# 5. Do the product sum check for the given value of k
"""
from primearray import prime_sieve
from time import time as t


def all_factors(factors: list) -> list:

    check = {}

    for factor in factors:

        if factor not in check:
            check[factor] = factors.count(factor)

    final = []

    for factor in check:

        if len(final) == 0:
            for power in range(1, check[factor] + 1):
                final.append(factor ** power)

        else:
            temp = [factor]

            for power in range(1, check[factor] + 1):
                for i in final:
                    temp.append(i * (factor ** power))

            final.extend(temp)

    return final


n = 10
primes = prime_sieve(n)
allprime = []

for i in range(2, n):

    pfactors = []
    if i not in primes:
        for prime in primes:

            while i % prime == 0:
                pfactors.append(prime)
                i //= prime

            else:
                continue

    else:
        pfactors.append(i)

    allprime.append(pfactors)
print(allprime)


k = 2
num = 4
answer = []
while k <= 6:

    found = False
    while not found:

        check = all_factors(allprime[num - 2])
        s = set()
        ans = dict()


        for i in check:

            container = frozenset([i, num // i])
            s.add(container)

        for i in s:

            ones = k - len(i)
            if sum(i) + ones == num:
                ans[k] = [num, i]
                answer.append(ans)
                found = True

            else:
                num += 1

print(ans)"""

# Recursion test

# If recursion is used, do I need to check divisibility with each number?
# A more efficient way would be to use it to search all factors (both prime & non prime)
# up to the square root & simultaneously use those factors to get the other number of the pair

# If we have n = 100
# We would use recursion up until 10, so we would get 2, 4,  5, & 10
# Using these numbers, we can get the other factors  50, 25, 20 & 10

# But the million-dollar question is would it be efficient when done mutiple times that too
# with numbers that only get larger & larger?

# Only one way to find out


"""
import math
from time import time

def recursion_v1(num: int, i: int, factors: list):

    # base case
    if i > math.ceil(num ** 0.5):
        return factors
    
    else:
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
        
        return recursion_v1(num, i + 1, factors)

"""

# ver 1 takes around 7 sec to get all factors of numbers until 100,000 but takes at least more than
# a minute to get to 500,000

# How can we optimize this function more ???

# So what we need now is a way to get the different ways of writing the factors
# For example if n = 100
# The recursive function returns [2, 50, 4, 25, 5, 20]
# But this is not an exhaustive list of the diff ways
# I need to have [2, [2, 25], [2, 2], [5, 5], 5, [2, 2, 5]]
# Do I?
# I don't think so now, as I have with every individual factor

# Need to recheck this logic

# Anyway now that we have the factors, what is left is deciding the number of factors
# k = cardinality of the set
# ones = k - len(factors)
# If the sum(factors) + ones == num, we have the answer for cardinality k

# But the problem comes when the same number can be written in terms of its prime factors
# For example when k = 4, the logic works when num = 8
# However for k = 5, it fails to do so because the answer is [2, 2, 2]
# which the current logic does not support
# So we need to get the prime factors
# So can we use recursion there too?
# Would it be efficient?
# Only one way to find out

# So the thing now is to get the full prime factorization of num
# Take all the diff combinations of the powers
# But how do we add recursion to this?

# But do I actually even need the full split???
# I anyway have the different non - prime factor split, thanks to the recursive function
# I only need to check the completely basic prime factorization of the number
# Is this valid?
# Only one way to find out

"""from primearray import prime_sieve

primes = prime_sieve(100_000)


def prime_fact(num: int) -> list:
    factors = []
    for prime in primes:

        if num % prime == 0:
            while num % prime == 0:
                factors.append(prime)
                num //= prime

    return factors


import math
from time import time


def recursion_v1(num: int, i: int, factors: list):
    # base case
    if i > math.ceil(num ** 0.5):
        return factors

    else:
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)

        return recursion_v1(num, i + 1, factors)
"""

# So now we have the non - prime splits from recursion_v1()
# And the completely prime split from prime_fact()
# What we need to do now is to use the same logic for product - sum check
# Get the cardinality , k
# ones = k - len(factors)
# if ones + sum(factors) == num, we have our number
# However, now we will be checking the same thing even with the full prime split
# Also, once we find an answer for a particular k, we know the answer for k + 1 is >= current answer
# Implementing that logic


"""strt = time()
k = 2
num = 4

ans = {}

while k <= 12000:

    found = False

    while not found:

        non_prime_factors = recursion_v1(num, 2, [])
        prime_factors = prime_fact(num)

        for i in range(0, len(non_prime_factors), 2):

            if i + 1 <= len(non_prime_factors) - 1:
                tochk = non_prime_factors[i: i + 2]
                ones = k - len(tochk)

                if ones + sum(tochk) == num:
                    ans[k] = num
                    found = True
                    break

            else:
                continue

        if not found:

            ones = k - len(prime_factors)

            if ones + sum(prime_factors) == num:
                ans[k] = num
                found = True

            else:
                num += 1

    k += 1

print(sum(set(ans.values())))
end = time()
print(end - strt)
"""

# However, I have just realized that under the recursion function we have assumed only 2 factors are possible
# But we know this need not be the case right?
# So another way of doing this would be if replaced the number with its non_prime factorization
# For eg if we had num = 16
# non_primes would be [2, 8, 4, 4]
# primes would be [2, 2, 2 ,2, 2]
# Under the current logic, the iters would be
# [2, 8] & [4, 4]
# NOW, we replace 8 with [2, 4] & 4 with [2, 2]
# This would make the prime_factors redundant !!!
# So we need a function which returns the factors of a number & then the factors of the factors
# But how many times would I need to do this?
# As long as all the factors are prime
# So for eg if num = 12
# iter1 -> [2, 6, 3, 4]
# iter2 -> [2, [2, 3], 3, [2, 2]]

# However if we have a highly divisible number like 120
# The iterations become too many & we call the recursive function too many times
# But I am still holding out hope that it would work, even if not fast enough

"""
import math
from primearray import prime_sieve


def recursion_v1(num: int, i: int, factors: list):
    # base case
    if i > math.isqrt(num):
        return factors

    else:
        if num % i == 0:
            temp = [i, num // i]
            factors.append(temp)

        return recursion_v1(num, i + 1, factors)


# Instead of calling the function many times, we will instead store a list of the factors
# for all numbers from 2 to 100K
# Whenever we encounter a number, we replace it with the factors from the generated list

all_factors = [0] * 150
for num in range(2, 150):
    all_factors[num] = recursion_v1(num, 2, [])

# Now that we have the factors for all the numbers, we simply need to keep substituting
# the factors until all the factors are prime
# So that is our base case

primes = prime_sieve(100_000)


# This function takes a list of factors, checks if the factors are prime or not
# If not prime, it fetches the factors of the factor from the all_factors & extends the given list
# If already prime, it simply returns the value


# A helper function to replace an element with the elements of a list
def merge(l1: list, n: int, l2: list) -> list:

    print(l1, n, l2)
    ind = l1.index(n)
    l1.pop(ind)
    toadd = 0

    for i in range(ind, len(l2) + 1):
        l1.insert(i, l2[toadd])
        toadd += 1

    return l1


def get_factors(factors: list) -> list:

    dup_factors = factors.copy()
    for factor in factors:

        if factor not in primes:
            for i in all_factors[factor]:
                print(merge(dup_factors, factor, i))

"""

# Ok I have realised the problem of scalability with this algo
# For the number 120 alone, I think I got a headache seeing the number of different cases this would split into
# I asked ChatGPT for a very very very small nudge to the right direction & it asked me to change my thinking

# Here is what it said -
# Stop thinking in terms of
#
# “Get all factors of a number, then break them further.”
#
# Instead, think in terms of
#
# “Build factor combinations directly.”


# So I think instead of looking at the final goal, we build the pathway to the final goal
# Start with a factor & recursively multiply with a factor greater than itself to get numbers
# But what about the cases where we multiply the number by itself ?
# We multiply as long as we do not exceed the limit which for now I have fixed as 100,000

# After that, how do I proceed ? Keep changing one of the 2s with a factor > 2 ?

import math as m
from time import time as t

strt = t()


# A helper function which takes care of generating the factors
# Since product grows faster than the sum, it is difficult to get sums that equal huge products
# If for the current factor combo the prod exceeds the sum, adding another factor is not going to help us
# Need to move on to the next number

# So the way we do this is by calculating the "k" needed instead of fixing the k and finding the solution for that particular k
# Then when we loop over the numbers, we get different numbers which require the same k. We take the smallest of them


def build_factors(placeholder: list, container: list, max_k: int) -> list:
    num = 2
    while True:
        dup = placeholder.copy()
        dup.append(num)
        prod = m.prod(dup)
        s = sum(dup)

        ones = prod - s
        k = ones + len(dup)
        if k > max_k:
            return container

        container.append(dup)
        num += 1


# Given a list of factors, I need a func that returns all the possible factors that can be built from it


def all_factors(placeholder: list, max_k: int) -> dict:
    chk = []
    build_factors(placeholder, chk, max_k)
    for i in chk:
        temp = []
        if build_factors(i, temp, max_k):
            chk.extend(temp)

    for j in chk:
        prod = m.prod(j)
        s = sum(j)
        ones = prod - s
        k = ones + len(j)

        if k > max_k:
            break

        else:
            try:
                if prod < ans[k][0]:
                    ans[k] = [prod, j]

            except KeyError:
                ans[k] = [prod, j]

    return ans


i = 2
max_k = 12000

ans = dict()

while i < 10_000:
    all_factors([i], max_k)
    i += 1


ohlordatlast = sum(set(ans[i][0] for i in ans))
print(ohlordatlast)
end = t()
print('------- %s seconds -------' % (end - strt))
