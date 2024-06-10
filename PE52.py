def search(a):
        if set(str(a)) == set(str(a*2)):
            if set(str(a)) == set(str(a * 3)):
                if set(str(a)) == set(str(a * 4)):
                    if set(str(a)) == set(str(a * 5)):
                        if set(str(a)) == set(str(a * 6)):
                            return 'y'

        else:
            return 'n'
i = 1
chk = True
while chk:
    if search(i) == 'y':
        print(i)
        chk = False
    i += 1