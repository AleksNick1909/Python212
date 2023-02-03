# Задача 1

# s = "I am learning Python. hello, WORLD!"
# ind1 = s.find('h')
# ind2 = s.rfind('h')
# res = s[:ind1] + s[ind2 + 1:]
# print(res)

# Задача 2

s = "I am learning Python. hello, WORLD!"
ind1 = s.find('h')
ind2 = s.rfind('h')
res = s[:ind1] + s[ind2:ind1-1:-1] + s[ind2 + 1:]
print(res)

# Задача 3

# s = input("вводим значения: ")
# print(s)
# a = input("какое значение заменяем: ")
# print(a)
# b = input("на какое значение меняем: ")
# print(s.replace(a, b))

# Задача 4

# str1 = "Ежевику для ежат " \
#        "Принесли два ежа. " \
#        "Ежевику еле-еле " \
#        "Ежата возле ели съели"
# print(str1)
# str1 = str1.split(" ")
# i = 0
# for x in str1:
#     if x[0].lower() == "е":
#         i = i + 1
#
# print(i)
