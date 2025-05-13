l1 = []
l2 = []

i = 1000
while True:

    cube = sorted(list(str(i**3)))
    l1.append(cube)
    l2.append(i**3)

    if l1.count(cube) == 5:
        ind = l1.index(cube)
        print(l2[ind])
        break

    else:
        i += 1