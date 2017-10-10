def sum_divisible_by(number, max):
	n = int((max - 1) / number)
	sum = number * (n * (n + 1) / 2)
	return sum

three = sum_divisible_by(3, 50000000)
five = sum_divisible_by(5, 50000000)
fifteen = sum_divisible_by(3 * 5, 50000000)

sum = three + five - fifteen
print sum