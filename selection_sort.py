def selection_sort(a):
	for i in range (len(a)):
		minimum_index = i

		for j in range(i, len(a)):
			if a[j] < a[minimum_index]:
				minimum_index = j

		a[i], a[minimum_index] = a[minimum_index], a[i]

	return a
a = [12, 3, 5, -3, 20]
print selection_sort(a)