def merge_and_sort(a, b):
	final_array = []
	while len(a) != 0 and len(b) != 0:
		if abs(a[len(a) - 1]) > abs(b[0]):
			final_array.append(b[0] * b[0])
			b.pop(0)
		elif abs(a[len(a) - 1]) <= abs(b[0]):
			final_array.append(a[len(a) - 1] * a[len(a) - 1])
			a.pop(len(a) - 1)
	if len(a) > 0:
		final_array += a
	else:
		final_array += b
	return final_array

array = [-3, -2, 3, 4, 5, 6]

lowest_abs = array[0]
lowest_abs_index = 0
for i in range (len(array)):
	if abs(array[i]) < abs(lowest_abs):
		lowest_abs_index = i
	if array[i] > 0:
		break

low_half = array[:lowest_abs_index]
high_half = array[lowest_abs_index:]

sqr_low = []
sqr_high = []

# for j in range(len(low_half)):
# 	sqr_low[i] = low_half[i] * low_half[i]

