from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageCounts")


@_attrs_define
class UsageCounts:
    """
    Attributes:
        requests (int):
        successes (int):
        failures (int):
        pending (int):
        billed_characters (int | Unset):  Default: 0.
        cost_usd (str | Unset):  Default: '0.000000'.
        unpriced_requests (int | Unset):  Default: 0.
    """

    requests: int
    successes: int
    failures: int
    pending: int
    billed_characters: int | Unset = 0
    cost_usd: str | Unset = "0.000000"
    unpriced_requests: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requests = self.requests

        successes = self.successes

        failures = self.failures

        pending = self.pending

        billed_characters = self.billed_characters

        cost_usd = self.cost_usd

        unpriced_requests = self.unpriced_requests

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requests": requests,
                "successes": successes,
                "failures": failures,
                "pending": pending,
            }
        )
        if billed_characters is not UNSET:
            field_dict["billed_characters"] = billed_characters
        if cost_usd is not UNSET:
            field_dict["cost_usd"] = cost_usd
        if unpriced_requests is not UNSET:
            field_dict["unpriced_requests"] = unpriced_requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        requests = d.pop("requests")

        successes = d.pop("successes")

        failures = d.pop("failures")

        pending = d.pop("pending")

        billed_characters = d.pop("billed_characters", UNSET)

        cost_usd = d.pop("cost_usd", UNSET)

        unpriced_requests = d.pop("unpriced_requests", UNSET)

        usage_counts = cls(
            requests=requests,
            successes=successes,
            failures=failures,
            pending=pending,
            billed_characters=billed_characters,
            cost_usd=cost_usd,
            unpriced_requests=unpriced_requests,
        )

        usage_counts.additional_properties = d
        return usage_counts

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
