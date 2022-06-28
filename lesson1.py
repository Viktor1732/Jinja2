from jinja2 import Template


# your_name = 'Василий'
# my_name = "Виктор"
# my_age = 33
#
# tm = Template("Привет {{ name }}, меня зовут {{ name2 }}. Мне {{ age }} года!")
# msg = tm.render(name=your_name, name2=my_name, age=my_age)


# class Person:
#     def __init__(self, my_name, my_age, your_name):
#         self.my_name = my_name
#         self.my_age = my_age
#         self.your_name = your_name
#
#
# per = Person('Виктор', 33, 'Василий')
#
# tm = Template("Привет {{ p.your_name }}, меня зовут {{ p.my_name }}. Мне {{ p.my_age }} года!")
# msg = tm.render(p=per)


# class Person:
#     def __init__(self, my_name, my_age, your_name):
#         self.my_name = my_name
#         self.my_age = my_age
#         self.your_name = your_name
#
#     def get_my_name(self):
#         return self.my_name
#
#     def get_my_age(self):
#         return self.my_age
#
#     def get_your_name(self):
#         return self.your_name
#
#
# per = Person('Виктор', 33, 'Василий')
#
# tm = Template("Привет {{ p.get_your_name() }}, меня зовут {{ p.get_my_name() }}. Мне {{ p.get_my_age() }} года!")
# msg = tm.render(p=per)


per = {'name': 'Василий', 'age': 33}


tm = Template("Привет {{ p['name'] }}. Мне {{ p.age }} года!")
msg = tm.render(p=per)

print(msg)
