from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiBalance")


@_attrs_define
class ApiBalance:
    """
    Attributes:
        balance_usd (str):
        reserved_usd (str):
        available_usd (str):
        billing_review_required (bool):
        topup_min_usd (str):
        topup_max_usd (str):
        currency (Literal['USD'] | Unset):  Default: 'USD'.
    """

    balance_usd: str
    reserved_usd: str
    available_usd: str
    billing_review_required: bool
    topup_min_usd: str
    topup_max_usd: str
    currency: Literal["USD"] | Unset = "USD"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_usd = self.balance_usd

        reserved_usd = self.reserved_usd

        available_usd = self.available_usd

        billing_review_required = self.billing_review_required

        topup_min_usd = self.topup_min_usd

        topup_max_usd = self.topup_max_usd

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balance_usd": balance_usd,
                "reserved_usd": reserved_usd,
                "available_usd": available_usd,
                "billing_review_required": billing_review_required,
                "topup_min_usd": topup_min_usd,
                "topup_max_usd": topup_max_usd,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance_usd = d.pop("balance_usd")

        reserved_usd = d.pop("reserved_usd")

        available_usd = d.pop("available_usd")

        billing_review_required = d.pop("billing_review_required")

        topup_min_usd = d.pop("topup_min_usd")

        topup_max_usd = d.pop("topup_max_usd")

        currency = cast(Literal["USD"] | Unset, d.pop("currency", UNSET))
        if currency != "USD" and not isinstance(currency, Unset):
            raise ValueError(f"currency must match const 'USD', got '{currency}'")

        api_balance = cls(
            balance_usd=balance_usd,
            reserved_usd=reserved_usd,
            available_usd=available_usd,
            billing_review_required=billing_review_required,
            topup_min_usd=topup_min_usd,
            topup_max_usd=topup_max_usd,
            currency=currency,
        )

        api_balance.additional_properties = d
        return api_balance

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
