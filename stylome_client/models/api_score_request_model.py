from enum import Enum


class ApiScoreRequestModel(str, Enum):
    STYLOME_1_0_LARGE = "stylome-1.0-large"
    STYLOME_1_2_LARGE = "stylome-1.2-large"

    def __str__(self) -> str:
        return str(self.value)
