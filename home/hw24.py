class Pair:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def sum_res(self):
        return f"Сумма: {self.width + self.height}"

    def pr_res(self):
        return f"Произведение: {self.width * self.height}"


class RightTriangle(Pair):
    def __init__(self, width, height):
        super().__init__(width, height)

    def show_rect(self):
        print(f"Прямоугольный треугольник: ({self.width}, {self.height}, {self.hypotenuse()})")

    def hypotenuse(self):
        return f"Гипотенуза: {(self.width ** 2 + self.height ** 2) ** 0.5}"

    def square_info(self):
        return f"Площадь: {self.width * self.height / 2}"


shape1 = RightTriangle(5, 8)
print(shape1.hypotenuse())
shape1.show_rect()
print(shape1.square_info())
print()
print(shape1.sum_res())
print(shape1.pr_res())
print()
shape2 = RightTriangle(10, 20)
shape2.show_rect()
print(shape2.hypotenuse())
print(shape2.sum_res())
print(shape2.pr_res())
print(shape2.square_info())
