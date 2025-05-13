def primes(a):
    # b
    l = []
    for i in range(2,a):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            l.append(i)
    return l

def prime(a):

    if a > 0:
        for i in range(2,int(a**0.5)+1):
            if a % i == 0:
                return 'NP'
        else:
            return 'P'
    else:
        pass

max_cnt = 0
max_prod = 0
l = primes(1000)


for b in l:
    for a in range(-999,1000):

         n = 0
         cnt = 0
         eq = n**2 + a*n + b
         while prime(eq) == 'P':

             n += 1
             cnt += 1
             eq = n** 2 + a*n + b

         if cnt > max_cnt:
             max_cnt = cnt
             max_prod = a * b

print(max_cnt)
print(max_prod)




