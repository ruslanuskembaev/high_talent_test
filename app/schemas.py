from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict


class QuestionBase(BaseModel):
    text: str = Field(..., min_length=1, max_length=10_000)


class QuestionCreate(QuestionBase):
    pass


class AnswerBase(BaseModel):
    text: str = Field(..., min_length=1, max_length=10_000)
    user_id: str = Field(..., min_length=1, max_length=64)


class AnswerCreate(AnswerBase):
    pass


class AnswerRead(AnswerBase):
    id: int
    question_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class QuestionRead(QuestionBase):
    id: int
    created_at: datetime
    answers: List[AnswerRead] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
