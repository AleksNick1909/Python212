# Установка модулей
# pip instal requests

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # print(type(response.text))
# # print(response.text[:50])
# todos = json.loads(response.text)
# # print(todos)
# # print(type(todos))
#
# todos_by_user = {}
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
#
# max_users = " and ".join(users)
# print(max_users)
#
# s = "s" if len(users) > 1 else ""
# print(f"User{s} {max_users} completed {max_complete} TODOs")
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId'] in users)
#     return is_complete and has_max_count
#
#
# with open('filtered.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)


# ********
# CSV (Comma Separated Values)

# csv.reader() - чтение из файла []
# csv.DictReader() - чтение из файла {}
import csv

# with open('data1.csv') as f:
#     file_reader = csv.reader(f, delimiter=";")  # reader() - чтение из файла
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# ****

# with open('data1.csv') as f:
#     file_names = ['Имя', 'Профессия', 'Год рождения']   # это если нет заголовочной строки, в
#     # file_reader добавляем еще параметр fieldnames=file_names
#     file_reader = csv.DictReader(f, delimiter=";")   # работает по ключам
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году")
#         count += 1

# ****
# with open('student.csv', 'w') as f:
#     write = csv.writer(f, delimiter=';', lineterminator='\r')
#     write.writerow(['Имя', 'Класс', 'Возраст'])   # запись одного элемента списка
#     write.writerow(['Женя', '9', '15'])
#     write.writerow(['Саша', '5', '12'])
#     write.writerow(['Маша', '11', '18'])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     # for row in data:
#     #     writer.writerow(row)  # записывает один список
#     writer.writerows(data)   # записывает список списков
#
#
# with open('sw_data.csv', 'r') as f:
#     print(f.read())
#

# ****

# with open('stud_1.csv', 'w') as f:
#     name = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=name)
#     file_writer.writeheader()  # для заголовка
#     file_writer.writerow({"Имя": "Саша", "Возраст": "6"})   # передаем ключи и значения
#     file_writer.writerow({"Имя": "Маша", "Возраст": "15"})   # передаем
#     file_writer.writerow({"Имя": "Вова", "Возраст": "14"})   # передаем


# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_writer.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)
