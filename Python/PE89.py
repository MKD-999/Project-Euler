import re
from time import time as t


strt = t()

with open("0089_roman.txt", "r") as file:
	nums = re.split("\n", file.read())

key = {'I': 1,
	   'V': 5,
	   'X': 10,
	   'L': 50,
	   'C': 100,
	   'D': 500,
	   'M': 1000}

lock = dict()
for i in key:
	lock[key[i]] = i

l = [0] * len(nums)
ind = 0
for i in nums:
	val = 0
	for j in range(len(i)):
		if j + 1 < len(i):
			if key[i[j + 1]] > key[i[j]]:
				val -= key[i[j]]

			else:
				val += key[i[j]]

		else:
			val += key[i[j]]

	l[ind] = str(val)
	ind += 1

ans = []
for num in l:
	ones = int(num[-1])

	try:
		tens = int(num[-2]) * 10
	except IndexError:
		tens = 0

	try:
		hunds = int(num[-3]) * 100
	except IndexError:
		hunds = 0

	try:
		thous = int(num[-4])
	except IndexError:
		thous = 0

	# Ones
	if ones < 4:
		roman_ones = lock[1] * ones

	elif ones == 4:
		roman_ones = lock[1] + lock[5]

	elif ones <= 8:
		roman_ones = lock[5] + (ones - 5) * lock[1]

	else:
		roman_ones = lock[1] + lock[10]

	# Tens
	if tens < 40:
		roman_tens = lock[10] * (tens // 10)

	elif tens == 40:
		roman_tens = lock[10] + lock[50]

	elif tens <= 80:
		roman_tens = lock[50] + ((tens - 50) // 10) * lock[10]

	else:
		roman_tens = lock[10] + lock[100]

	# Hundreds
	if hunds < 400:
		roman_hunds = lock[100] * (hunds // 100)

	elif hunds == 400:
		roman_hunds = lock[100] + lock[500]

	elif hunds <= 800:
		roman_hunds = lock[500] + ((hunds - 500) // 100) * lock[100]

	else:
		roman_hunds = lock[100] + lock[1000]

	# Thousands
	roman_thous = lock[1000] * thous

	ans.append(roman_thous + roman_hunds + roman_tens + roman_ones)

final = 0
for i in range(len(ans)):
	final += abs(len(ans[i]) - len(nums[i]))

print(final)
end = t()
print('------- %s seconds -------' % (end - strt))
