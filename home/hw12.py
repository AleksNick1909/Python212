# def decor():
#     def su(fn):
#         def wrap(a, b, c, d):
#             print("Сумма чисел:", a + b + c + d)
#             fn(a, b, c, d)
#
#         return wrap
#     return su
#
#
# @decor()
# def sub(a, b, c, d):
#     print("Среднее арифметическое чисел:", (a + b + c + d) / 4)
#
#
# sub(2, 3, 3, 4)
#
# # *****
#
#
# def decor(args1):
#     def args_dec(fn):
#         def wrap(x, y, z, w):
#             print(args1, end=' ')
#             fn(x, y, z, w)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма чисел:")
# def summa(a, b, c, d):
#     print(a + b + c + d)
#
#
# @decor("Среднее арифметическое чисел:")
# def sub(a, b, c, d):
#     print((a + b + c + d) / 4)
#
#
# summa(2, 3, 3, 4)
# sub(2, 3, 3, 4)


# def decor(func):
#     def wrap(*args):
#         print("Среднее арифметическое чисел", str(args)[1:-1], "=", func(*args) / len(args))
#     return wrap
#
#
# @decor
# def summ(*args):
#     print("Сумма чисел", str(args)[1:-1], "=", sum(args))
#     return sum(args)
#
#
# summ(2, 3, 3, 4)
