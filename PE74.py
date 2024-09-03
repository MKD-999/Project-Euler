from time import time as t

'''
# Brute Force
def factorial(n: int) -> int:
    fact = 1
    while n > 1:
        fact *= n
        n -= 1

    return fact

ans = 0
strt = t()
for num in range(3, 1000000):
    
    cnt = 1
    l = [num]
    for i in l:

        if cnt > 60:
            break

        val = 0
        for j in str(i):
            val += factorial(int(j))

        if val not in l:
            l.append(val)
            cnt += 1

        else:
            break

    if cnt == 60:
        ans += 1

print(ans)
end = t()
print("------- %s seconds -------" % (end - strt))

'''


#  Manual from Brute force answer
def factorial(n: int) -> int:
    fact = 1
    while n > 1:
        fact *= n
        n -= 1

    return fact


strt = t()

fact_dict = {}
for i in range(10):
    fact_dict[i] = factorial(i)

num = 3
ans = []
while num < 10000:

    cnt = 1
    l = [num]
    for i in l:

        if cnt > 60:
            break

        val = 0
        for j in str(i):
            val += fact_dict[int(j)]

        if val not in l:
            l.append(val)
            cnt += 1

        else:
            break

    if cnt == 60:
        ans.append(num)
        break

    num += 1

num = 10000

while num < 100000:

    cnt = 1
    l = [num]
    for i in l:

        if cnt > 60:
            break

        val = 0
        for j in str(i):
            val += fact_dict[int(j)]

        if val not in l:
            l.append(val)
            cnt += 1

        else:
            break

    if cnt == 60:
        ans.append(num)
        break

    num += 1

num = 100000
while num < 1000000:

    cnt = 1
    l = [num]
    for i in l:

        if cnt > 60:
            break

        val = 0
        for j in str(i):
            val += fact_dict[int(j)]

        if val not in l:
            l.append(val)
            cnt += 1

        else:
            break

    if cnt == 60:
        ans.append(num)
        break

    num += 1

final = 0
chk = []
for i in ans:

    todivide = 0
    for j in str(i):
        if str(i).count(j) > 1 and j not in chk:
            chk.append(j)
            todivide += fact_dict[str(i).count(j)]

    if todivide != 0:
        final += fact_dict[len(str(i))] / todivide

    else:
        final += fact_dict[len(str(i))]

print(int(final + 3 * 3 * 2))  # 1479 but 1! == 0! so 4079 and permutations without 0 in first place also count
end = t()
print("------- %s seconds -------" % (end - strt))
