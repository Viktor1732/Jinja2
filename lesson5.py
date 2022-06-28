from jinja2 import FileSystemLoader, Environment

file_loader = FileSystemLoader('templates')
evn = Environment(loader=file_loader)
tm = evn.get_template("content.html")
msg = tm.render(domain="http://prorororgs.ru", title="Про программирование")

print(msg)
