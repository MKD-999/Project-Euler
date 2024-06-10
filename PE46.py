def primes(a):
    l = []
    for i in range(2,a+1):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            l.append(i)
    return l

tochk = True
i = 9

while tochk:

    a = primes(i)
    for j in a:
        if ((i-j)/2)**0.5 == int(((i-j)/2)**0.5):
            i += 2
            break
    else:        
        print(i)
        tochk = False



