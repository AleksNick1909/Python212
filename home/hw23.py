# 1 вариант

# class Account:
#     num = ""
#     surname = ""
#     percent = ""
#     value = ""
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def input_info(self, surname, num, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт")
#
#     def get_num(self):
#         return self.num
#
#     def set_num(self, num):
#         self.num = num
#
#     def get_surname(self):
#         return self.surname
#
#     def set_surname(self, surname):
#         self.surname = surname
#
#     def get_percent(self):
#         return self.percent
#
#     def set_percent(self, percent):
#         self.percent = percent
#
#     def get_value(self):
#         return self.value
#
#     def set_value(self, value):
#         self.percent = value
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account()
# acc.input_info(num='12345', surname='Долгих', percent=0.03, value=1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.set_surname("Дюма")
# acc.set_num('66666')
# acc.set_percent(0.1)
# acc.print_info()
# acc.add_percents()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)

# 2 вариант

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.num} принадлежащий {self.surname} был открыт")
        print("*" * 50)

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, new_num):
        self.__num = new_num

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, new_percent):
        self.__percent = new_percent

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
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

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


acc = Account(num='12345', surname='Долгих', percent=0.03, value=1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.surname = "Дюма"
acc.num = "66666"
acc.percent = 0.1
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

