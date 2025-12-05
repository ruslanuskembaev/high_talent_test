from typing import List, Optional

from sqlalchemy.orm import Session

from app import models, schemas


def create_question(db: Session, question_in: schemas.QuestionCreate) -> models.Question:
    question = models.Question(text=question_in.text)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


def get_questions(db: Session) -> List[models.Question]:
    return db.query(models.Question).order_by(models.Question.created_at.desc()).all()


def get_question(db: Session, question_id: int) -> Optional[models.Question]:
    return db.query(models.Question).filter(models.Question.id == question_id).first()


def delete_question(db: Session, question: models.Question) -> None:
    db.delete(question)
    db.commit()


def create_answer(db: Session, question_id: int, answer_in: schemas.AnswerCreate) -> models.Answer:
    answer = models.Answer(
        question_id=question_id,
        user_id=answer_in.user_id,
        text=answer_in.text,
    )
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer


def get_answer(db: Session, answer_id: int) -> Optional[models.Answer]:
    return db.query(models.Answer).filter(models.Answer.id == answer_id).first()


def delete_answer(db: Session, answer: models.Answer) -> None:
    db.delete(answer)
    db.commit()
