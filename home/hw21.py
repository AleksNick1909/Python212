
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print("Длина прямоугольника:", self.length)
        print("Ширина прямоугольника:", self.width)

    def s(self):
        print("Площадь прямоугольника:", self.length * self.width)

    def p(self):
        print("Периметр прямоугольника:", 2 * (self.length + self.width))

    def d(self):
        print("Гипотенуза прямоугольника:", round((self.length ** 2 + self.width ** 2) ** 0.5, 2))

    def r(self):
        for x in range(self.length):
            for y in range(self.width):
                print("*", end='')
            print()


p1 = Rectangle(3, 9)
p1.s()
p1.p()
p1.d()
p1.r()

