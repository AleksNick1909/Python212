# ООП - (Объектно-ориентированное программирование)
# Свойства (переменные, поля)
# Методы (функции)
# Атрибуты (Свойства + Методы)

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

class Human:
    name = "name"
    birthday = "00.00.0000"
    phone = '00-00-00'
    country = "country"
    city = "city"
    address = "street, house"

    def print_info(self):
        print(" Персональные данные ".center(40, "*"))
        print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
              f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
              f"Город: {self.city}\nДомашний адрес: {self.address}")
        print("=" * 40)

    def input_info(self, first_name, birthday, phone, country, city, address):
        self.name = first_name
        self.birthday = birthday
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


h1 = Human()
h1.print_info()
h1.input_info("Юля", "23.05.1986", "45-45-45", "Россия", "Москва", "Чистопрудный бульвар, 1А")
h1.print_info()
h1.set_name("Анна")
print(h1.get_name())

# ******* папка 01, практика 01
