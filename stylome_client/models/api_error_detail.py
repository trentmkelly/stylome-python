from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_error_field import ApiErrorField


T = TypeVar("T", bound="ApiErrorDetail")


@_attrs_define
class ApiErrorDetail:
    """
    Attributes:
        code (str):
        message (str):
        request_id (str):
        retryable (bool):
        param (None | str | Unset):
        fields (list[ApiErrorField] | None | Unset):
    """

    code: str
    message: str
    request_id: str
    retryable: bool
    param: None | str | Unset = UNSET
    fields: list[ApiErrorField] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        request_id = self.request_id

        retryable = self.retryable

        param: None | str | Unset
        if isinstance(self.param, Unset):
            param = UNSET
        else:
            param = self.param

        fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.to_dict()
                fields.append(fields_type_0_item)

        else:
            fields = self.fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "request_id": request_id,
                "retryable": retryable,
            }
        )
        if param is not UNSET:
            field_dict["param"] = param
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_error_field import ApiErrorField

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        request_id = d.pop("request_id")

        retryable = d.pop("retryable")

        def _parse_param(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        param = _parse_param(d.pop("param", UNSET))

        def _parse_fields(data: object) -> list[ApiErrorField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in _fields_type_0:
                    fields_type_0_item = ApiErrorField.from_dict(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApiErrorField] | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        api_error_detail = cls(
            code=code,
            message=message,
            request_id=request_id,
            retryable=retryable,
            param=param,
            fields=fields,
        )

        api_error_detail.additional_properties = d
        return api_error_detail

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
