import re

# s1 = '192.168.255.255'  # 127.0.0.1
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'  # ?:
# print(re.findall(reg, s1))


# *****
# s1 = "Word2016, PS6, AI5"
# # reg = r'([A-z]+)(\d+)'  # буквы и цифры отдельно
# reg = r'(([A-z]+)(\d+))'
# # reg = r'([A-z]+)\d+'
# print(re.findall(reg, s1))
# print(re.findall(reg, s1)[0][1])

# *****
# s1 = "5 + 7*2 -4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s1))

# *****
# a = '28-08-2021'
# reg = r'(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(reg, a))
# print(re.search(reg, a))

# ******
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s)[0])
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m)
# print(m[0])  # 0 полностью весь шаблон
# print(m[1])  # 1 круглые скобки
# print(m[2])  # вторые круглые скобки

# ****
# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.findall(r'\s*(\w+)\s*', text))
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# *****
# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src=(['\"])(.+)\1>"
# print(re.findall(reg, s)[0][1])

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src=(?P<q>['\"])(.+)(?P=q)>"
# print(re.findall(reg, s)[0][1])

# (?P<name>) (?Pname)

# ****
# s = "Самолет прилетает 10/23/2023. Будем вас рады видеть после 10/24/2023"  # 24.10.2023
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))  # \2\1\3 номер скобок

# ***
# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9\-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))




