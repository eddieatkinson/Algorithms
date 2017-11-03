import numpy
import numpy.random as r

def merge_and_sort(a, b):
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

def merge_sort(a):
	if len(a) == 1:
		return a
	midpoint = len(a) / 2
	first_half = merge_sort(a[:midpoint])
	second_half = merge_sort(a[midpoint:])
	return merge_and_sort(first_half, second_half)


random_array = r.random_integers(0, 100, 10).tolist()
print random_array

sorted_array = merge_sort(random_array)
print sorted_array