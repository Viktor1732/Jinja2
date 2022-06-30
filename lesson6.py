from jinja2 import FileSystemLoader, Environment

list_users = ["Вася", "Петя", "Даша", "Каша"]


file_loader = FileSystemLoader('templates')
evn = Environment(loader=file_loader)
tm = evn.get_template("about.html")
msg = tm.render(list_people=list_users)

print(msg)
