# работа с двумя словарями
# dict_one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# dict_two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, v1)
#     print(k2, v2)


# распаковка кортежа
# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # print(dict(pairs))
# a, b = zip(*pairs)
# print(a)
# print(b)


# letters = ['b', 'a', 'd', 'c']
# numbers = [3, 1, 2, 4]
# data = list(zip(letters, numbers))
# print(data)
# data.sort()
# print(data)
# data1 = list(zip(numbers, letters))
# data1.sort()
# print(data1)
# data2 = dict(data1)
# print(data2)
# data3 = sorted(data2.items())
# print(data3)


# ****
# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
#
# print({**two, **one})  # распаковка словаря
#
# for k, v in {**two, **one}.items():
#     print(k, "->", v)


# ********
# data = [2, 5, 3, 4, 1, 5]
# for i in data:
#     print(i, end=' ')
# print()
# for i in range(6):
#     print(i, end=' ')
# print()
# colors = ['red', 'green', 'blue']
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1

# второй способ
# colors = ['red', 'green', 'blue']
# for num, val, in enumerate(colors, 1):  # enumerate функция
#     print(num, ") ", val, sep="")

# со списком
# n = {i: i + 1 for i in range(10, 18)}  # создали словарь
# print(n)
#
# for i, (j, v) in enumerate(n.items(), 100):
#     print(i, ": ", j, " -> ", v, sep="")


# ******
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):  # произвольное количество аргументов
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(2, 3, 4, 5, 1))
# print(func(2, 4, 7))
# print(func())


# Задача: напишите функцию, которая принимает произвольное количество аргументов и
# возвращает словарь, в котором каждый элемент списка является и ключом и значением


# def to_dict(*lst):
#     return {i: i for i in lst}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# *****
#  Написать функцию, которая принимает произвольное число чисел, вычисляет
#  их среднее арифметическое и возвращает только те числа, которые меньше
#  полученного среднего арифметического

# def ch(*args):
#     res = []
#     sr = sum(args) / len(args)
#     print(sr)
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))

# ******

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))

# *****

# def print_scores(student, *scores):
#     print("Student Name:", student)
#     for score in scores:
#         print(score)
#
#
# print_scores("Джонатан", 100, 95, 88, 92, 99)
# print_scores("Роман", 96, 20, 33)

# *****

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func(d="python"))
# ****
# ЗАДАЧА

# def db(**data):
#     my_dict.update(data)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='gray')
# print(my_dict)


# ****

# def func(aa, *args, d=0, **kwargs):
#     return aa, args, d, kwargs
#
#
# print(func("one", 5, 9, 7, 8, 1, a=1, b=2, c=3, d=6))

