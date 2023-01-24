# методы списка

# a = [1, 2, 3, 4, 2, 3, 55, 99]
# print(a)
# a.remove(2)  # remove удаляет из списка указанный элемент по значению,
# # но если элементов несколько, то удалится только первый
# print(a)
# last = a.pop()  # pop удаляет последний элемент из списка и
# # возвращает удаляемое значение (усли скобки пустые)
# print(last)
# print(a)
# last = a.pop(-2)  # удаляет элемент с указанным индексом
# print(last)
# print(a)
# a.clear()  # быстрый способ очистить список
# print(a)


# Задача: Дан список из чисел и индекс элемента в списке К. Удалите из списка
# элемент с индексом К, сдвинув влево все элементы, стоящие правее элемента с инд К
# 1 вариант
a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: ")))]
k = int(input("Введите индекс: "))
a.pop(k)
print(a)
# 2 вариант

# a = []
# [a.append(input("->")) for i in range(int(input("n = ")))]
# print(a)
# while True:
#     if len(a) == 0:
#         break
#     k = int(input("Введите индекс: \nk = "))
#     a.pop(k)
#     print(a)

# отладчик
# a = [3, 5, 8, 4]
#
# s = 0
# for i in a:
#     s += i
#
# print(s)


# a = [3, 5, 8, 4, 5, 7, 5, 5]
# print(a)
# num = a.count(5)  # считает количество заданных значений в списке
# print(num)
# ind = a.index(5, 5, -1)  # возвращает индекс первого вхождения заданного значения (если значение не
# # найдено, то будет иключение ValueError)
# # 1-какое значение ищем,
# # 2- с какого по счету элемента ищем заданный индекс,
# # 3-до какого индекса
# print(ind)
#
# ch = 3  # проверяем есть ли 3 в списке
# if ch in a:
#     ind = a.index(ch)
#     print(ind)


# a = [3, 5, 8, 4]
# b = a
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)
# print(id(a))
# print(id(b))

# a = [3, 5, 8, 4]
# b = a.copy()  # создает копию списка
# print("a =", a)
# print("b =", b)
# b.append(120)
# print("a =", a)
# print("b =", b)
# print(id(a))
# print(id(b))

# a = [3, 5, 8, 4, 5, 7, 5, 5]
# print(a)
# a.reverse()  # обратный порядок списка
# print(a)
# a.sort()  # сортирует элементы списка по возрастанию
# print(a)
# a.sort(reverse=True)  # сортирует элементы списка по убыванию
# print(a)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# print(s)
# s.sort()  # по умолчанию по алфавиту
# print(s)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# print(s)
# s.sort(key=len)  # сортировка по количеству элементов по возрастанию
# print(s)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# print(s)
# s.sort(key=len, reverse=True)  # сортировка по количеству элементов по уюыванию
# print(s)

# a = [3, 5, 8, 4, 5, 7, 5, 5]
# print(a)
# a.reverse()  # обратный порядок списка
# print(a)
# a.sort()  # сортирует элементы списка по возрастанию
# print(a)
# a.sort(reverse=True)  # сортирует элементы списка по убыванию
# print(a)

# b = sorted(a, reverse=True)  # встроенная функция для сортировки и добавляет новый список
# print("b =", b)
# print("a =", a)


# ГЕНЕРАЦИЯ СЛУЧАЙНЫХ ДАННЫХ
# import должен находиться вверху документа
# 1 способ

# import random    # всегда прописывать random
#
# print(random.random())
# print(random.randint(1, 9))  # 9 включается в диапазон (1-9)
# print(random.randrange(9))  # 9 не включается в диапазон (0-9)
# print(random.randrange(0, 10, 2))

# 2 способ

# когда не нужно каждый раз прописывать random
# from random import randint, randrange
# print(randint(1, 9))
# print(randrange(9))

# 3 способ

# from random import *   # использует все модули, но при этом увеличивает память документа
#
# print(randint(1, 9))
# print(randrange(9))

# 4 способ

# import random as r
# #  as дали второе имя псевдоним, чтобы каждый раз не писать длинное имя
# print(r.randint(1, 9))
# print(r.randrange(9))


#  ЕЩЕ ВАРИАНТЫ ГЕНЕРАЦИИ

# import random as r
# print(r.randint(1, 9))
# print(r.randrange(9))
# print(r.uniform(10.5, 26.3))  # для генерации вещественного числа в заданном диапазоне

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))  # метод choice вызывает из списка случайное ОДНО значение
# print(r.choices(city, k=3))  # choices выводит случайные
# несколько значений (к - сколько именно будет выводить, могут одинаковые выводится)

# r.shuffle(city)  # метод shuffle случайно перемешивает список
# print(city)
# также работает и с числами


# import random as r
# mas = [r.randint(0, 10) for i in range(10)]  # r.randint(0, 10) диапазон случайных чисел в списке,
# # range(10) - количество этих элементов
# print(mas)


# ТЕМА: Поиск макс, мин, сум значений
# lst = [4, 6, 8, 9, 1]
# print(min(lst))  # готовая функция ищет минимальное значение
# print(max(lst))  # готовая функция ищет максимальное значение
# print(sum(lst))  # готовая функция ищет сумму значений


# Заполнить список из 10 элементов случайными числами.
# Найти максимальный элемент списка и переместить его в начало списка

# import random as r
# mas = [r.randint(1, 20) for i in range(10)]
# print(mas)
# b = max(mas)
# print(b)
# mas.remove(b)
# mas.insert(0, b)
# print(mas)

#  ЗАДАЧА: Заполнить список из 10 элементов случайными числами, как положительными,
#  так и отрицательными. Изменить этот список таким образом, чтобы все отрицательные элементы оказались в конце
import random as r

# a = [r.randint(-20, 20) for i in range(10)]
# print(a)
# a.sort(reverse=True)
# print(a)

# ЗАДАЧА: Заполнить список из 10 элементов случайными числами. Удалить
# все элементы, расположенные перед минимальным элементом списка.

# a = [r.randint(10, 100) for i in range(10)]
# print(a)
# lst = min(a)
# print("Min:", lst)
# index_min = a.index(lst)
# print("index min:", index_min)
# a = a[index_min:]
# print(a)


# x = list('1agj32kj')
# print(x)
# print('a' in x)
# print('a' not in x)

# lst = []
# if len(lst) == 0:
#     print("Пустой список")
#
# if not lst:
#     print("Пустой список")


# ЗАДАЧА
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [r.randint(0, 10) for _ in range(n1)]
# b = [r.randint(0, 10) for _ in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print("Третий список:", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы списка без повторения: ", c)
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)


# Матрицы - вложенные списки
# m = [
#     [1, 2, 3, 4],
#     [5, 3, 6],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
#  2 вариант
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

#  ЗАДАЧА: Возвести каждый элемент матрицы в квадрат

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()

# for row in m:
#     for x in row:
#         print(x ** 2, end="\t\t")
#     print()


# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)

# for h in matrix:
#     for w in h:
#         print(w, end="\t")
#     print()
# print()


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)


