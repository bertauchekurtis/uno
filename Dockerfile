FROM python:3

COPY . /app

WORKDIR /app

ENTRYPOINT [ "python", "main.py" ]