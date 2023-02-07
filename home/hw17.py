# Задача 1

import re
s1 = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78,"
r1 = r"\+?7[\s*\d()-]+"
print(re.findall(r1, s1))

# Задача 2

# def otr_res(lst):
#     if not lst:
#         return 0
#     else:
#         count = otr_res(lst[1:])
#         if lst[0] < 0:
#             count += 1
#
#         return count
#
#
# print("n =", otr_res([-2, 3, 8, -11, -4, 6]))

