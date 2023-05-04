from jinja2 import Template

data = [
    {'id': "/index", 'href': 'Главная'},
    {'id': "/news", 'href': 'Новости'},
    {'id': "/about", 'href': 'О компании'},
    {'id': "/shop", 'href': 'Магазин'},
    {'id': "/contacts", 'href': 'Контакты'},
]

link = """<ul>
{% for c in data -%}
{% if c.href == 'Главная' -%}
    <li><a href="{{ c ['id'] }}" class="active">{{ c ['href']}}</a></li>
{% else -%}
    <li><a href="{{ c ['id'] }}">{{ c ['href']}}</a></li>
{% endif -%}
{% endfor -%}
</ul>"""

tm = Template(link)
msg = tm.render(data=data)

print(msg)
