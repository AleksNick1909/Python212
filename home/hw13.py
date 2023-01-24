# Задача 1

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

# Задача 3

# s = '0123456789'
# s2 = s[:4] + s[5:]
# print(s2)

# Задача 4


def func(s, old, new):
    s2 = ""
    i = 0
    while i < len(s):
        if s[i] == old:
            s2 += new
        else:
            s2 += s[i]
        i += 1
    return s2


str1 = "012345363738494"
str2 = func(str1, "3", "")
print(str1)
print(str2)

# Задача 4


# def func(n):
#     print(bin(n))
#
#
# func(int(input("-> ")))
