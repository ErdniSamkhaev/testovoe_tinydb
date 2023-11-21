import requests

from app import db

# URL вашего веб-приложения
url = 'http://127.0.0.1:5000/get_form'

# Очистить базу данных перед добавлением записей
db.truncate()

# Добавить записи
db.insert({"name": "MyForm", "field_name_1": "email", "field_name_2": "phone"})
db.insert({"name": "OrderForm", "field_name_1": "user_name", "field_name_2": "order_date"})


# Тест 1: Подходящий шаблон
data1 = {'f_name1': 'test@example.com', 'f_name2': '+7 123 456 78 90'}
response1 = requests.post(url, data=data1)
print(response1.json())  # Ожидаемый вывод: {"template_name": "MyForm"}

# Тест 2: Подходящий шаблон
data2 = {'f_name1': 'john.doe@example.com', 'f_name2': '2022-01-01'}
response2 = requests.post(url, data=data2)
print(response2.json())  # Ожидаемый вывод: {"template_name": "OrderForm"}

# Тест 3: Неподходящий шаблон
data3 = {'f_name1': 'some_text', 'f_name2': '+7 987 654 32 10'}
response3 = requests.post(url, data=data3)
print(response3.json())  # Ожидаемый вывод: {"f_name1": "email", "f_name2": "phone"}

# Тест 4: Подходящий шаблон, но с дополнительным полем
data4 = {'f_name1': 'test@example.com', 'f_name2': '+7 123 456 78 90', 'extra_field': 'some_value'}
response4 = requests.post(url, data=data4)
print(response4.json())  # Ожидаемый вывод: {"template_name": "MyForm"}

# Тест 5: Проверка типизации полей
data5 = {'text_field': 'some_text', 'date_field': '2022-01-01', 'phone_field': '+7 987 654 32 10'}
response5 = requests.post(url, data=data5)
print(response5.json())  # Ожидаемый вывод: {"text_field": "text", "date_field": "date", "phone_field": "phone"}
