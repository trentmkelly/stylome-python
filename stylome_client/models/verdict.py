from enum import Enum


class Verdict(str, Enum):
    AI_TYPICAL = "ai_typical"
    HUMAN_TYPICAL = "human_typical"
    MIXED_SIGNALS = "mixed_signals"

    def __str__(self) -> str:
        return str(self.value)
