# МНОЖЕСТВО (set)

# s = {"banana", "apple", "orange", "apple"}
# print(type(s))
# print(len(s))
# print(s)
# print(s[0])  # нельзя


# a = set('Hello')  # создать пустое множество
# print(type(a))
# print(a)


# s = {x * x for x in range(10)}
# print(s)


# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# # num = {i for i in numbers if i % 2 == 0}
# num = list(set(numbers))
# print(num)


# ****
# def to_set(s):
#     st = set(s)
#     return st, len(st)
#
#
# print(to_set("Я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))
# ****

# t = {'red', 'green', 'blue'}
# print('green' in t)  # 'not in' тоже работает


# pr = {2, 5, 3, 7, 11}
# for i in pr:
#     print(i, end=" ")


# *****
# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c'}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s}
# # a = {i for i in s if 'a' not in i}
# print(a)
# ****


#  папка 10
# a = {0, 1, 2, 3}
# a.add(4)  # добавление элементов
# print(a)
# a.remove(2)  # удаление элементов
# print(a)
# a.discard(3)  # удаление элементов, без генерации исключения
# print(a)
# a.pop()  # в скобках ничего не принимает, удаляет первый элемент,
# print(a)
# a.clear()  # очистка множества
# print(a)

# ***** папка 10
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# print(c)
# a |= b
# print(a)

# c = a & b  # выводит только одинаковые элементы
# print(c)
# a &= b
# print(a)

# c = a - b  # вывел уникальные элем которых нет в b
# print(c)
# a -= b
# print(a)

# c = a ^ b  # уникальное значение из первого и второго множества
# print(c)
# a ^= b
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a >= b
# print(c)


# ЗАДАЧА
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7  # выводили уникальные элементы
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print("Max =", max(s))
# print("Min =", min(s))

# ЗАДАЧА
# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")

# ЗАДАЧА найдите все буквы в первой строке, которые отсутвуют во второй
# str1 = "Python"
# str2 = "Programming language"
# s = set(str1) - set(str2)
# print(s)
# for i in s:
#     print(i, end=" ")


# ЗАДАЧА
# drawing = {"Марина", "Женя", "Света"}
# music = {"Женя", "Илья"}
#
# only_one_hobby = drawing ^ music
# print("Только одно хобби:", only_one_hobby)
#
# both_hobbies = drawing & music
# print("Два хобби:", both_hobbies)
#
# drawing = drawing - both_hobbies
# print(drawing)


# frozenset не изменяемый set
# s = frozenset({1, 2, 3, 4, 5})
# print(s)
# print(type(s))


# СЛОВАРЬ (dict)
# s = [1, 2]  # список
# d = {'one': 1, 'two': 2, 'ten': 10}
# print(s[0], s[1])
# print(d)

# d = {}  # первый способ создания словаря
# print(d)
# d = {"one": "один", "two": "два"}
# print(d)
# # print(type(d))
# # d["one"] = "один"
# # d["two"] = "два"
# # print(d)
# # d1 = dict()  # второй способ создания словаря
# # print(d1)
# d1 = dict(one="один", two="два")  # второй способ создания словаря
# print(d1)

# *** ключом может быть только не изменяемый тип данных
# d = {0: "text1", "one": 45, (1, 2.3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d)
# print(d["one"])  # обращаемся к конкретному ключу
# d["one"] = 100  # можно поменять значение ключа
# print(d)
# d[42][1] += 100  # добавили в ключе к значению ([1] - индекс в ключе) 100
# print(d)


# d = {a: a ** 2 for a in range(7)}
# print(d)


# d = [1, 2, 3]
# print(d)
# print(dict(d))  # нельзя


# преобразование списка в словарь
# users = [
#     ['igor@gmail.com', 'Igor'],
#     ['irina@gmail.com', 'Irina'],
#     ['anna@gmail.com', 'Anna']
# ]
#
# print(users)
# d_users = dict(users)
# print(d_users)
# print()
# преобразование кортежа в словарь
# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )

# print(user)
# d_user = dict(user)
# print(d_user)
#
# # print('irina@gmail.com' in d_user)  # проверка есть данный ключ
#
# for key in d_user:
#     print(key)  # выводим ключ
#     print(d_user[key])  # выводим значение ключа
#     print(key, "->", d_user[key])


# d = {'one': 1, 'two': 2, 'three': 3}
#
# del d['two']  # удаление из списка
# print(d)

# задача дан словарь с числовыми значениями. Необходимо их все перемножить
# и вывести на экран

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# mult = 1
# for key in d:
#     mult *= d[key]
#
# print(mult)


# задача
# 1 variant
# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# 2 variant
# d = {i: input("->") for i in range(1, 5)}
# print(d)
# dislike = int(input("Исключить: "))
# del d[dislike]
# print(d)


# ****
# d = {'one': 1, 'two': 2, 'three': 3}
# print(len(d))


# ЗАДАЧА

# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core i5-3450", 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         m = int(input("Количество: "))
#         goods[n][1] = m
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
# *******


# МЕТОДЫ СЛОВАРЕЙ
# d = {'one': 1, 'two': 2, 'three': 3}
# print(d["two"])
# value = d.get("two")  # получаем элем из словаря по заданному ключу, второй параметр возвращает значение
# # по умолчанию, если ключа нет
# print(value)
# print(d.keys())  # список ключей словаря
# print(d.items())  # список ключей и значений в виде кортежа
# print(d.values())  # список значений словаря
#
# for key, value in d.items():
#     print(key, value)
#
# d.clear()  # очистит словарь
# print(d)

# ****
# d = {'one': 1, 'two': 2, 'three': 3}
# d2 = d.copy()  # копия словаря
# print("D =", d)
# print("D2 =", d2)
#
# d["four"] = 4
# d2["five"] = 5
# print("D =", d)
# print("D2 =", d2)

# d = {'one': 1, 'two': 2, 'three': 3}

# item = d.pop('two')  # удаляет элем по ключу, возвращает удаленное значение (не ключ)
# item = d.setdefault("four", 4)  # добавляет ключ и значение в солварь, если ключа нет
# item = d.popitem()  # удаляет произвольную пару ключ и значение, возвращ удал знач в виде кортежа
# print(item)
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# # d.update({'four': 4, 'five': 5})
# d.update([('four', 4), ('five', 5)])  # добавляет и может изменять значения
# print(d)


# Задача: даны два словаря: х ={'a': 1, 'b': 2} и у = {'b': 3, 'c': 4}.
# Объединить их в третий словарь
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x.copy()
# z.update(y)
# z = x | y  # объединять словари в новый
# z = {i: d[i] for d in [x, y] for i in d}
# print(z)

# Задача дан словарь. создать новый, который будет содержать только имя и
# зарплату сотрудника, а затем удалить эти значения из исходного словаря

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# 1 var
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# # 2 var
# new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
# print(d)
# print(new_d)

# задача дан словарь, переименовать ключ city в location
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)

# ******
# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     },
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")
# *****
# Задача: создать след набор данных, предоставляющий объемы продаж по регионам, в виде
# двумерного словаря. Запросите у пользователя имя и регион. выводите соответсвующие данные.
# Запросите у пользователя имя и регион того значения который он хочет изменить
# и позвольте скорректировать объем продаж. выведите объм продаж по всем регионам для
# имени, выбранного пользователем.
# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# *****
# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# new_d = {v: k for k, v in d.items()}  # поменяли местами ключ и значения
# print(new_d)
# *****
# из исходного словаря выведите только два первых ключа и значения
# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# new_d = {k: v for k, v in d.items() if v <= 2}
# print(new_d)
# ***

# s = "Hello"
# d = {i: i * 3 for i in s}
# print(d)
# ***

# lt = [1, 2, 3, 4]
# value = input("-> ")  # одно значение будет в ключах
# d = {i: input("-> ") for i in lt}
# print(d)
# ***
# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# # value = list(d)
# # value = list(d.values())
# # value = list(d.keys())
# value = list(d.items())
# print(value)
# ***

# ЗАДАЧА Преобразовать список в словарь так, чтобы строковые значения были ключами, а
# числовые - значениями
# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# ****
# zip() функция преобразования
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(a, b)}
# print(f)

# d = list(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
# d = dict(zip('one', 'two'))
# print(d)

# a = [1, 2, 3]
# print(list(zip(a)))

# print(list(zip(range(5), range(95, 100))))

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# c = [4.0, 5.4, 6.7]
# print(list(zip(a, b, c)))
