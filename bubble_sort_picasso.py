import picasso
import numpy.random as r

def bubble_sort(a):
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                swapped = True
                a[i], a[i + 1] = a[i + 1], a[i]

    return a


p = picasso.Picasso('bubble_sort')

p.draw_best_fitting_line = True

for i in range(0, 15001, 1000):
    p.start(i)
    a = r.random_integers(0, i, i)
    bubble_sort(a)
    p.end()
    p.export()
