from enum import Enum


class ApiKeyIdentityRetentionMode(str, Enum):
    STANDARD = "standard"
    ZERO_CONTENT = "zero_content"

    def __str__(self) -> str:
        return str(self.value)
