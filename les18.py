# ПОИСК
# Линейный (последовательный)поиск


# def seq_search(s, item):
#     pos = 0  # 1
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
# print(seq_search(lst, 93))  # True
# print(seq_search(lst, 28))  # False

# **** 2 способ


# def seq_search(s, item):
#     pos = 0  # 1
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
# lst.sort()  # [17, 20, 26, 31, 44, 54, 55, 65, 77, 93] работать будет быстрее
# print(lst)
# print(seq_search(lst, 93))  # True
# print(seq_search(lst, 28))  # False

# **** Бинарный поиск работает только с отсортированным списком

# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
# print(binary_search(lst, 26))
# print(binary_search(lst, 28))


# Алгоритмы сортировки
# Пузырьковая сортировка (самый медленный)
from random import randint
import time
#
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [randint(1, 100) for i in range(10000)]
#
# start = time.monotonic()
# bubble(a)
# # print(a)
# res = time.monotonic() - start
# print(round(res, 3), "sec")  # 5.828 sec заняла сортировка списка

# *****
# Алгоритм сортировки СЛИЯНИЯ


# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     left = merge_sort(a[:n // 2])  # от начала до середины списка
#     right = merge_sort(a[n // 2:n])
#     # print(left)
#     # print(right)
#
#     i = j = 0
#     res = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     return res
#
#
# array = [randint(1, 100) for i in range(10000)]
# # print(array)
# start = time.monotonic()
# array = merge_sort(array)
# # print(array)
# res = time.monotonic() - start
# print(round(res, 3), "sec")


# ****
# Сортировка Шелла
# def shell_sort(s):
#     gap = len(a)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#     return s
#
#
# a = [randint(1, 100) for i in range(10000)]
# # print(a)
# start = time.monotonic()
# shell_sort(a)
# # print(a)
# res = time.monotonic() - start
# print(round(res, 3), "sec")

# ******

# Быстрая сортировка

# def quick_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1) // 2]  # среднее значение
#         low = [i for i in a if i < x]
#         eq = [i for i in a if i == x]
#         hi = [i for i in a if i > x]
#         a = quick_sort(low) + eq + quick_sort(hi)
#     return a
#
#
# lst = [randint(1, 100) for i in range(10000)]
# # print(lst)
# start = time.monotonic()
# lst = quick_sort(lst)
# # print(lst)
# res = time.monotonic() - start
# print(round(res, 3), "sec")

