from enum import Enum


class PublicModelStatus(str, Enum):
    AVAILABLE = "available"
    DEPRECATED = "deprecated"

    def __str__(self) -> str:
        return str(self.value)
