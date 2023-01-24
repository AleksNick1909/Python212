# РАБОТА СО СТРОКАМИ папка 15 посмотреть

# print(int('18'))
#
# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 10))
# print(int('100', 16))
#
# print(bin(18))  # 0b10010 двоичная система счисления
# print(oct(18))  # 0o22 восьмиричная
# print(hex(18))  # 0x12 шестнадцатиричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12)


# таблица кодировки символов ASCII

# таблица символов ЮНИКОД папка 15


# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# # print(e * -3) # не будет выводить результат
#
# print(e in "i am learn Python")
# print(e[1:6])
# print(e[:])
# print(e[::-1])
# print(e[5:0:-1])
# print(e[5::-1])
# print(e[3])
# e = e[:3] + "t" + e[4:]
# print(e)

# *** Заменить символ в строке


# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 =changeCharToStr(str1, "N", "P")
# print(str1)
# print(str2)


# ********* ПРЕФИКСЫ
# print(u"Привет")

# print('C:\program\file.txt')
# print('C:\\program\\file')
# print(r'C:\program\file')  # префикс r
#
# print(r'C:\program\file' + "\\")
# print(r'C:\program\file\\'[:-1])

# префик b
# print(b'a1b2c3')
# print(b'a1b2c3'[1])  # перевод в 10 ю систему счисления
# print(b'\xff\xfe\xfd'[1])   # перевод в 10 ю систему счисления

# префикс f
# name = "Дмитрий"
# age = 35
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print("Меня зовут " + name + ". Мне", str(age), "лет.")
#
# print(f"Меня зовут {name}. Мне {age} лет.")

# from math import pi
#
# print(f"Значение числа pi: {round(pi, 2)}")
# print(f"Значение числа pi: {pi:.2f}")  # 2f кол символов после точки (float)

# ***
# x = 10
# y = 5
# print(f"{x = }\n{y = }")
# print(f"{x} x {y} / 2 = {x * y / 2}")

# a = 74
# print(f"{{{a}}}")


# *** префикс fr

# dir_name = "my doc"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)  # не удобно и большой код

# *** префикс br не используется

# ******* # многострочный текс (не комментарии), либо для документирования функции и классов

# s1 = """<div>
#     <a href = "#">content</a>
# </div>"""
# s2 = '''<div>
#     <a href = "#">content</a>
# </div>'''
# print(s1)
# print(s2)

# ***

# def square(n):
#     """Принимает число n, и возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(len.__doc__)

# import math as m


# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * m.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# ****

# print(ord('a'))  # ASKII
# print(ord('k'))
#
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# ****

# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# # mean = round(sum(arr) / len(arr))
# # arr.insert(0, mean)

# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифм:", arr)
# arr += [x for x in [ord(x) for x in (input("-> " + " ")[:6])] if x not in arr]
# print(arr)
#
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов:", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)


# ********

print(chr(101))  # Преобразует число в символ Юникода
print(chr(84))
print(chr(1085))

# *** Даны 2 числа a = 122, b = 97, где а и в коды символов. вывести все символы которые лежат
# между а и в включительно, в порядке возрастания их кодов

a = 122
b = 97

print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))
# 2 вар
q = [chr(x) for x in range(min(a, b), max(a, b) + 1)]
print(*q)
