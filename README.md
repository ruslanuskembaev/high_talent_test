# Тестовое: API сервис вопросов и ответов

Небольшой FastAPI-сервис c PostgreSQL и Alembic, обёрнутый в Docker Compose. Реализованы CRUD для вопросов и ответов, каскадное удаление и простые автотесты.

## Запуск
1. Скопируйте `env.example` в `.env` при необходимости и поправьте переменные (по умолчанию Postgres в docker-compose):
   ```bash
   cp env.example .env
   ```
2. Запустите контейнеры:
   ```bash
   docker-compose up --build
   ```
3. Приложение будет доступно на `http://localhost:8000`, Swagger — `http://localhost:8000/docs`.

## Локально без Docker (опционально)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

## Тесты
```bash
pytest
```

## Основные моменты
- Стек: FastAPI, SQLAlchemy 2.0, Alembic, PostgreSQL.
- Валидация входных данных через Pydantic (нельзя создавать пустые тексты, user_id обязателен).
- Каскадное удаление ответов через `ForeignKey(ondelete="CASCADE")` и `cascade="all, delete-orphan"` на модели.
- Миграции: `alembic/versions/20241205_0001_init.py` создаёт таблицы `questions` и `answers`.
- Роуты:
  - `GET /questions/`, `POST /questions/`, `GET /questions/{id}`, `DELETE /questions/{id}`
  - `POST /questions/{id}/answers/`
  - `GET /answers/{id}`, `DELETE /answers/{id}`
- Простой healthcheck: `GET /health`.
