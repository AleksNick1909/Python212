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

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open("text2.txt", "r")  # считали что было в документе
# read_f = f.readlines()
# print(read_f)
# for i in range(len(read_f)):
#     if read_f[i] == "изменить строку в списке;\n":
#         read_f[i] = "Hello World!\n"
# print(read_f)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_f)
# f.close()


# f = open("Text.txt", "r")
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# ****
# f = open("Text.txt", "r+")  # r+ записывает, перезаписывает
# print(f.write("I am learning Python!"))  # write записать новую строку
# print(f.seek(3))  # seek переставляем курсор на позицию
# print(f.write("-new string-"))  # перезаписали от курсора
# print(f.tell())  # показывает сколько символов мы записали
# f.close()


# **** контекстный менеджер
# with open("text3.txt", "w+") as f: # w+ для чтения и записи и если нет файла то создаст (as назвать файл)
#     print(f.write("0123456789\n123456789"))  # записывает только строковое значение
#
#
# with open("text3.txt", "r") as f:
#     for line in f:
#         print(line[:6])


# ****
# file_name = "res_1.txt"
# lst = [4.5, 2.8, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))  # map преобразует тип данных
#     print(lt)
#     return '\t'.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")

# **** в текстовом файле выше преобразовать обратно из строки в список
# numbers = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_string(l: list) -> str:
#     return '\t'.join(map(str, l))
#
#
# with open('res_1.txt', 'r+', encoding='utf-8') as file:
#     # text = get_string(numbers)
#     # file.write(text)
#     nums = file.read()
#     print(nums)
#     nums_list = list(map(float, nums.split('\t')))
#     print(nums_list)
#     print(len(nums))
#     print(sum(nums_list))


#  Написать функцию, которая вводит слово из файла, имеющее максимальную длину или несколько

# def longest_world(file):
#     with open(file, 'r', encoding="utf-8") as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# file_name = "res_1.txt"
# print(longest_world(file_name))

# ***
# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)

read_file = 'one.txt'
write_file = 'two.txt'
with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
    for line in fr:
        line = line.replace("Строка", "Линия - ")
        fw.write(line)
