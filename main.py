from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
from collections import Counter

app = Flask(__name__)
environment = Environment(loader=FileSystemLoader("./"))

def calculate_compatibility(name_1, name_2):
    name = name_1 + name_2
    count_dict = Counter(name)
    values = count_dict.values()
    while len(values) > 2:
        n = values[0] + values[-1]
        


def calculate(name_1, name_2):
    name = name_1 + name_2
    name_d = Counter(name)
    count_list = []
    for i in name_d:
        count_list.append(name_d[i])
    
    

@app.route("/", methods=['GET', 'POST'])
def hello():
    if 'first_name' not in request.args:
        first_name = ''
    else:
        first_name = request.args['first_name']
    if 'second_name' not in request.args:
        second_name = ''
    else:
        second_name = request.args['second_name']
    percentage = calculate_compatibility(first_name, second_name)
    template = environment.get_template("index.html")
    return template.render(first_name=first_name, second_name=second_name, percentage=percentage)

def main():
     app.run(debug=True)


if __name__ == '__main__':
    main()