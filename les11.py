# Lambda (анонимная функция)

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))
#
#
# def summa(x, y):
#     return x + y
#
#
# print(summa(1, 2))
# print(summa('a', 'b'))

# Задача создать лямбда выражение, которое находит сумму квадратов двух чисел
# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# *****

# s = lambda a = 1, b = 2, c = 3: a + b + c
#
# print(s())
# print(s(10, 20, 30))

# s = lambda *args: args
#
# print(s(1, 2, 3, 4))
# print(s(10, 20, 30))

# f = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for i in f:
#     print(i('abc_'))

# *****

# def inc(n):
#     return lambda x: x + n

# inc = (lambda n: lambda x: x + n)
#
#
# print(inc(42)(1))
# print(inc(42)(3))

# f = inc(42)
# print(f(1))
# print(f(3))

# ЗАДАЧА создать лямбда выражение для вычисления суммы трех чисел, с использованием вложенных лмбда выражений
# sum3 = (lambda x: lambda y: lambda z: x + y + z)
# print(sum3(2)(4)(6))

# ***** сортировка
# d = {'b': 15, 'a': 10, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)

# def func(i):
#     return i[1]
#
#
# d = {'b': 15, 'a': 10, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)

# ******
# задача: дан список игроков, при чем для каждого игрока указаны его имя, фамилия
# и игровой рейтинг. отсортировать список игроков по фамилии, а затем по рейтингу
# от лучшего к худшему (лямбда функия)
#
# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)


# ******

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[0](15, 5)  # обращаемся к конкретной лямбде
# print(b)

# *******

# a = {'one': lambda x: x - 1, 'two': lambda x: x + 3, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# ******

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[4]()

# *****
# print((lambda a, b: a if a > b else b)(15, 23)) большое значение

# **** создать лямбда выражение нахождения минимального згачения между тремя числами 9 8 5
# print((lambda a, b, c: a if a < b and a < c else b if b < c else c)(9, 8, 5))
# ******

# Функция map(func, iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [1, 8, 12, -5, -10]
#
# lst2 = list(map(mult, lst))
#
# print(lst2)
# второй вариант
# print(list(map(lambda t: t * 2, [1, 8, 12, -5, -10])))


# ****** с кортежем
# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# особенность map

# areas = [3.456789, 5.7873448, 7.90023443, 45.654378, 78.3429111]
# print(list(map(round, areas, range(1, 7))))
#
# print(round(3.674843, 2))  # второе значение показывает сколько символов после запятой

# ******

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: (x, y), st, num)))
# print(dict(map(lambda x, y: (x, y), st, num)))

# ***** найти поэлементно сцмму чисел двух списков
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))


# *****
# Функция filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# print(tuple(filter(lambda s: len(s) == 3, t)))

# ******
# b = [66, 90, 54, 34, 97, 51, 67, 19, 198, 329]
# res = list(filter(lambda s: s > 75, b))
# print(res)


# ***** сгенерировать список из десяти элементов случайным образом. из полученного
# списка чисел выбрать только те, которые находятся в диапазоне от 10 до 20 (включительно)

# import random
#
# lst = [random.randint(1, 30) for _ in range(10)]
# lst_new = list(filter(lambda x: 9 < x < 21, lst))
# print(lst)
# print('[10; 20] =', lst_new)

# ******

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))  # [1, 3, 5, 7, 9]
# print(m)
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)
