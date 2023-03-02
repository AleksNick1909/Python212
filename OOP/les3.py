# Методы класса

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, data_as_string):
#         day, month, year = map(int, data_as_string.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(data_as_string):
#         if data_as_string.count(".") == 2:
#             day, month, year = map(int, data_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '89.12.2021',
#     '12.31.2022'
# ]
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print("Неправильная дата")
#
# # string_date = "23.10.2021"
# # # print(string_date.split(".")) # split разбили список
# # day, month, year = map(int, string_date.split("."))
# # print(type(day), month, year)
# # date = Date.from_string("23.10.2021")
# # print(date.string_to_db())
#
# # string_date2 = "15.06.2021"
# # # print(string_date.split(".")) # split разбили список
# # day, month, year = map(int, string_date2.split("."))
# # date2 = Date.from_string("15.11.2021")
# # print(date2.string_to_db())

# **** ООП2 карт 1_1, 1_2

class Account:
    rate_usd = 0.013  # статические свойства
    rate_eur = 0.011  # статические свойства
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, percent, value=0):  # динамические свойства
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"Счет #{self.num} принадлежащий {self.surname} был открыт")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт")

    @staticmethod  # Статический метод
    def convert(value, rate):
        return value * rate

    @classmethod  # класс метод
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod  # класс метод
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def add_percents(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято!")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def edit_owner(self, surname):  # обычный метод смены владельца
        self.surname = surname

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


acc = Account(num='12345', surname='Долгих', percent=0.03, value=1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.edit_owner("Дюма")
acc.print_info()
acc.add_percents()
print()
acc.withdraw_money(100)
print()
acc.withdraw_money(3000)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)

# ****************************8
# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)  # запускаем проверку
#         # self.verify_old(old)  # запускаем проверку
#         # self.verify_weight(weight)  # запускаем проверку
#         # self.verify_ps(ps)  # запускаем проверку
#
#         self.fio = fio
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО длжно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#
#         letters = "".join(re.findall(r'[а-яё-]', fio, re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             print(s.strip(letters))  # strip удаляет пробелы если ничего не указать в ()
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 18 or old > 90:
#             raise TypeError("Возраст должен быть числом в диапазоне от 18 до 90 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числов и выше 20 кг")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():  # isdigit возвращает True если все символы являются числами
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)  # запускаем проверку
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)  # запускаем проверку
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)  # запускаем проверку
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)  # запускаем проверку
#         self.__weight = w
#
#
# p1 = UserDate("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# p1.old = 31
# p1.password = "6666 666666"
# p1.weight = 24.5
# print(p1.__dict__)
