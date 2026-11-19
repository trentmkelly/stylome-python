from enum import Enum


class GetUsageGroupBy(str, Enum):
    DAY = "day"
    KEY = "key"
    MODEL = "model"

    def __str__(self) -> str:
        return str(self.value)
