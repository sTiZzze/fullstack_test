from enum import Enum


class StatusEnum(str, Enum):
    in_progress = "в прогрессе"
    is_done = "выполнено"


class PriorityEnum(str, Enum):
    important = "важно"
    average = "средне"
