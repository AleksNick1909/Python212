# Шаблонизатор Jinja
# pip install jinja2
# {{}} - выражение для вставки конструкции Phyton в шаблон (переменная)
# {% %} - спецификатор шаблона (for, if, else)
# { # # } - блок комментария
# ## - строчный комментарий

# from jinja2 import Template

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
# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Сочи'},
#     {'id': 3, 'city': 'Смоленск'},
#     {'id': 4, 'city': 'Минск'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
#
# link = """<select name="cities">
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value="{{ c['id'] }}">{{ c['city']}}</option>
# {% elif c.city == "Москва" %}
#     <option>{{ c['city'] }}</option>
# {% else -%}
#     {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# ***
# car = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44200},
#     {'model': 'Wolksvagen', 'price': 21300},
# ]
# lst = [1, 2, 3, 4, 5, 6]
# # tpl = "{{ cs | sum(attribute='price')}}"
# # tpl = "{{ (cs | max(attribute='price')).model }}"  # макс цена модель авто
# # tpl = "{{ (cs | max(attribute='price')).price }}"
# # tpl = "{{ cs | random }}"
# tpl = "{{ cs | replace('model', 'brand') }}"
# # tpl = "{{ cs | sum }}"
# tm = Template(tpl)
# msg = tm.render(cs=car)
# # msg = tm.render(cs=lst)
#
# print(msg)

# ****
# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.3},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.2},
# ]
#
# tpl = """
# {%- for u in users -%}
#     {% filter upper %}{{ u.name }}{% endfilter %}
# {% endfor -%}
# """
# tm = Template(tpl)
# msg = tm.render(users=persons)
# print(msg)

# *** Макроопределения

# html = """
# {%- macro text_input(name, value='', type='text', size=40) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro -%}
#
# <p>{{ text_input('username') }}</p>
# <p>{{ text_input('email') }}</p>
# <p>{{ text_input('password', type='password') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# ***

# html = """
# {%- macro text_input(name, placeholder, type='text') -%}
# <input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}">
# {%- endmacro -%}
#
# <p>{{ text_input('firstname', 'Имя') }}</p>
# <p>{{ text_input('lastname', 'Фамилия') }}</p>
# <p>{{ text_input('address', 'Адрес') }}</p>
# <p>{{ text_input('phone', 'Телефон', 'tel') }}</p>
# <p>{{ text_input('email', 'Почта', 'email') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)


# *** вложенный список через макроопределения

# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.3},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.2},
# ]
# html = """
# {%- macro list_users(list_user) -%}
# <ul>
# {%- for u in list_user %}
#     <li>{{ u.name }} {{ caller(u) }} </li>
# {%- endfor %}
# </ul>
# {%- endmacro -%}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>age: {{ user.year }}</li>
#         <li>weight: {{ user.weight }}</li>
#     </ul>
# {% endcall %}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
#
# print(msg)


# *****
from jinja2 import Environment, FileSystemLoader


# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.3},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.2},
# ]

subs = ['Культура', 'Наука', 'Политика', 'Спорт']

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(list_table=subs)

print(msg)
