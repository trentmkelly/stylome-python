from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_usage_group_by import ApiUsageGroupBy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_bucket import UsageBucket
    from ..models.usage_counts import UsageCounts


T = TypeVar("T", bound="ApiUsage")


@_attrs_define
class ApiUsage:
    """
    Attributes:
        start (datetime.datetime):
        end (datetime.datetime):
        measured_at (datetime.datetime):
        group_by (ApiUsageGroupBy):
        totals (UsageCounts):
        data (list[UsageBucket]):
        object_ (Literal['api_usage'] | Unset):  Default: 'api_usage'.
        description (str | Unset):  Default: 'Request-ledger operations by start time; excludes idempotent replays and
            failures before ledger creation. Costs are exact prepaid debits; historical unpriced requests have no inferred
            charge.'.
    """

    start: datetime.datetime
    end: datetime.datetime
    measured_at: datetime.datetime
    group_by: ApiUsageGroupBy
    totals: UsageCounts
    data: list[UsageBucket]
    object_: Literal["api_usage"] | Unset = "api_usage"
    description: str | Unset = (
        "Request-ledger operations by start time; excludes idempotent replays and failures before ledger creation. Costs are exact prepaid debits; historical unpriced requests have no inferred charge."
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start.isoformat()

        end = self.end.isoformat()

        measured_at = self.measured_at.isoformat()

        group_by = self.group_by.value

        totals = self.totals.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        object_ = self.object_

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "measured_at": measured_at,
                "group_by": group_by,
                "totals": totals,
                "data": data,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_bucket import UsageBucket
        from ..models.usage_counts import UsageCounts

        d = dict(src_dict)
        start = datetime.datetime.fromisoformat(d.pop("start"))

        end = datetime.datetime.fromisoformat(d.pop("end"))

        measured_at = datetime.datetime.fromisoformat(d.pop("measured_at"))

        group_by = ApiUsageGroupBy(d.pop("group_by"))

        totals = UsageCounts.from_dict(d.pop("totals"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = UsageBucket.from_dict(data_item_data)

            data.append(data_item)

        object_ = cast(Literal["api_usage"] | Unset, d.pop("object", UNSET))
        if object_ != "api_usage" and not isinstance(object_, Unset):
            raise ValueError(f"object must match const 'api_usage', got '{object_}'")

        description = d.pop("description", UNSET)

        api_usage = cls(
            start=start,
            end=end,
            measured_at=measured_at,
            group_by=group_by,
            totals=totals,
            data=data,
            object_=object_,
            description=description,
        )

        api_usage.additional_properties = d
        return api_usage

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
