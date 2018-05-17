from flask import Flask, request
from jinja2 import Environment, FileSystemLoader
from collections import Counter

app = Flask(__name__)
environment = Environment(loader=FileSystemLoader("./"))

def calculate_compatibility(name_1, name_2):
    name = name_1 + name_2
    count = 0
    count_dict = Counter(name)
    for i in name:
        count += count_dict[i]
    percent = (count - len(name_1)) * len(name_2)
    if percent > 100:
        return percent / len(name_2)
    if percent < 0:
        return 0
    return percent

@app.route("/", methods=['GET', 'POST'])
def hello():
    first_name = request.args['first_name']
    second_name = request.args['second_name']
    percentage = calculate_compatibility(first_name, second_name)
    template = environment.get_template("index.html")
    return template.render(first_name=first_name, second_name=second_name, percentage=percentage)

def main():
     app.run(debug=True)


if __name__ == '__main__':
    main()