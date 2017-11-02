def lin_search(array, num):
	for i in range (len(array)):
		if (num == array[i]):
			return i
	return -1

def binary_search(array_sorted, num):
	start = 0
	end = len(array_sorted) - 1

	while start < end:
		mid = (start + end)/2
		if array_sorted[mid] == num:
			return mid
		elif array_sorted[mid] > num:
			end = mid - 1
	
	return -1	

array = [1, 2, 5, 4, 3]
array_sorted = range(0, 10, 1)
num = 2

# print(lin_search(array, num))
print(binary_search(array_sorted, -1))