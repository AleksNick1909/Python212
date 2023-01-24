# Модули math используется для вычислений

# import math
#
# num1 = math.ceil(3.2)  # округление в большую сторону до целочисленного значения
# num2 = math.floor(3.8)  # округление в меньшую сторону до целочисленного значения
# num3 = math.sqrt(2)  # корень квадратный
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)  # вывод числа ПИ

# from math import ceil
#
# num1 = ceil(3.2)
# print(num1)

# from math import pi
# # Пользователь вводит радиус окружности. Найти длину окружности
# r = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * pi * r, 2))


#  Работа с датой и временем

# картинка в папке 7
# time - возвращает текущее время, прошедшее с начала 1970 года в секунду
# import time


# second = time.time()
# print(second)
# a = 167788923
# local_time = time.ctime(a)  # возвращает местное время в строке или
# # время полученное из 5 секунд(можно в скобках передавать кол секунд)
# print(local_time)
# res = time.localtime()
# print(res)
# print(res.tm_mon, res.tm_year)  # значение года(можно вывести мес, день, время и тд)
#
# print(time.strftime("Today is %B %d %y"))  # strftime удобный метод вывода даты
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(a)))  # time.localtime указывает конкретнуу дату

# sleep - задержка запуска
# pause = 2
# print("Запуск программы")
# time.sleep(pause)
# print(pause, "сек.")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)

# start = time.monotonic()  # monotonic более точное значение показывает
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)


# import locale
# locale.setlocale(locale.LC_ALL, "ru")  # автомат перевод (в папке 7)
#
# print(time.strftime("Сегодня %B %d %Y"))

# ФУНКЦИИ

# def hello(name, age):
#     print("hello,", name, ". I am ", age, sep="")
#
#
# hello("Irina", 20)
# hello("Ivan", 26)

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', 'hello')
# get_sum(2.5, 4.3)

# Задача: функция вывода на экран линии из чередующихся символов заданной длины
# (функция, которая принимает три параметра, но не возвращает никакого значения

# def symbol(n, a, b):
#     [print(b, end='') if i % 2 else print(a, end='') for i in range(n)]
#     print()

# def symbol(n, a, b):
#     for i in range(n):
#         if i % 2:
#             print(b, end='')
#         else:
#             print(a, end='')
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def get_sum(a, b):
#     if a > b:
#         return True
#     else:
#         return False
#
#
# x = 15
# y = 7
# if get_sum(x, y):
#     print("Первое число больше")
# else:
#     print("Второе больше")


# Написать функцию, нахождения разности, если a>b или сумму, если a<b. a и b - вводяться с клавиатуры
# def razn(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# x, y = int(input("a = ")), int(input("b = "))
# print(razn(x, y))


# Задача: Вывести куб всех чисел от 1 до 10
# (функция которая принимает один параметр и возвращает значение)
# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# Задача: напишите функ change(lst), которая принимает список и меняет местоами его первый и
# последний элемент. В исходном списке минимум 2 элемента

# def change(lst):
#     # lst[-1], lst[0] = lst[0], lst[-1]  первый способ
#     n = lst.pop()
#     m = lst.pop(0)
#     lst.insert(0, n)
#     lst.append(m)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# ЗАДАЧА проверка надежности пароля

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль!!!")
# else:
#     print("Это не надежный пароль!!!")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# ЗАДАЧА
# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()
#
#
# set_param(10, s="+")
# set_param(5, "*")
# set_param(7)

# ЗАДАЧА
# def digits_sum(n, even=True):  # 9874023
#     s = 0
#     while n > 0:  # 987402
#         num = n % 10  # 3
#         if even and num % 2 == 0:
#             s += num  # 0
#         if not even and num % 2 != 0:
#             s += num
#         n //= 10  # 987402
#     return s
#
#
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
#
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# ----

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")


