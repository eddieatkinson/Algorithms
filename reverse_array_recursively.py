def rec_rev(a, i):
	if i == (len(a)/2):
		return a
	else:
		a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
		return rec_rev(a, i + 1)

a = [0, 1, 2, 3]
print rec_rev(a, 0)