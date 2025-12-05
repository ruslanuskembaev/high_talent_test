from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.deps import get_db

router = APIRouter(prefix="/answers", tags=["answers"])

@router.post(
    "/{question_id}/answers/",
    response_model=schemas.AnswerRead,
    status_code=status.HTTP_201_CREATED,
)
def create_answer_for_question(
    question_id: int, answer_in: schemas.AnswerCreate, db: Session = Depends(get_db)
):
    question = crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Question not found")
    return crud.create_answer(db, question_id, answer_in)

@router.get("/{answer_id}", response_model=schemas.AnswerRead)
def get_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = crud.get_answer(db, answer_id)
    if not answer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Answer not found")
    return answer


@router.delete("/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = crud.get_answer(db, answer_id)
    if not answer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Answer not found")
    crud.delete_answer(db, answer)
    return None
