def find_minimum(a):
	minimum = a[0]
	for i in range (1, len(a)):
		if a[i] < minimum:
			minimum = a[i]
	return minimum
a = [12, 3, 5, -3, 20]
print find_minimum(a)