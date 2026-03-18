#!/bin/bash

# 1. Подготовка
rm -rf tempdir
mkdir -p tempdir/templates tempdir/static

# 2. Копирование
cp sample_app.py tempdir/
cp -r templates/* tempdir/templates/
cp -r static/* tempdir/static/

# 3. Создание Dockerfile
cat <<EOF > tempdir/Dockerfile
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
EOF

# 4. Сборка и запуск
cd tempdir
docker stop samplerunning 2>/dev/null
docker rm samplerunning 2>/dev/null
docker build -t sampleapp . | tee /home/devasc/devnet-day1-ib-23-5b-karpyuk/artifacts/day4/docker/sampleapp_build_log.txt
docker run -d -p 5050:5050 --name samplerunning sampleapp

# 5. Проверка статуса
sleep 2
docker ps -a
#
