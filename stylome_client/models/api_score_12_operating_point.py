from enum import Enum


class ApiScore12OperatingPoint(str, Enum):
    VALUE_0 = "0.01%"
    VALUE_1 = "0.1%"

    def __str__(self) -> str:
        return str(self.value)
