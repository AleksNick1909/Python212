# Задача 1
from random import randint

# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# a = [randint(1, 100) for i in range(10)]
# print(a)
# n = int(input("Введите число: "))
# if seq_search(a, n):
#     print(f"Число {n} в списке присутсвует")
# else:
#     print(f"Число {n} в списке отсутствует")

# Задача 2

# f = open("home.txt", "w")
# f.write("Замена строки в текстовом файле; \nИзменить строку в списке; \nЗаписать список в файл;")
# f.close()
#
# pos = int(input('pos = '))
# f = open("home.txt")
# lst = f.readlines()
# print(lst)
# if (pos >= 0) and (pos < len(lst)):
#     i = pos
#     while i < len(lst) - 1:
#         lst[i] = lst[i + 1]
#         i = i + 1
#     lst = lst[:-1]
# f.close()
#
# f = open("home.txt", "w")
# for line in lst:
#     f.write(line)
#
# f.close()
# print(lst)

# Задача 3


def seq_search(s, item):
    pos = 0
    found = False
    while pos < len(s) and not found:
        if s[pos] == item:
            found = True
        else:
            pos += 1
    return found


a = [5, 9, 6, 7]
b = [3, 11, 8]
c = [2, 4]
d = [10, 1, 12]
f = a + b + c + d
print(f)
number = int(input("1 - сортировка по убыванию \n2 - сортировка по возрастанию \n-> "))
if number == 1:
    f.sort()
else:
    f.sort(reverse=True)
print(f)
n = int(input("Введите число: "))
if seq_search(f, n):
    print(f"Значение {n} найдено")
else:
    print(f"Значение {n} не найдено")
