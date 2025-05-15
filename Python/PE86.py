# Given a cuboid of length l, breadth b and height h,
# We know the shortest distance is a pythagorean triplet of the form (l, (b + h), x) where x is some unknown constant
# Which implies that the square root of l**2 + (b + h)**2 must be a perfect square

# We fix l and then loop over all possible values of b + h
# We have the constraints b <=l & h <= l
# This implies that the least value for both b & h is 1 and the biggest value for both is l
# Therefore all the possible values of b + h are [2, 2 * l]

# Because we have only 2 numbers involved in the sum b + h = s, we can directly find the number of partitions of s
# If s <= l -> no of partitions are s // 2
# If s > l -> This does not imply that the individual values are still greater than l
# The number of valid partitions of s when s > l is (2*l -s + 1) // 2 or l - (s - 1) // 2

from time import time as t

strt = t()
cnt = 0
l = 0

while cnt < 1_000_000:

    l += 1
    for bh in range(2, 2 * l + 1):

        if int((l ** 2 + bh ** 2) ** 0.5) ** 2 == l ** 2 + bh ** 2:

            if bh <= l:
                cnt += bh // 2

            else:
                cnt += l - (bh - 1) // 2

print(l)
end = t()
print("------- %s seconds -------" % (end - strt))
