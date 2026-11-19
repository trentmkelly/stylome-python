from enum import Enum


class ApiStatusStatus(str, Enum):
    DEGRADED = "degraded"
    OPERATIONAL = "operational"

    def __str__(self) -> str:
        return str(self.value)
