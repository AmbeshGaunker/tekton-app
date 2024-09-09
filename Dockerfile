FROM python:3.11-alpine AS base

WORKDIR /app

COPY src /app/src

RUN pip install pytest


FROM base AS runtime

ENV PYTHONUNBUFFERED=1

CMD ["python", "/app/src/main.py"]

FROM base AS test

CMD ["pytest", "/app/src/tests"]
