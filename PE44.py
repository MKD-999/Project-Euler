def penta(n):

    if (1+(24*n+1)**0.5)%6 == 0:
        return True

    return False

i = 1
chk = True

while chk:
    for j in range(1,i):

        a = i*((3*i)-1)/2
        b = j*((3*j)-1)/2
        if penta(a-b) and penta(a+b):
            print(int(a-b))
            chk = False
            break
    i += 1



