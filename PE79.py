import array as arr
import re
from time import time as t

# Trial 1
strt = t()

codes = ('319 680 180 690 129 620 762 689 762 318 368 710 720 710 629 168 160 689 716 731 736 729 316 729 729 710 769 '
         '290 719 680 318 389 162 289 162 718 729 319 790 680 890 362 319 760 316 729 380 319 728 716')

codes = re.split(' ', codes)

password = []

for i in list(codes[0]):
    password.append(int(i))

password = arr.array('I', password)


def merge(password: arr.array, code2: list) -> arr.array:
    for i in code2:
        if i not in password:
            ind = code2.index(i)

            if ind >= len(code2) // 2:
                ind -= 1
                while code2[ind] not in password:
                    ind -= 1

                cont_ind = password.index(code2[ind])
                password.insert(cont_ind + 1, i)

            else:
                ind += 1
                while code2[ind] not in password:
                    ind += 1

                cont_ind = password.index(code2[ind])
                password.insert(cont_ind, i)

    return password


for code_ind in range(1, len(codes)):

    # Getting the codes and converting to int
    code2 = []

    for thing in codes[code_ind]:
        code2.append(int(thing))

    # Take common elements from password and code2
    # and adjust the indices

    # If there are no common elements, just skip this code2

    chk = set(password).isdisjoint(set(code2))

    if not chk:

        if len(set(password).intersection(set(code2))) == 1:
            password = merge(password, code2)

        else:

            order = []
            for i in password:
                if i in code2:
                    order.append(i)

            # Need to check if the numbers in password 
            # have the same order as the code2

            if order != code2:
                if len(order) == 2 and order == code2[:2]:
                    password = merge(password, code2)

                else:

                    # Changing the order of the nums in the password
                    rearranged = []
                    for i in code2:
                        if i in order:
                            rearranged.append(i)

                    indices = []
                    for i in password:
                        if i in rearranged:
                            indices.append(password.index(i))

                    ind = 0
                    for i in indices:
                        password[i] = rearranged[ind]
                        ind += 1

                    password = merge(password, code2)

    else:
        continue

ans = ''
for i in password:
    ans += str(i)

print(f'Your password is: {ans}')
end = t()
print('------- %s seconds -------' % (end - strt))
