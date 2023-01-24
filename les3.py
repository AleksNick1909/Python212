# тернарное выражение
# a, b = 10, 20
# minim = a if a < b else b  # ищем минимальное значение
# print(minim)

# a, b = 10, 30
# minim = "a == b" if a == b else "a > b" if a > b else "b > a"  #
# print(minim)

# Написать программу проверки деления на ноль с испол тернарного выражения
# a, b = 10, 5
# c = a / b if b != 0 else "На ноль делить нельзя"
# print(c)

# ТЕМА ИСКЛЮЧЕНИЯ (папка 3 исключения)
# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что то не так")

# если две ошибки
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Что то не так")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")

# еще способ
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или делить на ноль")
# else:
#     print("Все верно", n, "и", m)  # отработает тогда когда в блоке try не возникло исключений
# finally:
#     print("Конец программы")  # выполняется в любом случае


# ЗАДАЧА
# Наисать программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация,
# то есть соединение, строк. В остальных случаях введеные числа суммируются

# n = (input("Введите первое число "))
# m = (input("Введите второе число "))
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# РАБОТА С ЦИКЛАМИ
# цикл While

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1  # i = i + 1

# написать программу которая будет выводить только четные числа от 1 до 20
# i = 2
# while i < 21:
#     print(i)
#     i += 2

# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# ЗАДАЧА
# n = int(input("Укажите количество символов "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов "))
# while n > 0:
#     print("*", end="")
#     n -= 1


# ЗАДАЧА
#  написать программу, которая находит сумму всех целых нечетных чисел в
#  диапазоне указанном пользователем
# start = int(input('Start: '))
# end = int(input('End: '))
# i = start
# sum_ = 0
# while i <= end:
#     if i % 2:
#         sum_ += i
#     i += 1
# print('Summa:', sum_)


# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное число")


# i = 0
# while i < 10:
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while i < 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i, end=" ")
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break
# print("Цикл завершен")

# Написать программ поиска произведения последовательности положительных
# и отрицательных чисел, вводимых с клавиатуру, пока пользователь не введет 0
# mult = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     mult *= n
#
# print("Произведение:", mult)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# ЗАДАЧА
# kol = int(input("Введите количество чисел последовательности: "))
# i = 1
# ch = float(input("Введите число: "))
# min_ch = ch
# max_ch = ch
# sum_ch = ch
# while i < kol:
#     ch = float(input("Введите число: "))
#     sum_ch += ch
#     if ch < min_ch:
#         min_ch = ch
#     if ch > max_ch:
#         max_ch = ch
#     i += 1
#
# print("Количество чисел: ", kol)
# print("Минимальное число: ", min_ch)
# print("Максимальное число: ", max_ch)
# print("Среднее арифметическое число: ", sum_ch / kol)

# Внутренний цикл
# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# Таблица умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1
