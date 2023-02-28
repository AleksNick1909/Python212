from random import randint


def warrior(a, b, c):
    print("Ваш персонаж:", "\tИмя -", a, "\tКласс -", b, "\tРаса -", c)
    s = randint(1, 3)
    v = randint(1, 3)
    lov = randint(1, 3)
    h = randint(1, 3)
    intel = randint(1, 3)
    ud = randint(1, 3)

    res = s + v + lov + h + intel + ud
    print(res)
    while res != 30:
        if cl == "Маг":
            res += 1
            intel = intel + 1
            ud = ud + 1

        elif cl == "Лучник":
            res += 1
            lov = lov + 1
            h = h + 1
        elif cl == "Воин":
            res += 1
            s = s + 1
            v = v + 1

    print(" Сила\t", s, "\n", "Выносливость\t", v, "\n", "Ловкость\t", lov, "\n", "Харизма\t", h, "\n",
              "Интелект\t", intel, "\n", "Удача\t", ud)


cl = input("Выберите класс: Маг, Лучник, Воин\n")
name = input("Введите имя персонажа:\n")
rasa = input("Введите расу персонажа: Человек, Эльф или Орк\n")
warrior(name, cl, rasa)

