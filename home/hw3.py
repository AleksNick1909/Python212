# Задача 1

# s = int(input("Количество символов: "))
# t = input("Тип символа: ")
# lin = int(input("0 - горизонтальная линия \n1 - вертикальная линия\n"))
# if lin == 0:
#     print("Ориентация линии: ", lin)
# if lin == 1:
#     print("Ориентация линии: ", lin)
# i = 0
# while i < s:
#     if lin == 0:
#         print(t, end="")
#     if lin == 1:
#         print(t)
#     i += 1


# Задача 2

# a = input("Введите первое значение: ")
# b = input("Введите второе значение: ")
# c = input("Введите третье значение: ")
# maxim = a if b < a > c else b if a < b > c else c if a < c > b else b
# print("Максимальное значение: ", maxim)


# Задача 3

# q = 1
# while q <= 3:
#     s = 1
#     while s <= 9:
#         print("*", end=" ")
#         s += 1
#     print("")
#     w = 1
#     while w <= 9:
#         print("-", end=" ")
#         w += 1
#     q += 1
#     print("")


# Задача 4

# print("Выберите операцию: \n"
#       '1 - "r" - применяет унарный минус к операнду \n'
#       '2 - "+" - сложение \n'
#       '3 - "-" - вычитание \n'
#       '4 - "/" - деление \n'
#       '5 - "*" - умножение \n'
#       '7 - "%" - остаток от деления \n'
#       '8 - "<" - минимальное из двух чисел \n'
#       '9 - ">" - максимальное из двух чисел \n'
#       )
# while True:
#     op = input("Введите операцию: ")
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     if op == "r":
#         print(-1 * num1)
#         print(-1 * num2)
#     if op == "+":
#         print(num1 + num2)
#     elif op == "-":
#         print(num1 - num2)
#     elif op == "*":
#         print(num1 * num2)
#     elif op == "%":
#         print(num1 % num2)
#     elif op == "<":
#         res1 = num1 if num1 < num2 else num2
#         print(res1)
#     elif op == ">":
#         res2 = num2 if num1 < num2 else num1
#         print(res2)
#     try:
#         if op == "/":
#             print(num1 / num2)
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!!!")
