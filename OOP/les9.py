# Упаковка (сериализация) и распаковка данных (десериализация)
# Модули:
# marshal
# pickle
# json
# МЕТОДЫ:
# dump() - сохраняет данные в открытый файл
# load() - считывает данные из файла
# dumps() - сохраняет данные в строку
# loads() - считывает данные из строки

# import pickle

# file_name = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': "морковь",
#     "бюджет": 1000
# }
# with open(file_name, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, 'rb') as fh:
#     shop_list2 = pickle.load(fh)
# print(shop_list2)

# ****


# class Test:
#     num = 35
#     st = "привет"
#     lst = [1, 2, 3]
#     d = {'first': 'a', 'second': 2}
#     tpl = (22, 63)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСрока: {Test.st}\nСписок: {Test.lst}\nСловарь: {Test.d}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# my_obj2 = pickle.loads(my_obj)
# print(my_obj2)

# *****


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# ********
# import json

# data = {
#     'name': 'Olga',
#     'age': 35,
#     '20': None,
#     'True': 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'first_name': 'Alice',
#             'age': 6
#         }
#     ]
# }
#
# # with open('data.json', 'w') as fw:
# #     json.dump(data, fw, indent=4)
# #
# # with open('data.json', 'r') as fw:
# #     data1 = json.load(fw)
# # print(data1)
# # print(data1['name'])
#
# json_string = json.dumps(data, sort_keys=True)
# print(json_string)
#
# data2 = json.loads(json_string)
# print(data2)
# print(data2['name'])

# ****
# x = {
#     'name': 'Виктор'
# }
# y = {
#     'name': 'Виктор'
# }
#
# # a = json.dumps(x)
# # print(a)
# # print(json.loads(a))
# print(json.dumps(x))
# print(json.dumps(x, ensure_ascii=False))

# ****

# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#     # print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('person.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('person.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())

# ******
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ', '.join(map(str, self.marks))
#         return f"Студент: {self.name}: {a}"
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @staticmethod
#     def dump_to_json(stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': stud.name, 'marks': stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_from_file(filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.students:
#             a += str(i) + '\n'
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     def dump_group(self, file):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def upload_journal(file):
#         with open(file) as f:
#             print(json.load(f))
#
#
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# file1 = 'student.json'
# file2 = 'group.json'
# # Student.dump_to_json(st1, file1)
# # Student.dump_to_json(st2, file1)
# # Student.load_from_file(file1)
# # Student.load_from_file(file1)
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# my_group.dump_group(file2)
# # print(my_group)
# my_group.add_student(st3)
# # print(my_group)
# my_group.remove_student(1)
# # print(my_group)
# group22 = [st2]
# my_group2 = Group(group22, 'ГК Web')
# my_group.dump_group(file2)
# Group.upload_journal(file2)
# # print(my_group)
# # print(my_group2)
# Group.change_group(my_group, my_group2, 0)
# # print(my_group)
# # print(my_group2)
# # print(st1)
# # st1.add_marks(4)
# # print(st1)
# # st1.delete_mark(2)
# # print(st1)
# # st1.edit_mark(4, 5)
# # print(st1)
# # print(st1.average())
