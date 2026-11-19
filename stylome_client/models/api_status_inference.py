from enum import Enum


class ApiStatusInference(str, Enum):
    CONFIGURED = "configured"
    UNCONFIGURED = "unconfigured"

    def __str__(self) -> str:
        return str(self.value)
