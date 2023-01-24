# Изменяемый и неизменяемый типы данных
# Изменяемый
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
#
# print(lt1 == lt2)
# print(lt1 is lt2)  # is по одинаковым ли адресам находятся переменные
#
# # неизменяемый
# a = True  # 'Hello', 3, 3.2, False
# b = True  # 'Hello', 3, 3.2, False
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)

# ----
# s = "Hello"
# print(s, id(s))
# s = s + "World"
# print(s, id(s))
#
# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))

# s = "Hello"
# print(s, id(s))
# # s[1] = "a"  # не можем изменить
# s = s[1:-1]  # срез
# print(s, id(s))


# def add_number(n):
#     print("Внутри функции:", n, id(n))
#     n += 1
#     print("Измененное значение:", n, id(n))
#     return n
#
#
# x = 1
# print("Внутри функции:", x, id(x))
# add_number(x)
# print("Измененное значение:", x, id(x))

# ----
# def add_number(n):
#     print("Внутри функции:", n, id(n))
#     n = n + [4]  # n += [4]
#     print("Измененное значение:", n, id(n))
#
#
# x = [1, 2, 3]
# print("Внутри функции:", x, id(x))
# add_number(x)
# print("Измененное значение:", x, id(x))

# КОРТЕЖИ (tuple) (Не изменяемый тип данных)

# lst = [10, 20, 30]  # списки
# tpl = (10, 20, 30)  # кортежи
# print(lst)
# print(tpl)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)  # есть смысл заполнять какими то данными
# print(type(a))
# b = tuple((1, 2, 3, 4, 5))  # стовить двойные скобки
# c = tuple("Hello")  # преобразует в кортеж
# print(type(b))

# d = 1, 2, 3, 4, 5
# e = tuple(d)
# print(d, type(d))
#
# t = (1,)  # кортеж с одним элементом
# print(type(t))

# d = 1, 2, 3, 4, 5
# print(d)
# print(d[3])
# print(d[1:3])  # срез

# s = [int(input("-> ")) for i in range(5)]  # список
# print(s)
# s = tuple(int(input("-> ")) for i in range(5))  # кортеж
# print(s)

# from random import randint

# s = [randint(1, 20) for i in range(6)]   # список
# print(tuple(s))  # можно с помощью tuple сразу же преобразовать список в кортеж
# либо вариант
# s = tuple(randint(1, 20) for i in range(6))  # кортеж
# print(tuple(s))

# Задача создать кортеж от 1 до 12 в квадрате
# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("Hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))  # количество букв l в кортеже
# print(t3.index('l'))  # возвращает индекс первого совпадения
# print(t3.index('l', 3))  # возвращает индекс совпадения

# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого значения нет")

# if 'w' in t3:
#     print(t3.index('w'))
# else:
#     print("Такого значения нет")
# for i in t3:
#     print(i * 2, end=" ")
# print("\n", t3)

# Задача: функция slicer() на вход принимает кортеж и случайный элемент.
# требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем
# и заканчивющийся вторым его появлением включительно. если элемента нет вовсе
# - вернуть пустой картеж. Если элемент втречается только 1 раз, то вернуть картеж,
# который начинается с него и идет до конца исходного.

# def slicer(tp1, el):
#     if el in tp1:
#         if tp1.count(el) > 1:
#             # return tp1[tp1.index(el):tp1.index(el, tp1.index(el) + 1) + 1]
#             start = tp1.index(el)
#             second = tp1.index(el, tp1.index(el) + 1)
#             return tp1[start:second + 1]
#         else:
#             return tp1[tp1.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# Задача: заполните один кортеж десятью случайными числами от 0 до 5 включительно.
# также заполните второй кортеж числами от -5 до 0.
# для заполнения кортежей числами напишите одну функцию.
# объедините два кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа count() определите в нем количество 0.
# Выведите на экран третий кортеж и количество нулей в нем.

# без функции
# from random import randint
# a = [randint(0, 5) for i in range(10)]
# print(tuple(a))
# b = [randint(-5, 0) for i in range(10)]
# print(tuple(b))
# c = a + b
# print(tuple(c))
# d = c.count(0)
# print(d)
# через функцию
# from random import randint
#
#
# def tuple_func(start, end):
#     return tuple(randint(start, end) for _ in range(10))
#
#
# tuple_1 = tuple_func(0, 5)
# tuple_2 = tuple_func(-5, 0)
# tuple_3 = tuple_1 + tuple_2
# count_0 = tuple_3.count(0)
# #
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print(count_0)

# *******

# t = (10, "hello", [1, 2, 3], (4, 5, 6), ["hello", "world"])
# print(t, id(t))
# t[-1][0] = 'new'
# print(t, id(t))
# # t[1][2] = 'a'  # не можем заменить не изменяемый тип данных
# # print(t, id(t))
# t[4].append('hi')  # добавили во вложенный список в кортеже
# print(t, id(t))


# ***
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# name1, age1, is_marreid1 = user
# # print(user[0])
# # print(user[1])
# # print(user[2])
# print(name1, age1, is_marreid1)
#
# name2, age2, is_marreid2 = get_user()
# print(name2, age2, is_marreid2)


# t = (1, 2, 3)
# # del t
#
# print(t)
# t = list(t)
# # print(list(t))
# print(t)
# t.append(4)
# print(t)
# t = tuple(t)
# print(t)


# СЛОЖНЫЕ КОРТЕЖИ

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "Население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "Население =", cityPopulation)

