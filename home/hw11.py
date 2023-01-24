# ЗАДАЧА 1

# def func_compute(n):
#     def inner(x):
#         return n * x
#
#     return inner
#
#
# res = func_compute(2)
# print(res(15))
# print(res(20))
#
# res = func_compute(3)
# print(res(15))
# print(res(20))

# ЗАДАЧА 2

# print((lambda x, y, z: x * y * z)(2, 5, 5))

# ЗАДАЧА 3

# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# res = sorted(students, key=lambda item: item['name'])
# print(res)
# res = sorted(students, key=lambda item: item['final'], reverse=True)
# print(res)

# ЗАДАЧА 4

# students = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
# res = max(students, key=lambda item: item['final'])
# print(res)
# res = min(students, key=lambda item: item['final'])
# print(res)
