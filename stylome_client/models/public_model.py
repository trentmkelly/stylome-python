from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.public_model_response_kind import PublicModelResponseKind
from ..models.public_model_status import PublicModelStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicModel")


@_attrs_define
class PublicModel:
    """
    Attributes:
        id (str):
        display_name (str):
        description (str):
        recommended (bool):
        normalization (str):
        operating_points (list[str]):
        default_operating_point (None | str):
        response_kind (PublicModelResponseKind):
        status (PublicModelStatus | Unset):  Default: PublicModelStatus.AVAILABLE.
        deprecation_date (datetime.datetime | None | Unset):
        retirement_date (datetime.datetime | None | Unset):
        min_characters (int | Unset):  Default: 200.
        max_characters (int | Unset):  Default: 10000.
        max_request_bytes (int | Unset):  Default: 131072.
        length_unit (Literal['normalized_unicode_code_points'] | Unset):  Default: 'normalized_unicode_code_points'.
        zero_content_retention_supported (bool | Unset):  Default: True.
        price_usd_per_million_characters (str | Unset):  Default: '5.000000'.
        pricing_version (str | Unset):  Default: 'api-characters-usd-2026-09-20'.
    """

    id: str
    display_name: str
    description: str
    recommended: bool
    normalization: str
    operating_points: list[str]
    default_operating_point: None | str
    response_kind: PublicModelResponseKind
    status: PublicModelStatus | Unset = PublicModelStatus.AVAILABLE
    deprecation_date: datetime.datetime | None | Unset = UNSET
    retirement_date: datetime.datetime | None | Unset = UNSET
    min_characters: int | Unset = 200
    max_characters: int | Unset = 10000
    max_request_bytes: int | Unset = 131072
    length_unit: Literal["normalized_unicode_code_points"] | Unset = "normalized_unicode_code_points"
    zero_content_retention_supported: bool | Unset = True
    price_usd_per_million_characters: str | Unset = "5.000000"
    pricing_version: str | Unset = "api-characters-usd-2026-09-20"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        description = self.description

        recommended = self.recommended

        normalization = self.normalization

        operating_points = self.operating_points

        default_operating_point: None | str
        default_operating_point = self.default_operating_point

        response_kind = self.response_kind.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        deprecation_date: None | str | Unset
        if isinstance(self.deprecation_date, Unset):
            deprecation_date = UNSET
        elif isinstance(self.deprecation_date, datetime.datetime):
            deprecation_date = self.deprecation_date.isoformat()
        else:
            deprecation_date = self.deprecation_date

        retirement_date: None | str | Unset
        if isinstance(self.retirement_date, Unset):
            retirement_date = UNSET
        elif isinstance(self.retirement_date, datetime.datetime):
            retirement_date = self.retirement_date.isoformat()
        else:
            retirement_date = self.retirement_date

        min_characters = self.min_characters

        max_characters = self.max_characters

        max_request_bytes = self.max_request_bytes

        length_unit = self.length_unit

        zero_content_retention_supported = self.zero_content_retention_supported

        price_usd_per_million_characters = self.price_usd_per_million_characters

        pricing_version = self.pricing_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "description": description,
                "recommended": recommended,
                "normalization": normalization,
                "operating_points": operating_points,
                "default_operating_point": default_operating_point,
                "response_kind": response_kind,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if deprecation_date is not UNSET:
            field_dict["deprecation_date"] = deprecation_date
        if retirement_date is not UNSET:
            field_dict["retirement_date"] = retirement_date
        if min_characters is not UNSET:
            field_dict["min_characters"] = min_characters
        if max_characters is not UNSET:
            field_dict["max_characters"] = max_characters
        if max_request_bytes is not UNSET:
            field_dict["max_request_bytes"] = max_request_bytes
        if length_unit is not UNSET:
            field_dict["length_unit"] = length_unit
        if zero_content_retention_supported is not UNSET:
            field_dict["zero_content_retention_supported"] = zero_content_retention_supported
        if price_usd_per_million_characters is not UNSET:
            field_dict["price_usd_per_million_characters"] = price_usd_per_million_characters
        if pricing_version is not UNSET:
            field_dict["pricing_version"] = pricing_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("display_name")

        description = d.pop("description")

        recommended = d.pop("recommended")

        normalization = d.pop("normalization")

        operating_points = cast(list[str], d.pop("operating_points"))

        def _parse_default_operating_point(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        default_operating_point = _parse_default_operating_point(d.pop("default_operating_point"))

        response_kind = PublicModelResponseKind(d.pop("response_kind"))

        _status = d.pop("status", UNSET)
        status: PublicModelStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PublicModelStatus(_status)

        def _parse_deprecation_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deprecation_date_type_0 = datetime.datetime.fromisoformat(data)

                return deprecation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deprecation_date = _parse_deprecation_date(d.pop("deprecation_date", UNSET))

        def _parse_retirement_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retirement_date_type_0 = datetime.datetime.fromisoformat(data)

                return retirement_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        retirement_date = _parse_retirement_date(d.pop("retirement_date", UNSET))

        min_characters = d.pop("min_characters", UNSET)

        max_characters = d.pop("max_characters", UNSET)

        max_request_bytes = d.pop("max_request_bytes", UNSET)

        length_unit = cast(Literal["normalized_unicode_code_points"] | Unset, d.pop("length_unit", UNSET))
        if length_unit != "normalized_unicode_code_points" and not isinstance(length_unit, Unset):
            raise ValueError(f"length_unit must match const 'normalized_unicode_code_points', got '{length_unit}'")

        zero_content_retention_supported = d.pop("zero_content_retention_supported", UNSET)

        price_usd_per_million_characters = d.pop("price_usd_per_million_characters", UNSET)

        pricing_version = d.pop("pricing_version", UNSET)

        public_model = cls(
            id=id,
            display_name=display_name,
            description=description,
            recommended=recommended,
            normalization=normalization,
            operating_points=operating_points,
            default_operating_point=default_operating_point,
            response_kind=response_kind,
            status=status,
            deprecation_date=deprecation_date,
            retirement_date=retirement_date,
            min_characters=min_characters,
            max_characters=max_characters,
            max_request_bytes=max_request_bytes,
            length_unit=length_unit,
            zero_content_retention_supported=zero_content_retention_supported,
            price_usd_per_million_characters=price_usd_per_million_characters,
            pricing_version=pricing_version,
        )

        public_model.additional_properties = d
        return public_model

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
