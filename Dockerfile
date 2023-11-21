# Используем базовый образ Python
FROM python:3.8

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы в контейнер
COPY . .

# Открываем порт 5000
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
