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

# def to_str(n, base):  # 15
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # [15] = 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # [15] = 'F'
#
#
# print(to_str(255, 16))
#
# print(int('FF', 16))

# ****
# папка 18
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names[0])
# print(names[1])
# print(isinstance(names[0], str))  # isinstance проверяет тип данных
# print(isinstance(names[1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# print(len(names))
# print(names)


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))
# *****

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]

# def count_items(item_list):
#     count = 0
#     stack = []
#     current_list = item_list
#     i = 0
#     while True:
#         if i == len(current_list):
#             if current_list == item_list:
#                 return count
#             else:
#                 current_list, i = stack.pop()
#                 i += 1
#         if isinstance(current_list[i], list):
#             stack.append([current_list, i])
#             current_list = current_list[i]
#             i = 0
#         count += 1
#         i += 1
#
#
# print(count_items(names))

# *****
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
#
#
# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# print(union(names))

def remove(text):
    if not text:
        return ""
    if text[0] == "\t" or text[0] == " ":
        return remove(text[1:])
    else:
        return text[0] + remove(text[1:])


print(remove(" Hello\tWorld! "))
