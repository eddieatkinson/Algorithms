import picasso

p = picasso.Picasso("my_example")
p.draw_best_fitting_line = True

for i in range(1000):
	p.add_point(i, i)
# p.add_point(0, 10)
# p.add_point(1, 20)
# p.add_point(2, 30)
# p.add_point(3, 40)
p.export()