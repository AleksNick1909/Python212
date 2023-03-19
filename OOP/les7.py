# ДИСКРИПТОРЫ

class String:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def set(self, value):
        self.__value = value

    def get(self):
        return self.__value


class Person:
    def __init__(self, name, surname):
        self.name = String(name)
        self.surname = String(surname)

    # @property
    # def name(self):
    #     return self.__name
    #
    # @name.setter
    # def name(self, value):
    #     self.__name = value
    #
    # @property
    # def surname(self):
    #     return self.__surname
    #
    # @surname.setter
    # def surname(self, value):
    #     self.__surname = value


p = Person("Иван", "Петров")
p.name.set("Владимир")
print(p.name.get())
