# Задача 1

# a = ['red', 'green', 'blue']
# b = ['#FF0000', '#008000', '#0000FF']
# c = {k: v for k, v in zip(a, b)}
# print(c)

# Задача 2

# a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# b = {i: i ** 3 for i in a}
# print(b)

# Задача 3

# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# z = a | b | c
# print(z)

# Задача 4

# names = {
#     "emp1": {"name": "John", "salary": 7500},
#     "emp2": {"name": "Emma", "salary": 8000},
#     "emp3": {"name": "Brad", "salary": 6500},
# }
# print(names["emp3"])
# names["emp3"]["salary"] = 8500
# for x in names:
#     print(x)
#     for y in names[x]:
#         print("\t", y, ": ", names[x][y], sep="")

# Задача 5

students = {}
n = int(input("Количество студентов: "))
s = 0
for i in range(n):
    s_name = input(str(i+1) + "-й студент: ")
    point = int(input("Балл: "))
    students[s_name] = point
    s += point

sr_ball = round(s / n)
print("\nСредний балл:", sr_ball, "\nСтуденты с баллом выше среднего:")
for i in students:
    if students[i] > sr_ball:
        print(i)

# Задача 6

# a = dict(zip(['color', 'fruit', 'pet'], ['blue', 'apple', 'dog']))
# print(a)
