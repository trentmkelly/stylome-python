from enum import Enum


class ApiScore12Label(str, Enum):
    AI_EDITED = "ai_edited"
    AI_GENERATED = "ai_generated"
    HUMAN_WRITTEN = "human_written"

    def __str__(self) -> str:
        return str(self.value)
