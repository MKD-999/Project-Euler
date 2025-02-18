# DP trial 1

# For every number below n store all the  ways to get that number


# As 1 cannot be written as the sum of 2 numbers >= 1,
# No of ways to write 1 is 0

# By default, every number n can be written as 1 added n times


# no of ways to get 1
# Total -> 0 -> (1)

# no of ways to get 2
# -> 1 + 1 -> (1) + (1) -> 0
# Total -> 0 + default -> 1 -> (2)

# no of ways to get 3
# -> 1 + 2
# -> 1 + 1 + 1
# Total -> 2 -> (3)

# Our method should give :
# -> 1 + 2 -> (1) + (2) -> 1
# Total -> 1 + default = 2 -> (3)


# no of ways to get 4
# -> 1 + 1 + 1 + 1
# -> 2 + 1 + 1
# -> 2 + 2
# -> 3 + 1
# Therefore 4 ways

# Our method should give:
# -> 1 + 3 -> (1) + (3) -> 2
# -> 2 + 2 -> ((2) + (2)) / 2 -> 1
# Total -> 3 + default = 4 -> (4)

# -> 2 + 2 -> ((2) + (2)) / 2 -> 1
# We are dividing by 2 because

# No of ways of writing 2 + 2
# Splitting up the 2nd 2
# -> 2 + 1 + 1
# Splitting up the 1st 2
# -> 1 + 1 + 2

# They are just permutations of each other

# Whenever n is being written as some m + m, that is 2 * m
# we need to add (m) only once


# no of ways to get 5
# -> 1 + 1 + 1 + 1 + 1
# -> 2 + 1 + 1 + 1
# -> 2 + 2 + 1
# -> 3 + 2
# -> 3 + 1 + 1
# -> 4 + 1
# Therefore 6 ways

# Our method should give:
# -> 1 + 4 -> (1) + (4) -> 4
# -> 2 + 3 -> (2) + (3) -> 1 + 2 -> 3 , But the no of ways is only 6 !!

# No of ways of writing 2 + 3 (without default)
# -> 2 + 2 + 1 !!!!
# -> 2 + 1 + 1 + 1 !!!!
# -> 1 + 1 + 3 !!!!


# No of ways of writing 4 + 1
# -> 3 + 2 !!!!
# -> 3 + 1 + 1 !!!!
# -> 2 + 1 + 1 + 1 !!!!


# All !!!! are the repeating sequences
# Have to remove the intersections between the 2 cases

# Every form of the composition can be transformed into another
# So we need to consider only 1 composition and just add the number of ways we can get compositions

# In this case:
# -> Start with (1) + (n - 1)
# -> Add (n - 1)
# -> Go up to half of n and add 1 to total at each step
# -> If n can be written as 2 * m, that is n is even, add (n//2), that is (m)
# -> Add default

# So it would now be:
# No of ways of writing 5
# Total = 0
# 1 + 4 -> (1) + (4) -> 4
# 2 + 3 -> 1
# Add default
# Total -> 6


# No of ways of writing 6:
# -> 1 + 5 -> (1) + (5) -> 6
# -> 2 + 4 -> 1
# -> 3 + 3 -> (3) -> 2
# -> Add default
# Total -> 10


# No of ways to write 7:
# -> 1 + 6 -> (1) + (6) -> 10
# -> 2 + 5 -> 1
# -> 3 + 4 -> 1
# -> Add default
# Total -> 13

"""
n = 10
l = [0] * n


for i in range(2, n + 1):
    total = 1
    total += l[i - 2]
    for j in range(2, (i // 2) + 1):
        if j == i / 2:
            total += l[j - 1]
        else:
            total += 1
    l[i - 1] = total

for i in l:
    print(l.index(i) + 1, i)
"""

# DP trial 2
# So our previous approach was not giving the correct answer
# Looks like we started correctly, but the problems we took care of were only the simplest of the problems
# Partitions are much more complex than that

# Just by looping up to n / 2 does not guarantee that we don't count repetitions
# Also all algos specify using l[0] as 1, that we can make 0 in one way, by not choosing any integer

# So had to look up some dp algos

# Found this beautiful algo online
# Let's break this down

# Creating a list which initially has all values set to 0
# Now as discussed, 0 can be written in 1 way

# So we start the outer loop from 1 to n -> i
# The inner loop goes from i to n -> j
# Basically j takes all values, n >= j >= i

# If n = 5
# When i = 1
# j takes -> 1, 2, 3, 4, 5
# l = [1, 0, 0, 0, 0, 0]

# Now, j - i -> 0, 1, 2, 3, 4
# l[j] += l[j - i] makes all the values in the list become 1

# I think this represents the default way in our previous algo
# That is, every number n can be written as a sum of n 1's

# Now when i = 2
# j takes -> 2, 3, 4, 5
# l = [1, 1, 1, 1, 1, 1]

# j - i -> 0, 1, 2, 3
# l[j] += l[j - i]

# l = [1, 1, 2, 2, 3, 3]

# This algo stores all the  ways to find each number below n
# And thus even computes no of ways to write n

# If n = 3
# i can take values -> 1, 2, 3
# When i = 1,
# j -> 1, 2, 3
# This stores all the ways 1, 2 and 3 can be written using 1

# When i = 2
# j can take -> 2, 3
# This stores all the ways 2, 3 can be written using 2
# AND ADDS IT TO THE NUMBER OF WAYS I CAN WRITE THEM AS THE SUM OF 1's

# When i = 3
# j can take -> 3
# This stores all the ways 3 can be written using 3
# AND ADDS IT TO THE NUMBER OF WAYS I CAN WRITE THEM AS THE SUM OF 1's and 2's

# As we are interested only in the case where we can write a number as a sum of at least 2 nums
# We can avoid the last step,
# that is, we can only loop from 1 to n

# THUS it takes care of all the possible ways because of " += "


# We avoid over counting by starting the inner loop from i to n
# Meaning j can only take values from i to n
# If i = 3
# j -> 3, 4, 5
# So when n = 5
# 2 + 3 is counted when i = 2
# 3 + 2 is not even considered, because the loop starts from 3(i), 3(j)


# Converting this algo into a function


from time import time as t


def partitions(n: int) -> int:

    l = [0] * (n + 1)
    l[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            l[j] += l[j - i]

    return l[n]


strt = t()
print(partitions(100))
end = t()
print("------- %s seconds -------" % (end - strt))
