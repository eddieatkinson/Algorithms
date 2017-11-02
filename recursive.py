def factorial(number):
	if number == 0:
		return 1
	else:
		result = number * factorial(number - 1)
		return result

print factorial(5)


# def count_down(number):
# 	if number == -1:
# 		return
# 	else:
# 		print number
# 		count_down(number - 1)

# count_down(10)

# def add(array, current_index, sum):
# 	sum += array[current_index]

# 	if current_index == len(array) - 1:
# 		return sum
# 	else:
# 		return add(array, current_index + 1, sum)




# a = [10, 15, 12, 13]

# print add(a, 0, 0)