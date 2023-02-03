# продолжение работы со строками
import re

# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord('a'))  # ord показывает код
# print(ord('A'))

# случайный пароль генерация
# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())


# ******
# Строка не изменяемый тип данных

# print(dir(list))  # методы списка
# print(dir(str))  # методы строк

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # приводит первую букву в верх регистр, остальные в нижний
# print(s.lower())  # все символы переведены в нижний регистр
# print(s.upper())  # все символы переведены в верхний регистр
# print(s.swapcase())  # меняет регистр на противоположный
#
# print(s.count('h'))  # подчитывает количество вхождений подстроки в строки(количество заданных символов)
# print(s.count('h', 1))
# print(s.count('o'))
# print(s.lower().count('o', 0, -5))
#
# print(s.find("Python"))  # возвращает первый индекс кот соответсвует заданной подстроке
# # есди совпадений нет, то вернется значение -1
#
# print(s.find("Python", -3))
#
# print(s.index("Python"))  # возвращает первый индекс кот соответсвует заданной подстроке
# # есди совпадений нет, то возвращается ошибка


# ЗАДАЧА дана строка из двух слов, нужно переставить их местами.

# s = 'один два'
# ind = s.find(' ')
# s = s[ind + 1:] + ' ' + s[:ind]
# print(s)

# Задача

# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)


# *******

# s = "hello, WORLD! I am learning Python."
# print(s.rfind("l"))  # с правой стороны
# print(s.rindex("l"))
# print(s.find("l", 4))

# **** Задача

# a = "Nearly all web services collect this basic information from users in their server logs. " \
#     "However, Python Tutor does not collect any personally identifiable information from its users."
#
# n = 'f'
#
# if a.count(n) == 1:
#     print(a.find(n))
# elif a.count(n) >= 2:
#     print(a.find(n), a.rfind(n))

# ***** Задача Дана строка, в которой буква h встречается минимум два раза. Удалите из
# этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними

# s = "I am learning Python, hello, WORLD"
# ind1 = s.find('h')
# print(ind1)
# ind2 = s.rfind('h')
# print(ind2)
# res = s[:ind1] + s[ind2 + 1:]
# print(res)


# ******
# s = "hello, WORLD! I am learning Python."
# print(s.startswith("hello"))  # с чего начинается строка
# print(s.endswith("Python."))  # чем заканчивается строка

# *****

# print('abc123'.isalnum())  # состоит строка из букв и цифр
# print('abc?123'.isalnum())
# print(''.isalnum())
#
# print('abc'.isalpha())  # проверка только на буквы
# print('abc12'.isalpha())
#
# print('132'.isdigit())  # проверка только на цифры

# ******
#  метод для форматирования выравнивания

# print('py'.center(10, "-"))  # относительно 10 символов выровнялись элементы
# print('py'.center(1, "-"))
# print('py'.center(7, "="))

# ****

# print("    py".lstrip())  # удалит пробелы слевой стороны
# print("    py".rsplit())  # удалит пробелы справой стороны
# print("    py".strip())  # удалит пробелы и слева и справа
#
# print('https://www.python.org'.lstrip('/:pths'))
# print('py.$$$;'.rstrip(';$.'))
# print('https://www.python.orgw'.lstrip('/:pths').rstrip('.orgw'))

# **** метод replace

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python", 2))  # что меняем, на что меняем, количество элементов

# **** метод join объединяет список в строку

# s = "-"
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print("..".join(['1', '99']))  # используется только строковые значения
#
# print(":".join("Hello"))  # объединяет итерируемую последовательность в строку через символ разделитель

# ***** метод split обратный метод join

# print("Строка разделенными пробелами".split())
# print('www.python.org.ru'.split(".", 2))
# print('1,2,3'.split(","))
# print('www.python.org.ru'.rsplit(".", 2))  # справа

# *****
# a = input("-> ").split()
# print(a)  # список строковых значений
# a = list(map(int, a))  # это встроенная функция Python, позволяющая обрабатывать
# # и преобразовывать все элементы в итерируемом объекте без цикла for
# print(a)  # список числовых значений


# ***** В строке заменить пробелы символом *
# s = "В строке заменить пробелы звездочками"
# s = s.split()  # разбиваем на список текущих элементов
# print(s)
# s = "*".join(s)  # объединяем через *
# print(s)

# ***** пользователь вводит ФИО. приложение должно вывести фамилию и инициалы

# s = input('FIO: ').split()
# print(s)
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')


# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ

# + от одного и более
# * может быть может не быть

# import re
#
# # print(dir(re))
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# req = 'Я ищу'
# print(re.findall(req, s))  # возвращает список содержащий все совпадения с заданным шаблоном
#
# print(re.search(req, s))  # возвращает данные по соответствию первого совпадения с шаблоном
# # print(re.search(req, s).span())  # индекс совпадения
# # print(re.search(req, s).start())  # первый индекс
# # print(re.search(req, s).end())  # последний индекс
# # print(re.search(req, s).group())  # само совпадение
#
# print(re.match(req, s))  # возвращает данные по соответствию первого совпадения от начала строки


# *****
# import re
#
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# req = r'\.'
#
# print(re.split(req, s, 1))  # разбивали строку на список

# # поиск и замена

# print(re.sub(req, "!", s, 1))  # последнее значение это сколько замен сделать


# ******

# import re
#
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812"
# ...
# # req = r'[203]'  # [] - достаточно по одному символу (папка 17, комбинации)
# # req = r'[0-9]'  # диапазон
# # req = r'[0-9][0-9][0-9][0-9]'  # поиск всех 4 значных значений
# req = r'2[0-9][0-9][0-9]'  # поиск в первом значении
# print(re.findall(req, s))  # findall возвращает все совпадения

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812. [Hello]"
# req = r'[А-яё.\[\]]'  # папка 17  если выводить скобки то нужно экранировать \\
# print(re.findall(req, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812. [Hello]"
# req = r'[^0-9]'  # ^ символ отрицания ищем все кроме заданных значений
# print(re.findall(req, s))


# # ***** найти время в формате [16:25]
# import re
# s1 = "Час в 24-часовом формате от 00 до 23. 2021-0615Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09"
# r1 = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(r1, s1))


# ****
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812. [Hello]"
# req = r'\d'  # d поиск совпадения чисел
# req = r'\w'  # w любая буква, цифра, подчеркивание
# req = r'\s'  # s ищет совпадения с символом пробела
# req = r'\D'  # D поиск все кроме цифр
# req = r'\w'  # W все кроме
# req = r'\S'  # S ищет совпадения без символом пробела
# req = r'\AЯ ищу'  # \A ищет символы в начале строки
# req = r'\[Hello]\Z'  # \Z ищет символы в конце строки
# req = r'\bсов'  # \b ищет совпадение в начале или конце слова, в зависимости от расположения, \B отрицание

# квантификаторы папка 17
# req = r'\w+'
# req = r'\d+'  # все цифры
# req = r'20*'  # выводится заданная цифра
# print(re.findall(req, s))

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# print(re.findall(r'[+-]?[\d.]+', d))  # [\d.] ищет точку
# # ? от 0 до 1 количества повторения +- и тд
# * любое количество повторений

# метод sub
# d = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub('#.*', '', d))  # sub поиск и замена, что меняем, на что меняем и где
# print("Дата рождения:", re.sub('-', '.', re.sub('#.*', '', d)))


# ***** Написать регулярное выражение для нахождения всех ключей и значений

# d = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # r1 = r'\w+\s*=\s*\w+\s*[\w.]*'
# r1 = r'\w+\s*=[^;]+'
# print(re.findall(r1, d))

# ****
# s1 = "12 сентября 2023"
# # r1 = r"\d{4}"  # {} ищет заданное количество цифр подряд
# r1 = r"\d{2,4}"  # ищет от мин по макс количеству цифр
# print(re.findall(r1, s1))

# ***** найти номер телефона в формате +7хххххххх или 7ххххххххх

# s1 = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, +74994564578,"
# r1 = r"\+?7\d{10}"
# print(re.findall(r1, s1))


# ***** МЕТАСИМВОЛЫ
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 98_12."
# reg = r'^\w+\s\w+'  # ^ с начала строки
# reg = r'\w+\.$'  # с конца
# print(re.findall(reg, s))

# **** ФЛАГИ
# *** flags
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 98_12."
# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# **** DEBUG флаг
# text = "hello world"
# print(re.findall(r'\w\+', text, re.DEBUG))

# *** IGNORECASE
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 98_12."
# reg = 'я'
# print(re.findall(reg, s, re.I))

# **** MULTILINE
# text = """
# one
# two
# three
# """
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one$", text))
# # print(re.findall(r"one$", text, re.MULTILINE))
#
# # *** DOTALL перенос на другую строку
# print(re.findall(r"one.\w+", text, re.DOTALL))

# **** VERBOSE игнор переносы на другую строчку, пробелы и комментарии
# print(re.findall(r"""
# [\w -]+
# @
# [\w-]+
# """, "test@mail.ru", re.VERBOSE))

# флаг в регулярном выражении
# text = """Python,
# python
# PYTHON
# """
# reg = "(?im)^python"
# print(re.findall(reg, text))


# **** & $
# def validate_name(name):
#     return re.findall(r'^[\w-]{3,16}$', name)[0]
#     # return re.search(r'^[\w-]{3,16}$', name).group()
#
#
# print(validate_name('Python_master'))
# print(validate_name('Pyt'))

# **** найти адрес электронный почты

# s1 = "123456@.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# # reg = r'[\w.-]+@\w*\.?\w*\.?\w*'
# reg = r'[\w.-]+@[\w.-]+[\w]{2,3}'
# print(re.findall(reg, s1))

# ****
# text = "<body>Пример жадного соответсвия регулярного выражения</body>"
# print(re.findall('<.*>', text))  # жадное рег выраж, захватывается максимальное число символов
#
# text = "<body>Пример жадного соответсвия регулярного выражения</body>"
# print(re.findall('<.*?>', text))  # *?,+?,?? ленивые рег выражение, захватывает мин кол символов
# # {m,n}?, {,n}?, {m,}?
# s1 = "12 сентября 2023 года 568561"
# r1 = r"\d{3,}?"  # лишнее отбрасывает
# print(re.findall(r1, s1))

# *****
# t = "<p>Изображение <img alt='картинка src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img\s+[^>]*?src\s*=\s*[^>]+>'  # ^> ищет все в данный момент до символа >
# print(re.findall(reg, t)[0])


# *****
# t = "Петр, Ольга и Виталий отлично учатся"
# reg = "Петр|Ольга"  # | выбирает один из перечисленных элементов
# print(re.findall(reg, t))

# ****
t = "int = 4, float = 4.0, double = 8.0f"
# reg = r"\w+\s*=\s*\d+[\w.]*"
# reg = r"int\s*=\s*\d+[\w.]*|double\s*=\s*\d+[\w.]*"
reg = r"(?:int|double)\s*=\s*\d+[\w.]*"  # (?:  ) - скобки не сохраняющие (группирующие)
print(re.findall(reg, t))
