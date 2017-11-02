def lin_search(array, num):
	for i in range (len(array)):
		if (num == array[i]):
			return i
	return -1

array = [1, 2, 5, 4, 3]
num = 2

print(lin_search(array, num))