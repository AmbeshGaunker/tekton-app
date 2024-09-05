
FROM python:3.11-alpine

WORKDIR /app

COPY src /app/src

ENV PYTHONUNBUFFERED=1

CMD ["python", "/app/src/main.py"]
