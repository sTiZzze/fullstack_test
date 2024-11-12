from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.addition.enum import StatusEnum, PriorityEnum
from src.domain.models.abstract_models import AbstractModel
from src.domain.models.user import User


class Task(AbstractModel):
    __tablename__ = 'task'
    __mapper_args__ = {"concrete": True}
    __table_args__ = {"postgresql_inherits": AbstractModel.__tablename__}

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String,  nullable=False)
    task_info: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[StatusEnum] = mapped_column(
        SQLAlchemyEnum(StatusEnum, create_type=True),
        default=StatusEnum.in_progress,
        nullable=False,
    )
    priority: Mapped[PriorityEnum] = mapped_column(
        SQLAlchemyEnum(PriorityEnum, create_type=True),
        default=PriorityEnum.average,
        nullable=False,
    )
    datetime_to_do = mapped_column(DateTime(timezone=True))
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    user: Mapped["User"] = relationship()
