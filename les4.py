
# for element in collection:
#   тело цикла

# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'yellow', 'green', 1, 20, 0.3:
#     print("color:", color)

# range(start, stop, step) начало, конец, шаг
# print(range(1, 3))

# for i in range(1, 10):  # последнее не отображается
#     print(i, end=" ")

# for i in range(10):  # последнее не отображается
#     print(i, end=" ")

# for i in range(1, 10, 2):  # шаг 2
#     print(i, end=" ")

# print()
# i = 1
# while i < 10:
#     print(i, end=" ")
#     i += 1

# for i in range(10, 1, -2):  # обратный порядок
#     print(i, end=" ")

# for i in range(100, 0, -10):  # обратный порядок
#     print(i, end=" ")

# ЗАДАЧА:
# a = int(input("Введите число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# ЗАДАЧА:
# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# print()
# for i in range(10, 100):  # 10 => 0 == 1
#     if i % 10 == i // 10:
#         print(i, end=" ")
#
# print()
# for i in range(1, 100):
#     if i % 11 == 0:
#         print(i, end=" ")


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

#  Вложенные
# for i in range(3):
#     print("***", i)
#     for j in range(2):
#         print("------", j)


# ЗАДАЧА:
# w = int(input("Введите длину: "))
# h = int(input("Введите высоту: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end=" ")
#     print()
# ЗАДАЧА:
# w = int(input("Введите длину: "))
# h = int(input("Введите высоту: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# letter = [i for i in "Hello"]
# print(letter)
# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# СПИСКИ ТЕМА
# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[-1])
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print("Длина списка: ", len(nums))

# s = []
# print(s)
# s1 = list()
# print(s)
# s2 = list("Hello")
# print(s2)

#
# s = [1, 3, 5]
# print(s)
# n = s * 6
# print(n)

# n = list(range(2, 10, 3))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# c = [i * 3 for i in "list"]
# print(c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)


# a = [0] * int(input("введите количество элементов: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)
# одна строка
a = [int(input("-> ")) for i in range(int(input("введите количество элементов: ")))]
print(a)

# a = [5, 6, 7, 3, 8]
# for i in range(len(a)):  # 0 1 2 3 4
#     print(a[i], end=" ")
# print()
# for i in a:
#     print(i, end=" ")


# ЗАДАЧКА
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print("сумма отриц элем: ", s)

# задача В списке на 20 элем поссчитать количество четных элем и найти сумму нечетных элем
# sp = [i for i in range(21, 41)]  # sp = list(range(21, 41)
# print(sp)
# ch = 0
# nech = 0
# for i in sp:
#     if i % 2 == 0:
#         ch += 1
#     else:
#         nech += i
# print("Количество четных элементов списка:", ch)
# print("Сумма нечетных элементов:", nech)

# задача найти среднее арифметическое всех ненулевых элем введенного числа
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# n = 0
# summa = 0
# for i in a:
#     summa += i
#     if i != 0:
#         n += 1
# print("Среднее арифметическое:", summa/n)
# дан список чисел. выведите все элементы списка, которые больше предыдущего
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

#  поменять местами
# a = [7, 8, 4, 6, 16]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)


#  СРЕЗЫ [star: stop: step]
# a = [7, 8, 4, 6, 16, 35]
# print(a[1:4])
# print(a[1:4:2])
# print(a[0:-1:1])
# print(a[0::1])
# print(a[::1])
# print(a[:])
# print(a[::-1])
# print(a[-2:2:-1])
# print(a[:-2])
# print(a[1:4:-1])
# print(a[10:20])

# Задача
# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[-3:])
# print(s[-3:1:-1])
# print(s[2:5])

# a = [7, 8, 4, 6, 16, 35]
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]  # если добавляем в срез то ставим []
# print(a)
# a[2] = 50  # если указываем индекс то без []
# print(a)

# del УДАЛЕНИЕ
# a = [7, 8, 4, 6, 16, 35]
# del a[2]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)

# МЕТОДЫ СПИСКА
# print(dir(list))

# s = [7, 8, 4, 6, 16, 35]
# print(s)
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 6])  # добавляет список элементов в конец первоначального списка
# print(s)
# s.extend('add')
# print(s)
# s.extend(['add', 'second'])
# print(s)
# s.insert(0, 100)  # добавляет в опеределенное место( 1 парамент это индекс, 2 это добавляемое значение
# print(s)


# [int(input("-> ")) for i in range(int(input("n: ")))]
# a = [1, 2, 3]
# n = int(input("n = "))
# for i in range(n):
#     # x = input("-> ")
#     # a.append(x)
#     a.append(int(input("-> ")))
# print(a)

# короткий способ
# [a.append(int(input("-> ")))for i in range(int(input("n = ")))]
# print(a)


#  ЗАДАЧА: Программа должна просить пользователя заданное количество раз ввести число
#  кратное 3, проверять, действительно ли оно кратно 3. Если да, то добавлять в список
#  если нет, то выводить пользователю на экране *введеное пользователем число не делится
#  на 3 без остатка.

# a = []
# n = int(input("Кол-во элементов списка: "))
# for i in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         a.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(a)


# a = [5, 9, 6, 2, 4, 1, 3, 2, 4]
# b = [4, 1, 7, 6, 2]
# c = []
# for i in a:
#     for j in b:
#         if i in c:  # чтобы повторно не выводилось в списке с
#             continue
#         if i == j:  # сравниваются все значения в списках (если равны то добавляет в список с)
#             c.append(i)
#             break
# print(c)

# Задача: Напишите функцию, которая создает комбинацию двух списков таким
# образом: [1, 2, 3] (+) [11, 22, 33] -> [1, 11, 2, 22, 3, 33]
# Результат [1, 11, 2, 22, 3, 33]

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# print("a =", a)
# print("b =", b)
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

#  если разный список
# a = [1, 2, 3]
# b = [11, 22, 33, 4, 3]
# c = []
# print("a =", a)
# print("b =", b)
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3, 5)
#     c.append(b[i])
# print(c)

# если первый список длиннее второго
# a = [1, 2, 3, 4, 3]
# b = [11, 22, 33]
# c = []
# print("a =", a)
# print("b =", b)
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3, 5)
#         c.append(a[i])
#
# print(c)