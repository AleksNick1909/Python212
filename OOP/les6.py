# import math


# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)
# pt.length = 10
# print(pt.length)

# *****
# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt =", pt.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())

# *****


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20)
# pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)


# ФУНКТОРЫ

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
#
# c2 = Counter()
# c2()
# c2()
#
# c1()
# c1()

# *****

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)  # strip удаляет и слева и справа
#
#
# s1 = StripChars("?:!.; ")
# print(s1(" ?Hello World!; "))
#
#
# # использование функции
# def strip_chars(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)  # strip удаляет и слева и справа
#
#     return wrap
#
#
# s2 = strip_chars("?:!.; ")
# print(s2(" ?Hello World!; "))

# Декораторы на основе классов

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("*" * 20)
#         self.func()
#         print("*" * 20)
#
#
# @MyDecorator
# def func1():
#     print("func")
#
#
# func1()

# *****

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, x, y):
#         res = self.func(x, y)
#         star = "*" * 20
#         return f"{star}\n{res}\n{star}"
#
#
# @MyDecorator
# def func1(a, b):
#     return a * b
#
#
# @MyDecorator
# def func2(a, b):
#     return a / b
#
#
# print(func1(2, 5))
# print(func2(2, 5))


# Создать класс, который будет декоррировать функцию. Функция возвращает результат умножения
# двух чисел (а = 2, b = 3), а класс возводит их в квадрат

