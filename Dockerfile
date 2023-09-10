# Базовый образ для Приложения
FROM python:3.11.4

# Установка зависимостей Приложения
RUN pip3 install --upgrade pip
COPY app/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Копирование кода приложения
COPY app /app
WORKDIR /app

# Запуск Приложения
CMD python /app/andom.py & tail -f /dev/null

