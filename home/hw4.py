# Задача 1
a = []
[a.append(int(input("Введите элемент списка: "))) for i in range(int(input("Введите длину списка: ")))]
print("Список: ", a)
sp = []
for i in a:
    if i > 0:
        sp.append(i)
print("Новый список, состоящий из положительных элементов: ", sp)
maxim = 0
for i in sp:
    if i > maxim:
        maxim = i
print("Наибольший элемент списка: ", maxim)


# Задача 2
# a = []
# n = int(input("n = "))
# for i in range(n):
#     a.append(int(input("-> ")))
# print(a)
# k = int(input("Введите индекс: "))
# c = int(input("Введите значение: "))
# a.insert(k, c)
# print(a)

#  Задача 3
# a = list(range(1, 11))
# print(a)
# b = []
# for i in a:
#     x = i ** 2
#     b.append(x)
# print(b)
