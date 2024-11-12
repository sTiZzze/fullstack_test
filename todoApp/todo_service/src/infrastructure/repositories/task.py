from typing import Iterable

from fastapi import HTTPException
from sqlalchemy import update, delete, case
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.domain.addition.enum import PriorityEnum
from src.domain.models.task import Task
from src.domain.models.user import User
from src.domain.DTO.task import TaskCreateUpdate, TaskUpdate


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def get_all(self, entity: Task, user: User) -> Iterable[Task]:
        query = await self.__session.execute(
            select(entity).filter(Task.user_id == user.id).order_by(
                case(
                    (Task.priority == PriorityEnum.important, 0),
                    (Task.priority == PriorityEnum.average, 1)
                )
            )
        )
        return query.scalars().all()

    async def get_by_id(self, entity: Task, user: User, id: int) -> Task:
        query = await self.__session.execute(
            select(entity).filter(entity.id == id, Task.user_id == user.id)
        )
        task = query.scalar_one_or_none()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found.")
        return task

    async def create(self, entity: Task, model: TaskCreateUpdate, user: User) -> Task:
        new_task = Task(
            title=model.title,
            task_info=model.task_info,
            user_id=user.id,
            datetime_to_do=model.datetime_to_do
        )

        self.__session.add(new_task)
        await self.__session.commit()
        await self.__session.refresh(new_task)

        return new_task

    async def update(self, entity: Task, model: TaskUpdate, user: User, id: int) -> Task:
        task_query = await self.__session.execute(
            select(entity).filter(entity.id == int(id), Task.user_id == int(user.id))
        )
        task = task_query.scalar_one_or_none()
        if not task:
            raise HTTPException(
                status_code=404, detail="Task not found."
            )

        stmt = (
            update(entity)
            .where(entity.id == int(id))
            .values(**model.model_dump())
        )
        await self.__session.execute(stmt)
        await self.__session.commit()
        await self.__session.refresh(task)
        return task


    async def delete(self, entity: Task, user: User, id: int) -> None:
        task_query = await self.__session.execute(
            select(entity).filter(entity.id == id, Task.user_id == user.id)
        )
        task = task_query.scalar_one_or_none()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found.")

        await self.__session.execute(delete(entity).where(entity.id == id))
        await self.__session.commit()
