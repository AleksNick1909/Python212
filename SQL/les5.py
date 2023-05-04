# Шаблонизатор Jinja
# pip install jinja2
# {{}} - выражение для вставки конструкции Phyton в шаблон (переменная)
# {% %} - спецификатор шаблона (for, if, else)
# { # # } - блок комментария
# ## - строчный комментарий

from jinja2 import Template

# name = "Игорь"
# age = 25
# per = {'name': 'Игорь', 'age': 25}


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 25)
#
# tm = Template("Мне {{ p.get_age() }} лет. Меня зовут {{ p.get_name() }}")
# # tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p.name }}")
# # tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p['name'] }}")
# msg = tm.render(p=per)
#
# print(msg)

# ***
cities = [
    {'id': 1, 'city': 'Москва'},
    {'id': 2, 'city': 'Сочи'},
    {'id': 3, 'city': 'Смоленск'},
    {'id': 4, 'city': 'Минск'},
    {'id': 5, 'city': 'Ярославль'},
]

link = """<select name="cities">
{% for c in cities -%}
{% if c.id > 3 -%}
    <option value="{{ c['id'] }}">{{ c['city']}}</option>
{% elif c.city == "Москва" %}
    <option>{{ c['city'] }}</option>
{% else -%}
    {{ c['city'] }}
{% endif -%}
{% endfor -%}
</select>"""

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)

# ***
# car = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44200},
#     {'model': 'Wolksvagen', 'price': 21300},
# ]
# lst = [1, 2, 3, 4, 5, 6]
# # tpl = "{{ cs | sum(attribute='price')}}"
# tpl = "{{ cs | sum }}"
# tm = Template(tpl)
# # msg = tm.render(cs=car)
# msg = tm.render(cs=lst)
#
# print(msg)

