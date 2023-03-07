class Figure:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def sum_res(self):
        return f"Сумма: {self.__a + self.__b}"

    def pr_res(self):
        return f"Произведение: {self.__a * self.__b}"


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.__a = a
        self.__b = b

    def hypotenuse(self):
        return f"Гипотенуза: {(self.__a ** 2 + self.__b ** 2) ** 0.5}"

    def print_info(self):
        return f"Прямоугольный треугольгик: ({self.__a}, {self.__b}, {self.hypotenuse()})"

    def square_info(self):
        return f"Площадь: {self.__a * self.__b / 2}"


res = Figure(5, 8)
rect = Rectangle(5, 8)
print(rect.hypotenuse())
print(rect.print_info())
print(rect.square_info())
print()
print(res.sum_res())
print(res.pr_res())
print()


