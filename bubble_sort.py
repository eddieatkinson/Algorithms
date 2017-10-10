array = [5, 3, 2, 4, 1]

def bubble_sort(a):
	swapped = True
	while(swapped):
		count = 0
		for i in range(0, len(array) - 1):
			if (array[i] > array[i + 1]):
				temp = array[i]
				array[i] = array[i + 1]
				array[i + 1] = temp
				count += 1
		if (count == 0):
			swapped = False
	return array


sorted_array = bubble_sort(array)
print sorted_array






