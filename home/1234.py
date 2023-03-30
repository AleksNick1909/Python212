import math


class Triangle:
    b = 90

    def __init__(self, a, ab, bc):
        self.a = a
        self.ab = ab
        self.bc = bc

    def __str__(self):
        return f"Угол A = {self.a} градусов\nУгол B = {self.b} градусов\nСторона AB = {self.ab}\nСторона BC = {self.bc}"

    def res_c(self):
        if 180 - self.a - self.b < 0:
            raise ValueError("Угол не может быть отрицательным")
        print("Угол С =", 180 - self.a - self.b, "градусов")

    def hypotenuse(self):
        print("Гипотенуза треугольника =", round(math.hypot(self.ab, self.bc), 2))


a1 = Triangle(20, 10, 20)
print(a1)
a1.res_c()
a1.hypotenuse()
