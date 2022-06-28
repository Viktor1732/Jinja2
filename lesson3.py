from jinja2 import Template

# cars = [
#     {'model': "Ауди", 'price': 45700},
#     {'model': "Форд", 'price': 27000},
#     {'model': "Бетнли", 'price': 89700},
#     {'model': "Феррари", 'price': 254000},
#     {'model': "Жигули", 'price': 13800},
# ]
#
# tpl = "Суммарна цена всех автомобилей: {{ cars| random }}"
# tm = Template(tpl)
# msg = tm.render(cars=cars)


# person = [
#     {'name': "alex", 'old': 43, 'weight': 69},
#     {'name': "boris", 'old': 34, 'weight': 108},
#     {'name': "kelly", 'old': 62, 'weight': 57},
#     {'name': "john", 'old': 37, 'weight': 98}
#     ]
#
# tpl = """{% for i in users -%}
# {% filter capitalize %}{{ i.name }}{% endfilter %}
# {% endfor %}"""
#
# tm = Template(tpl)
# msg = tm.render(users=person)

#
# html = """{% macro input(name, value="", type="text", size="30") -%}
#     <input name="{{ name }}" value="{{ value }}" type="{{ type }}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input("login") }}</p>
# <p>{{ input("password") }}</p>
# <p>{{ input("age") }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()


persons = [
    {"name": "Alex", "login": "alexbig1987", "password": "12345678"},
    {"name": "Boris", "login": "boris1050", "password": "kdklsjjd11"},
    {"name": "Vasiliy", "login": "vasiavasia16", "password": "room134567"}
]

html = """
{% macro list_users(list_of_users) %}
<ul>
  {%- for i in list_of_users %}
  <li>{{ i['name'] }}{{ caller(i) }}</li>
  {%- endfor %}
</ul>
{% endmacro %}

{% call(users) list_users(users) %}
   <ul>
     <li>login: {{ users['login'] }}</li>
     <li>password: {{ users['password'] }}</li>
   </ul>
{% endcall %}
"""

tm = Template(html)
msg = tm.render(users=persons)

print(msg)