# РАБОТА С ФАЙЛАМИ папка 19 режимы открытия файла 'r' - чтение, 'w' - запись

# f = open(r'D:\Python\lessons\Text.txt')
# print(f)
# print(*f)
# # Атрибуты файлового объекта
# print(f.mode)  #
# print(f.name)  # имя файла
# print(f.encoding)  # кодировка
# f.close()
# print(f.closed)  # проверка (False если открыт, True если закрыт)

# f = open('Text.txt', 'r')  # 'r' значение по умолчанию
# print(f.read(2))  # 2 (цифра в скобках) количество символов или индекс
# print(f.read())
# f.close()


#  ****
# f = open('test.txt', 'r')
# print(f.readline())  # считает только одну строку
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# ***
# f = open('test.txt', 'r')
# print(f.readlines(16))  # считает весь документ в строку
# print(f.readlines())
# f.close()

# ***
# f = open('test.txt', 'r')
# for line in f:
#     print(line)
#
# f.close()


# Задача: Определите количество строк в файле
# count = 0
# f = open('test.txt')
# for line in f:
#     count += 1
# print(count)
# f.close()
# #  второй способ
# fail = open('test.txt')
# count_lines = len(fail.readlines())
# print(count_lines)


# ***** перезапись w
# f = open('xyz.txt', 'w')
# f.write('Hello\nWorld')  # write режим записи
# f.close()

# ****** Режимы открытия файла
# f = open('xyz.txt', 'a')  # дозапись в конце
# f.write('Hello\nWorld')
# f.close()
# ****
# f = open('xyz.txt', 'a')
# lines = ['This is line 1', 'This is line 2']
# f.writelines(lines)
# for index in lines:
#     f.write(index + "\n")
# f.close()
# ****
# f = open('xyz.txt', 'w')
# lines = [str(i ** 5) for i in range(1, 20)]
# print(lines)
# for index in lines:
#     f.write(index + "\t")
# f.close()

# Задача Заменить строку в текстовом файле

f = open("text2.txt", "w")
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
f.close()

f = open("text2.txt", "r")  # считали что было в документе
read_f = f.readlines()
print(read_f)
for i in range(len(read_f)):
    if read_f[i] == "изменить строку в списке;\n":
        read_f[i] = "Hello World!\n"
print(read_f)
f.close()

f = open("text2.txt", "w")
f.writelines(read_f)
f.close()
