def merge_and_sort(first_array, second_array):
	final_array = []
	while len(a) != 0 and len(b) != 0:
		if a[0] > b[0]:
			final_array.append(b[0])
			b.pop(0)
		elif a[0] <= b[0]:
			final_array.append(a[0])
			a.pop(0)
	if len(a) > 0:
		final_array += a
	else:
		final_array += b
	return final_array

a = [1, 3, 5, 7, 10, 11]
b = [2, 4, 6, 7, 10, 11, 12]

print merge_and_sort(a, b)