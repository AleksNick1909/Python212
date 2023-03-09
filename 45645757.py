import random


a = ['чтение', 'пение', 'рисование', 'математика']
b = ['литература', 'музыка', 'рисование', 'математика', 'Труд', 'ОБЖ', 'русс.яз',
     'география']
c = ['литература', 'музыка', 'математика', 'Труд', 'ОБЖ', 'русс.яз',
     'география', 'физкультура', 'химия', 'физика', 'черчение', 'англ.яз']
d = ['ПОНЕДЕЛЬНИК', 'ВТОРНИК', 'СРЕДА', 'ЧЕТВЕРГ', 'ПЯТНИЦА']
f = open("666.txt", "w", encoding='utf-8')
i = 0
while True:
    cl = int(input('введите номер класса\n'))
    if 1 <= cl <= 4:
        print('распиание на 5 дней:')
        for i in d:
            print(i, ':', end='\n')
            for j in range(3):
                print(random.choice(a), end='\n')
    elif 5 <= cl <= 8:
        print('распиание на 5 дней:')
        for i in d:
            print(i, ':', end='\n')
            for j in range(4):
                print(random.choice(b), end='\n')
    elif 9 <= cl <= 11:
        print('распиание на 5 дней:')
        for i in d:
            print(i, ':', end='\n')
            for j in range(5):
                print(random.choice(c), end='\n')
    else:
        print('Введен некорректный номер класса')

    f.write(i)
    f.close()
