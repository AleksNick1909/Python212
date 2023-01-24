# ОБЛАСТИ ВИДИМОСТИ папка 12

# name = "Tom"  # Глобальная переменная
# surname = None
#
#
# def hi():
#     global name, surname
#     name = "Sam"  # Локальная переменная
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bey", name, surname)
#
#
# print(name)
# hi()
# bye()
# print(name)

# *****
# i = 5
# arg = 5
#
#
# def func(arg):
#     print(arg)
#
#
# i = 6
# arg = 6
# func(arg)  # 6
# *****

#  ENCLOSED область видимости (две функции вложенные друг в друга с одним названием переменной)

# x = 7
#
#
# def add_five(a):
#     x = 2
#
#     def add_two():
#         return a + x
#
#     return add_two()
#
#
# print(add_five(3))

# Built-in(B) область видимости

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# *****
# min1 = [5, 7, 8, 9, 7]
# print(max(min1))
# a = [5, 6, 7, 8, 4]
# print(min(a))
# *****


# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func('World!')


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("a + b =", a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()

# *****

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal: ", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# z = x + t  # 25 + 35
# print(z)

# *****
# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()

# ******


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# *****
#  ЗАМЫКАНИЕ одна функция вызывает другую функцию

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add2(10))
#
# print(outer(7)(10))


def func1():
    a = 1
    b = 'line'
    c = [1, 2, 3]

    def func2():
        nonlocal a, b
        c.append(4)
        a = a + 1
        b = b + '1'
        return a, b, c

    return func2


func = func1()
print(func())

# *****
# Задача

# def func(city):
#     s = 0
#
#     def func1():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return func1
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func('Сочи')
# res2()
# res2()
#
# res1()


# *****

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
#
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# ******

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
