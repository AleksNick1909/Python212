import re
# Задача 1
# password = "my-p@ss_w0rd"
# print(re.findall(r'[\dA-z@-]{6,18}', password))


def validate_name(name):
    return re.findall(r"^[a-z\d@_-]{6,18}$", name, re.IGNORECASE)


print(validate_name('my-p@ssw0rd'))

# Задача 2

# s = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков"
# reg = r"[\d/]{10}"
# print(re.findall(reg, s))
