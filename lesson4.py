from jinja2 import Environment, FunctionLoader

persons = [
    {"name": "Alex", "login": "alexbig1987", "password": "12345678"},
    {"name": "Boris", "login": "boris1050", "password": "kdklsjjd11"},
    {"name": "Vasiliy", "login": "vasiavasia16", "password": "room134567"}
]


# file_loader = FileSystemLoader('templates')
# evn = Environment(loader=file_loader)
#
# tm = evn.get_template("main.html")
# msg = tm.render(users=persons)


# print(msg)

def loadTpl(path):
    if path == 'index':
        return """имя: {{ per.name }}, логин: {{ per.login }}, пароль: {{ per.password }}"""
    else:
        return """{{ per }}"""


file_loader = FunctionLoader(loadTpl)
evn = Environment(loader=file_loader)
tm = evn.get_template("index")
msg = tm.render(per=persons[2])

print(msg)
