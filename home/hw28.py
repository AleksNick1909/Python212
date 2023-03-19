import math
from abc import ABC, abstractmethod


class Shape:
    def __init__(self, color):
        self.color = color

    def info(self):
        print("Цвет:", self.color)

    @abstractmethod
    def sq(self):
        print("Площадь:", end=" ")

    @abstractmethod
    def per(self):
        print("Периметр:", end=" ")


class Square(Shape, ABC):
    def __init__(self, a):
        self.a = a
        print("===Квадрат===")
        super().__init__(color="red")

    def info(self):
        print(f"Сторона: {self.a}")
        super().info()

    def pl(self):
        super().sq()
        print(self.a ** 2)

    def per(self):
        super().per()
        print(4 * self.a)


class Rectangle(Shape, ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("===Прямоугольник===")
        super().__init__(color="green")

    def info(self):
        print(f"Длина: {self.a} \nШирина: {self.b}")
        super().info()

    def pl(self):
        super().sq()
        print(self.a * self.b)

    def per(self):
        super().per()
        print(2 * (self.a + self.b))


class Triangle(Shape, ABC):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print("===Треугольник===")
        super().__init__(color="yellow")

    def info(self):
        print(f"Сторона 1: {self.a} \nСторона 2: {self.b} \nСторона 2: {self.c}")
        super().info()

    def pl(self):
        super().sq()
        per = (self.a + self.b + self.c) / 2
        print(math.sqrt(per * (per - self.a) * (per - self.b) * (per - self.c)))

    def per(self):
        super().per()
        print((self.a + self.b + self.c) / 2)


s = Square(3)
s.info(), s.pl(), s.pl(), s.per()
for i in range(s.a):
    for y in range(s.a):
        print("*", end="")
    print()
print()
r = Rectangle(3, 7)
r.info(), r.pl(), r.per()
for i in range(r.a):
    for y in range(r.b):
        print("*", end="")
    print()
print()
t = Triangle(11, 6, 6)
t.info(), t.pl(), t.per()
for x in range(t.c):
    print(" " * (t.c - 1 - x) + "*" * (1 + x * 2))

