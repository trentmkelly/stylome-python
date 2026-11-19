from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_status_database import ApiStatusDatabase
from ..models.api_status_inference import ApiStatusInference
from ..models.api_status_status import ApiStatusStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiStatus")


@_attrs_define
class ApiStatus:
    """
    Attributes:
        status (ApiStatusStatus):
        checked_at (datetime.datetime):
        database (ApiStatusDatabase):
        inference (ApiStatusInference):
        object_ (Literal['api_status'] | Unset):  Default: 'api_status'.
        description (str | Unset):  Default: 'API and database reachability with inference configuration presence. Does
            not run inference or measure model availability.'.
    """

    status: ApiStatusStatus
    checked_at: datetime.datetime
    database: ApiStatusDatabase
    inference: ApiStatusInference
    object_: Literal["api_status"] | Unset = "api_status"
    description: str | Unset = (
        "API and database reachability with inference configuration presence. Does not run inference or measure model availability."
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        checked_at = self.checked_at.isoformat()

        database = self.database.value

        inference = self.inference.value

        object_ = self.object_

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "checked_at": checked_at,
                "database": database,
                "inference": inference,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ApiStatusStatus(d.pop("status"))

        checked_at = datetime.datetime.fromisoformat(d.pop("checked_at"))

        database = ApiStatusDatabase(d.pop("database"))

        inference = ApiStatusInference(d.pop("inference"))

        object_ = cast(Literal["api_status"] | Unset, d.pop("object", UNSET))
        if object_ != "api_status" and not isinstance(object_, Unset):
            raise ValueError(f"object must match const 'api_status', got '{object_}'")

        description = d.pop("description", UNSET)

        api_status = cls(
            status=status,
            checked_at=checked_at,
            database=database,
            inference=inference,
            object_=object_,
            description=description,
        )

        api_status.additional_properties = d
        return api_status

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
