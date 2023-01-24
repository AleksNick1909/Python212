# Задача 1
import random

# a = []
# [a.append(int(input("-> ")))for i in range(int(input("n = ")))]
# print(a)
# ch = int(input("Введите число: "))
# if ch in a:
#     print("Число присутствует в элементах списка")
# else:
#     print("Число отсутсвует в элементах списка")


# Задача 2

# import random as r
# a = [r.randint(1, 100) for i in range(20)]
# print(a)
# summa = sum(a)
# print(summa)


# Задача 3

# import random as r
# a = [r.randint(0, 100) for i in range(10)]
# print(a)
# a.sort(reverse=True)
# print(a)


# Задача 4

import random as r
n, m = 4, 3
a = [[r.randint(0, 4) for i in range(m)] for j in range(n)]
for h in a:
    for w in h:
        print(w, end="\t\t")
        # if w > 0:
        #
    print()
s = 1
for row in range(len(a)):
    for col in range(len(a[row])):
        if a[row][col] > 0:
            s *= a[row][col]
print(s)

# Задача 5

# n = int(input("Размерность матрицы: "))
# mas = []
# for i in range(n):
#     mas.append([])
#     for j in range(n):
#         mas[i].append(random.randint(1, 100))
# print(mas)
# for row in mas:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# m = 101
# lst = []
# for k in range(n):
#     if m > mas[k][k]:
#         lst.append(mas[k][k])
# print(lst, end="\t")
# print("\n", min(lst))
