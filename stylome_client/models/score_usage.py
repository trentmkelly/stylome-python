from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScoreUsage")


@_attrs_define
class ScoreUsage:
    """
    Attributes:
        input_characters (int): Normalized Unicode code points; the same normalization used for inference and input
            limits.
        cost_usd (str): Original operation's committed cost. An idempotent replay does not charge this amount again.
        currency (Literal['USD'] | Unset):  Default: 'USD'.
        pricing_version (str | Unset):  Default: 'api-characters-usd-2026-09-20'.
    """

    input_characters: int
    cost_usd: str
    currency: Literal["USD"] | Unset = "USD"
    pricing_version: str | Unset = "api-characters-usd-2026-09-20"

    def to_dict(self) -> dict[str, Any]:
        input_characters = self.input_characters

        cost_usd = self.cost_usd

        currency = self.currency

        pricing_version = self.pricing_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "input_characters": input_characters,
                "cost_usd": cost_usd,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency
        if pricing_version is not UNSET:
            field_dict["pricing_version"] = pricing_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_characters = d.pop("input_characters")

        cost_usd = d.pop("cost_usd")

        currency = cast(Literal["USD"] | Unset, d.pop("currency", UNSET))
        if currency != "USD" and not isinstance(currency, Unset):
            raise ValueError(f"currency must match const 'USD', got '{currency}'")

        pricing_version = d.pop("pricing_version", UNSET)

        score_usage = cls(
            input_characters=input_characters,
            cost_usd=cost_usd,
            currency=currency,
            pricing_version=pricing_version,
        )

        return score_usage
