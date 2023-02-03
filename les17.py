# РЕКУРСИЯ - функция вызывает сама себя папка 18

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("->", n)
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))  # 5
# elevator(n1)

# ****

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25
#
#
# def sum_list(lst):  # [1, 3, 5, 7, 9]
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# *****

def to_str(n, base):  # 15
    convert = "0123456789ABCDEF"
    if n < base:
        return convert[n]  # [15] = 'F'
    else:
        return to_str(n // base, base) + convert[n % base]  # [15] = 'F'


print(to_str(255, 16))

print(int('FF', 16))
