import math


def s(a, b):
    return a * b


x, y = int(input("Введите сторону a: ")), int(input("Введите сторону b: "))
print("Площадь прямоугольника =", s(x, y))


def s(a, h):
    return (a * h) / 2


x, y = int(input("Введите сторону a: ")), int(input("Введите высоту h: "))
print("Площадь треугольника =", s(x, y))


def s(r):
    return math.pi*(r ** 2)


x = int(input("Введите радиус r: "))
print("Площадь круга =", s(x))
