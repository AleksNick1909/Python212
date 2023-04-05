import json


class CountryCapital:
    @staticmethod
    def load(file_name):
        try:
            data = json.load(open(file_name))
        except FileNotFoundError:
            data = {}
        finally:
            return data

    @staticmethod
    def add_country(file_name):
        new_country = input("Введите название страны: ")
        new_capital = input("Введите название столицы: ")

        data1 = CountryCapital.load(file_name)

        data1[new_country] = new_capital

        with open(file_name, 'w') as f:
            json.dump(data1, f, indent=2)

    @staticmethod
    def delete_country(file_name):
        del_country = input("Введите названия страны: ")

        data1 = CountryCapital.load(file_name)

        if del_country in data1:
            del data1[del_country]

            with open(file_name, 'w') as f:
                json.dump(data1, f, indent=2)
        else:
            print("Такой страны в базе нет")

    @staticmethod
    def search_data(file_name):

        data1 = CountryCapital.load(file_name)

        country = input("Введите название страны: ")
        if country in data1:
            print(f"Страна {country}, столица {data1[country]} есть в словаре!")
        else:
            print(f"Страны {country} нет в словаре")

    @staticmethod
    def edit_data(file_name):
        country = input("Введите странц для корректировки: ")
        new_capital = input("Введите новое название столицы: ")

        data1 = CountryCapital.load(file_name)

        if country in data1:
            data1[country] = new_capital
            with open(file_name, 'w') as f:
                json.dump(data1, f, indent=2)
        else:
            print("Такой страны в базе нет")

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, 'r') as f:
            print(json.load(f))


file = "list_capital.json"
while True:
    index = input('Выбор дейтвия:\n1 - добавление данных\n2 - удаление данных\n'
                  '3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n'
                  '6 - завершение работы\nВвод: ')
    if index == "1":
        CountryCapital.add_country(file)
    elif index == "2":
        CountryCapital.delete_country(file)
    elif index == "3":
        CountryCapital.search_data(file)
    elif index == "4":
        CountryCapital.edit_data(file)
    elif index == "5":
        CountryCapital.load_from_file(file)
    elif index == "6":
        break
    else:
        print("Введен некорректный номер")