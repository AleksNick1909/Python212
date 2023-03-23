from geometry import tr, rect, sq
# import geometry.rect
# import geometry.sq
# import geometry.tr
# from geometry import *

r1 = rect.Rectangle(1, 2)
r2 = rect.Rectangle(3, 4)

s1 = sq.Square(10)
s2 = sq.Square(20)

t1 = tr.Triangle(1, 2, 3)
t2 = tr.Triangle(4, 5, 6)

shape = [r1, r2, s1, s2, t1, t2]

for g in shape:
    print(g.get_perimetr())
