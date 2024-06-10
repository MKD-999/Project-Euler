def leap(a):
    if a % 4 == 0 and a % 100 != 0:
        return 'L'
    elif a % 100 == 0 and a % 400 == 0:
        return 'L'
    else:
        return 'NL'

sun = 6
cnt = 0
for i in range(1901,2001):

    dupsun = sun
    a = leap(i)

    if dupsun == 1:
        cnt += 1

    if a == 'L':

        days = [31,29,31,30,31,30,31,31,30,31,30]
        for j in days:
            dupsun += 28
            dupsun -= j
            if dupsun < 0:
                dupsun += 7
            #print(dupsun)
            if dupsun == 1:
                cnt += 1
        #print()
        sun -= 2
        if sun <= 0:
            sun += 7

    else:

        days = [31,28,31,30,31,30,31,31,30,31,30]
        for j in days:
            dupsun += 28
            dupsun -= j
            if dupsun < 0:
                    dupsun += 7
            #print(dupsun)
            if dupsun == 1:
                cnt += 1
        #print()
        sun -= 1
        if sun <= 0:
            sun += 7

print(cnt)
