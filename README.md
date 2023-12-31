# Web-приложение для определения заполненных форм

Это веб-приложение предназначено для определения заполненных форм на основе заданных шаблонов. Проект разработан с использованием Flask, TinyDB и Python.

## Установка

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/ваш_пользователь/ваш_репозиторий.git
    ```

2. **Перейдите в каталог проекта:**

    ```bash
    cd ваш_репозиторий
    ```

3. **Создайте виртуальное окружение (рекомендуется):**

    ```bash
    python -m venv venv
    ```

4. **Активируйте виртуальное окружение:**

    - На Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - На MacOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

## Запуск приложения

### Локально

1. **Запустите ваше веб-приложение:**

    ```bash
    python app.py
    ```

2. **Перейдите по адресу http://127.0.0.1:5000/ в вашем веб-браузере.**

### С использованием Docker

1. **Создайте и запустите Docker-контейнер:**

    ```bash
    docker-compose up
    ```

2. **Откройте ваш веб-браузер и перейдите по адресу http://127.0.0.1:5000/**

## Тестирование

Для запуска тестов используйте следующую команду:

```bash
python test.py

"Примечание: Убедитесь, что приложение запущено перед выполнением тестов."
