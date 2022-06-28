from jinja2 import Template

# from markupsafe import escape


# data = """{% raw %} Модуль jijnja2 \
# вместо определения {{ name }} \
# подставляет соответствующее значение. {% endraw %}"""
#
# tm = Template(data)
# msg = tm.render(name="Fedor")

#
# link = """В HTML-документе ссылки определяюся так:
# <a href="#">Ссылка</a>"""
#
# tm = Template("{{ link |e }}")
# msg = tm.render(link=link)
#
# #Метод чтобы не писать громоздкую конструкцию.
# tm1 = escape(link)


# cities = [{'id': 1, "city": "Moscow"},
#           {'id': 3, "city": "Novosibirsk"},
#           {'id': 6, "city": "Kemerovo"},
#           {'id': 12, "city": "Krasnoyarsk"},
#           {'id': 17, "city": "Kerch"}]
#
# link = """<select name=cities>
# {% for i in cities -%}
#     <option value={{ i['id'] }}>{{ i['city'] }}</option>
# {% endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)


cities = [{'id': 1, "city": "Moscow"},
          {'id': 3, "city": "Novosibirsk"},
          {'id': 6, "city": "Kemerovo"},
          {'id': 12, "city": "Krasnoyarsk"},
          {'id': 17, "city": "Kerch"}]

link = """<select name='cities'>
{% for i in cities -%}
{%- if i['id'] > 6 -%}
    <option value='{{ i['id'] }}'>{{ i['city'] }}</option>
{% elif i['city'] == 'Moscow' -%}
    <option value='{{ i['id'] }}'>{{ i['city'] }}</option>
{% else -%}
    {{ i['city'] }}
{% endif -%}
{% endfor -%}
</select>"""

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
