def bubble_sort(a):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(a) - 1):
			if (a[i] > a[i + 1]):
				# temp = a[i]
				# a[i] = a[i + 1]
				# a[i + 1] = temp
				a[i], a[i + 1] = a[i + 1], a[i]
				swapped = True
	return a

array = [5, 3, 2, 4, 1]
sorted_array = bubble_sort(array)
print sorted_array






