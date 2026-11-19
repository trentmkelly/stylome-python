from enum import Enum


class ApiStatusDatabase(str, Enum):
    REACHABLE = "reachable"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
