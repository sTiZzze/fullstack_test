from datetime import datetime
from typing import List

from pydantic import BaseModel, constr

from src.domain.addition.enum import StatusEnum, PriorityEnum


class TaskBase(BaseModel):
    id: int
    title: constr(max_length=50)
    task_info: constr(max_length=256)
    datetime_to_do: datetime

    class Config:
        from_attributes = True


class TaskCreateUpdate(BaseModel):
    title: constr(max_length=50)
    task_info: constr(max_length=256)
    datetime_to_do: datetime

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: constr(max_length=50)
    task_info: constr(max_length=256)
    priority: PriorityEnum
    status: StatusEnum
    datetime_to_do: datetime

    class Config:
        from_attributes = True


class TaskResponse(BaseModel):
    tasks: List[TaskBase]
