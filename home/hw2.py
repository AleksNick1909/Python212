k = int(input("Введите количество копеек: "))
if 1 <= k <= 99:
    print(k, end=" ")
    if k % 10 == 1 and k != 11:
        print("копейка")
    elif 2 <= k % 10 <= 4:
        print("копейки")
    else:
        print("копеек")
else:
    print("Вы ввели неверное количество!")
