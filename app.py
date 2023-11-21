from flask import Flask, request, jsonify
from tinydb import TinyDB
import re
from datetime import datetime


app = Flask(__name__)
db = TinyDB('database.json')


# Загружаем тестовую базу данных
db.insert({"name": "MyForm", "field_name_1": "email", "field_name_2": "phone"})
db.insert({"name": "OrderForm", "field_name_1": "user_name", "field_name_2": "order_date"})


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form
    template_name = find_matching_template(data)

    if template_name:
        return jsonify({"template_name": template_name})
    else:
        field_types = type_fields(data)
        return jsonify(field_types)


def find_matching_template(data):
    for template in db:
        template_fields = set(template.keys()) - {'name'}  # Убираем имя шаблона
        data_fields = set(data.keys())

        if template_fields.issubset(data_fields):
            if all(data[field] == template[field] for field in template_fields):
                return template['name']

    return None


def type_fields(data):
    field_types = {}

    for field, value in data.items():
        if is_valid_date(value):
            field_types[field] = "date"
        elif is_valid_phone(value):
            field_types[field] = "phone"
        elif is_valid_email(value):
            field_types[field] = "email"
        else:
            field_types[field] = "text"

    return field_types


def is_valid_date(value):
    date_formats = ['%d.%m.%Y', '%Y-%m-%d']
    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return True
        except ValueError as e:
            print(f"Error validating date {value}: {e}")
            return False

    return False


def is_valid_phone(value):
    pattern = re.compile(r'^\+7 \d{3} \d{3} \d{2} \d{2}$')
    try:
        return bool(re.match(pattern, value))
    except re.error as e:
        print(f"Error validating phone {value}: {e}")
        return False


def is_valid_email(value):
    pattern = re.compile(r'^\S+@\S+\.\S+$')
    try:
        return bool(re.match(pattern, value))
    except re.error as e:
        print(f"Error validating email {value}: {e}")
        return False


@app.route('/')
def index():
    return "Hello, this is the main page!"


if __name__ == '__main__':
    app.run(debug=True)
