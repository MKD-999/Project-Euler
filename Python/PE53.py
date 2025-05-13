from math import factorial as fact

cnt = 0
for i in range(23,101):
    if i % 2 == 0:
        for j in range(2,(i//2)):
            combo = fact(i)//(fact(j)*fact(i-j))
            if combo > 1000000:
                cnt += 2
        cnt += 1
    else:
        for j in range(2,(i+1)//2):
            combo = fact(i) // (fact(j) * fact(i - j))
            if combo > 1000000:
                cnt += 2

print(cnt)
