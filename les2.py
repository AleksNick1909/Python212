# функции преобразования типов данных

# num1 = "2"
# num2 = 3
# res = num1 + str(num2)
# print(res)
# res = int(num1) + num2
# print(res)
# num1 = "2.5"
# num2 = 3
# res = float(num1) + num2  #flot для преобразования типа с точкой
# print(res)
# bool преобразование булевых значений
# print(int(3.8))
# print(round(3.8))  # округление
#
# print(round(3.891, 2))  # второе число показывает сколько символов будет после точки

# a = 1
# b = 2
# print("a:", a)
# print()
# print("b:", b)
#
# print("a:", a, "\nb:", b)  # \n перенос строки

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="", end=" ")
# # sep показывает что будет на выводе вместо запятой
# # end=" " оставляем на одной строке end="\n" перенос на другую строку
# print("Я учу Python.")


# ввод данных input
# name = input("Введите имя: ")
# print("Hello", name)

# Пример
# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# Задача
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))
# # sum1 = num1 + num2
# # sum2 = num3 + num4
# # itog1 = sum1 / sum2
# # print(round(itog1, 2))
# print("Ответ:", round((num1 + num2)/(num3 + num4), 2))


# булевы значения
# b1 = True  # = 1
# b2 = False  # = 0
# print(b1 + 5)  # = 6
# print(b2 + 5)  # = 5

# print(bool("Python"))  # True
# print(bool(""))  # False
# print(bool(5))
# print(bool(0))
# print(bool(None))  # False
# # None используется когда мы не присваеваем значение в  переменную
# test = None
# print(test)

# операторы сравнения == != > < >= <=
# print(7 == 7)
# print(2 + 5 != 7)
# print("привет" > "Привет")

# print(2 < 4 < 9)  # True &&(и) True => True
# print(2 * 5 > 7 >= 4 + 3)  # True &&(и) True => True
# print(3 * 3 <= 7 >= 2)  # False &&(и) True => False

# Пример
# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# Логические операторы or (ИЛИ), and (И), not (нет)
# print(5 - 3 == 2 and 1 + 3 == 4)  # True
# print(5 - 3 == 2 and 1 + 3 < 4)  # False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True

# print(not 9 - 5)  # False
# print(not 5 - 5)  # True


# оператор if
# cnt = 5
# if cnt < 10:
#     cnt += 1
#     print(cnt)
#
# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ разрешен!")
# else:
#     print("Доступ запрещен!!!")

# a = 25
# b = 15
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("a == b")

# ЗАДАЧА
# a = int(input("Введите первую сторону: "))
# b = int(input("Введите второю сторону: "))
# c = int(input("Введите третью сторону: "))
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or c == b:
#     print("Это равнобедренный треугольник")
# else:
#     print("Это разносторонний треугольник")


# ЗАДАЧА
# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня не существует")


# ЗАДАЧА
# Напишите программу которая запрашивает у пользователя номер месяца
# и затем выводить название времени года. В случае если пользователь введет недопустимое
# число, программа должна вывести сообщение "Ошибка ввода данных"

# month = int(input("Введите номер месяца: "))
# if month == 1 or month == 2 or month == 12:
#     print("Зима")
# elif 3 <= month <= 5:
#     print("Весна")
# elif 6 <= month <= 8:
#     print("Лето")
# elif 9 <= month <= 11:
#     print("Осень")
# else:
#     print("Нет такого месяца")
#
# # второй вариант
# m = int(input("Введите месяц (цифрой): "))
# if 3 <= m <= 5:
#     print("Весна")
# elif 6 <= m <= 8:
#     print("Лето")
# elif 9 <= m <= 11:
#     print("Осень")
# else:
#     print("Зима")

# третий вариант

# ЗАДАЧА
# написать программу котроая предлагает пользователю ввести
# число ворон на верке в диапазоне от 0 до 9
# а затем вывести сообщение о количестве ворон определив при этом
# правильный падеж слова вороны

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     if 2 <= n <= 4:
#         print("вороны")
#     if 5 <= n <= 9 or n == 0:
#         print("ворон")
# else:
#     print("Ошибка ввода данных!!!")

# ЗАДАЧА
# Написать слово "КОПЕЕК" в правильном формате (диапазон от 1 до 99)
