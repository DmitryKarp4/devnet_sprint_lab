FROM python:3.9-slim
RUN pip install --no-cache-dir --progress-bar off Flask==2.0.3 Werkzeug==2.0.3

# Указываем Flask, какой файл запускать
ENV FLASK_APP=/home/myapp/sample_app.py

COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY sample_app.py /home/myapp/

EXPOSE 5050

# Запуск без потоков и с указанием хоста
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5050", "--without-threads"]
