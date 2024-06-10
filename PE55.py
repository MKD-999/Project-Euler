def lychrel(a):

    i = 0
    a = str(a)
    while i < 51:

        rev = a[::-1]
        val = int(a) + int(rev)

        if len(str(val)) % 2 == 0:
            mid1 = len(rev)//2
            mid2 = mid1 + 1

            if str(val)[:mid1] == str(val)[-1:-mid2:-1]:
                return 'n'

        else:
            mid = int(len(str(val))/2 + 0.5)
            if str(val)[:mid-1] == str(val)[-1:mid-1:-1]:
                return 'n'

        i += 1
        a = str(val)

    else:
        return 'y'

cnt = 0
for i in range(1,10000):

    if lychrel(i) == 'y':
        cnt += 1

print(cnt)

