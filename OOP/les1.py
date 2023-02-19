# ООП - (Объектно-ориентированное программирование)
# Свойства (переменные, поля)
#     - статические
#     - динамические(изменяемые)
# Методы (функции)
# Атрибуты (Свойства + Методы)
# Специальные методы:
# * конструктор (__new__) для выделения памяти
# * Инициализатор (__init__) присвоение начального значения
# * Деструктор (__del__) удаление памяти после завершения программы

# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# print(dir(Point))
# print(Point.__doc__)


# class Point:
#     x = 1
#     y = 1  # 100
#
#
# p1 = Point()
# p1.x = 410
# p1.y = 200
# Point.y = 100
# print(p1.x, p1.y)
# print(p1.__dict__)  # возвращает словарь
# print(Point.__dict__)  #

# p2 = Point()
# print(p2.x, p2.y)
#
# print(id(Point))
# print(id(p1))
# print(id(p2))

# print(type(p1))
# print(isinstance(p1, Point))

# ***

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         # print(self.__dict__)
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
#
# p1.set_coord(5, 10)
# # Point.set_coord(p1)
# # print(p1.__dict__)
#
# p2 = Point()
# # p2.x = 20
# # p2.y = 30
# p2.set_coord(20, 30)
# # print(p2.__dict__)

# *********

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = '00-00-00'
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-45-45", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Анна")
# print(h1.get_name())

# ******* папка 01, практика 01
#  реализуйте класс "Автомобиль". Необходимо хранить в полях класса:
#  название модели, год выпуска, производителя, мощность двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных, вовода данных, реализуйте доступ
# к отдельным полям через методы класса.

# class Car:
#     model = None
#     year = None
#     pr = None
#     power = None
#     color = None
#     price = None
#
#     # Ввод данных
#     def input_info(self, model, year, pr, power, color, price):
#         self.model = model
#         self.year = year
#         self.pr = pr
#         self.power = power
#         self.color = color
#         self.price = price
#
#     # Вывод данных
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print("Название модели:", self.model)
#         print("Год выпуска:", self.year)
#         print("Производитель:", self.pr)
#         print("Мощность двигателя:", self.power)
#         print("Цвет машины:", self.color)
#         print("Цена:", self.price)
#         print("*" * 40)
#
#     def get_model(self):
#         return self.model
#
#     def set_model(self, value):
#         self.model = value
#
#
# BMW = Car()
# BMW.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
# BMW.print_info()
# BMW.set_model("Y7")
# print(BMW.get_model())

# ****
# Создать класс Person с данными о сотруднике (имя, фамилия) и двумя
# методами. Первый должен выводить данные о сотруднике, второй
# должен увеличивать уровень квалификации сотрудника на передоваемое
# количество единиц.

# class Person:
#     skill = 10
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):  #
#         self.name = name
#         self.surname = surname
#
#     def __del__(self):
#         print("Удаление экземпляра", "\n\n")
#
#     def print_info(self):
#         print("Данные о сотруднике:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника: {self.name}", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
# del p1
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)
# ******

# ******

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.count)
# p2 = Point(15, 20)
# print(p2.count)
# p3 = Point(23, 39)
# print(p3.count)
# print("count =", Point.count)

# *****
# Необходимо создать класс Robot. Каждый экземпляр робота нужно инициализировать.
# Робот должен поздороваться и представиться. При этом должен вестись
# подсчет роботов. По завершению работы роботов нужно выключить.

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация {self.name}")
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зову:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print()
# del droid1
# del droid2
# print("Численность роботов:", Robot.k)
