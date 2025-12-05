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
  
## Скриншоты (для GitHub)
###

  **Основная страница FastAPI с автогенерируемой документацией**<img width="1484" height="823" alt="image" src="https://github.com/user-attachments/assets/1f4cb225-48db-4b6a-9791-ccb0696a6fe6" />

  ###
  
  **Запущенные контейнеры c логами**<img width="1110" height="859" alt="Снимок экрана 2025-12-06 в 01 31 49" src="https://github.com/user-attachments/assets/5fdfbcb9-eaac-4368-bf41-ed914d42cd8c" />

  ###
  
  **кофигурация контейнеров**<img width="1010" height="735" alt="Снимок экрана 2025-12-06 в 01 30 11" src="https://github.com/user-attachments/assets/23f1de5a-855d-4f8b-8441-ebfdd0e93439" />



