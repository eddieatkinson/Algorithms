import picasso
import numpy.random as r

def insertion_sort(array):
	for i in range(len(array)):
		temp = array[i]
		j = i
		while j > 0 and array[j - 1] > temp:
			array[j] = array[j - 1]
			j -= 1
			
		array[j] = temp
	print array

insertion_sort([5, 3, 4, 1, 2])
