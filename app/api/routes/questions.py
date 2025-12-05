from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.deps import get_db

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/", response_model=list[schemas.QuestionRead])
def list_questions(db: Session = Depends(get_db)):
    return crud.get_questions(db)


@router.post("/", response_model=schemas.QuestionRead, status_code=status.HTTP_201_CREATED)
def create_question(question_in: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db, question_in)


@router.get("/{question_id}", response_model=schemas.QuestionRead)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    return question


@router.delete("/{question_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    crud.delete_question(db, question)
    return None


