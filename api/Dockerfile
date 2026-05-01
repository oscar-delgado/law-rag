FROM python:3.12.12-slim-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install poetry==2.3.2

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

EXPOSE 5000

CMD ["fastapi", "dev", "src/main.py", "--host", "0.0.0.0"]
