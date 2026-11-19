from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_key_identity_retention_mode import ApiKeyIdentityRetentionMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyIdentity")


@_attrs_define
class ApiKeyIdentity:
    """
    Attributes:
        public_id (str):
        project_id (str):
        scopes (list[str]):
        retention_mode (ApiKeyIdentityRetentionMode):
        expires_at (datetime.datetime | None):
        rate_limit_exempt (bool):
        object_ (Literal['api_key'] | Unset):  Default: 'api_key'.
    """

    public_id: str
    project_id: str
    scopes: list[str]
    retention_mode: ApiKeyIdentityRetentionMode
    expires_at: datetime.datetime | None
    rate_limit_exempt: bool
    object_: Literal["api_key"] | Unset = "api_key"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_id = self.public_id

        project_id = self.project_id

        scopes = self.scopes

        retention_mode = self.retention_mode.value

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        rate_limit_exempt = self.rate_limit_exempt

        object_ = self.object_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "public_id": public_id,
                "project_id": project_id,
                "scopes": scopes,
                "retention_mode": retention_mode,
                "expires_at": expires_at,
                "rate_limit_exempt": rate_limit_exempt,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        public_id = d.pop("public_id")

        project_id = d.pop("project_id")

        scopes = cast(list[str], d.pop("scopes"))

        retention_mode = ApiKeyIdentityRetentionMode(d.pop("retention_mode"))

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        rate_limit_exempt = d.pop("rate_limit_exempt")

        object_ = cast(Literal["api_key"] | Unset, d.pop("object", UNSET))
        if object_ != "api_key" and not isinstance(object_, Unset):
            raise ValueError(f"object must match const 'api_key', got '{object_}'")

        api_key_identity = cls(
            public_id=public_id,
            project_id=project_id,
            scopes=scopes,
            retention_mode=retention_mode,
            expires_at=expires_at,
            rate_limit_exempt=rate_limit_exempt,
            object_=object_,
        )

        api_key_identity.additional_properties = d
        return api_key_identity

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
