import sys
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))

if len(sys.argv) != 3:
    print('Usage:', sys.argv[0], 'TEMPLATE USER')
    sys.exit(1)

template = environment.get_template(sys.argv[1] + ".txt")
print(template.render(user=sys.argv[2]))