from enum import Enum


class PublicModelResponseKind(str, Enum):
    CATEGORICAL = "categorical"
    LEGACY_NUMERIC = "legacy_numeric"

    def __str__(self) -> str:
        return str(self.value)
