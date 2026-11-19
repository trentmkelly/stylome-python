from enum import Enum


class ApiUsageGroupBy(str, Enum):
    DAY = "day"
    KEY = "key"
    MODEL = "model"

    def __str__(self) -> str:
        return str(self.value)
