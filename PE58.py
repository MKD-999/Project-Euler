from time import time as t

def prime(a):
    
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return 'n'
    else:
        return 'y'

strt = t()
a = 1
add = 2
length = 1
nums = []

while True:

    for i in range(4):
        a += add
        if prime(a) == 'y':
            nums.append(a)

    add += 2
    length += 4

    if (len(nums)/length)*100 < 10:
        print((length+1)//2)
        break

end = t()
print(end-strt)









