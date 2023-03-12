
# вытащить все слова с заглавной буквы
with open('text2.txt') as f:
    f = f.read().splitlines()
    for line in f:
        for word in line.split(' '):
            if word.istitle():
                print(word)