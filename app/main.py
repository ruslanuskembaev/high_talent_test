from fastapi import FastAPI
from loguru import logger

from app.api.routes import answers, questions

app = FastAPI(title="Q&A Service", version="1.0.0")

logger.info("Application startup")

app.include_router(questions.router)
app.include_router(answers.router)


@app.get("/health", tags=["service"])
def healthcheck():
    return {"status": "ok"}
