FROM python:3.11-alpine AS base

WORKDIR /app

COPY src /app/src

RUN pip install pytest


FROM base AS runtime

ENV PYTHONUNBUFFERED=1

FROM base AS test

RUN ["pytest", "/app/src/tests"]

CMD ["python", "/app/src/main.py"]
