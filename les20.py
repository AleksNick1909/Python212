# МОДУЛЬ OS (OS.PATH)

import os

# print(os.getcwd())  # возвращает путь к текущуй директории
# print(os.listdir())  # список директорий, какие есть папки, файлы
# print(os.listdir(".."))  # выходим на уровень выше, /.. еще на уровень выше

# os.mkdir("folder")  # создали папку по указанному пути
# os.makedirs("nested1/nested2/nested3")  # создает несколько папок друг в дружке

# os.remove("xyz.txt")  # удаление файла

# os.rename("nested1", "test")  # переименовали папку, можно и файлы переименовывать

# os.rename("fgt.txt", "test/text333.txt")  # переместили и переименовали файл все директории должны существовать
# # os.renames() создаются промежуточные директории

# os.rmdir("folder")  # удаление пустой директории

# for root, dirs, files in os.walk("test", topdown=True):  # topdown=True обход папки сверху вниз, стоит по умолчанию,
#     # # topdown=False наоборот
#     print("Root:", root)
#     print("Sub_dirs:", dirs)
#     print("Files:", files)


# **** Удалить пустые директории в ветви Work

# def remove_empty_dir(root_tree):
#     print(f"Удаление пустых директорий в ветке {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 50)
#
#
# remove_empty_dir("test")

# *****

# МОДУЛЬ OS.PATH
import os.path
import time
# print(os.path.split(r'D:\Python\lessons\test\nested2\nested3\text3.txt'))  # разбивает путь на кортеж (head, tail)
# print(os.path.dirname(r'D:\Python\lessons\test\nested2\nested3\text3.txt'))  # имя директории
# print(os.path.basename(r'D:\Python\lessons\test\nested2\nested3\text3.txt'))  # имя файла

# print(os.path.join(r'D:\Python', 'lessons', 'test'))  # объединяет путь

# **** написать программу которая создаст дерево директорий и файлов
# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():  # items берем и ключи и значения
#     for f in file:
#         file_path = os.path.join(d, f)  # объединяем
#         # print(file_path)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12', r'Work\F2\f21\f211.txt', r'Work\F2\f21\f212.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fl in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(fl)
#     print('-' * 50)
#
# # print_tree('Work', topdown=False)
# print_tree('Work', True)

# **** метод exists

# print(os.path.exists(r'D:\Python\lessons\test\nested2\nested3\text3.txt'))  # возвращает True если файл
# существует, если нет то False

# getsize размер файла

# path = r'D:\Python\lessons\home\home.txt'
# k_size = os.path.getsize(path)  # размер файла
# print(k_size // 1024)
# print(os.path.getmtime(path))  # время последнего изменения файла
# print(os.path.getatime(path))  # время последнего доступа к файлу
# t = os.path.getctime(path)  # время создания сайта
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(t)))

# *** Задача
# file_parh = r'D:\Python\lessons\test\text333.txt'
# # exists проверка существует ли файл
# # split разбивает путь на кортежи
# if os.path.exists(file_parh):
#     dirs, name = os.path.split(file_parh)
#     atime = os.path.getmtime(file_parh)
#     print(f"{name} ({dirs}) - last access time {atime} sec")
# else:
#     print(f'File {file_parh} does not exist!')

# ****
# isfile, isdir модули

# file_parh = r'D:\Python\lessons\test\text333.txt'
# print(os.path.isfile(file_parh))  # возвращает True если указанный путь является файлом
# print(os.path.isdir(file_parh))  # возвращает True если указанный путь является папкой

# *** Напишите программу которая просканирует выбранную директорию и для всех ее
# объектов выведет следующую информацию на экран: имя - тип - размер (только для файлов)

# dir_name = r'D:\Python\lessons\test'
# obj = os.listdir(dir_name)
# print(obj)
#
# for i in obj:
#     p = os.path.join(dir_name, i)
#     # print(p)
#     if os.path.isfile(p):
#         print(f'{i} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{i} - dir')

# *****
