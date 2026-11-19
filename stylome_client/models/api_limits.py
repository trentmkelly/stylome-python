from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_limits_retention_mode import ApiLimitsRetentionMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_balance import ApiBalance


T = TypeVar("T", bound="ApiLimits")


@_attrs_define
class ApiLimits:
    """
    Attributes:
        measured_at (datetime.datetime):
        request_limit (int | None):
        remaining_requests (int | None):
        resets_at (datetime.datetime | None):
        rate_limit_exempt (bool):
        idempotency_supported (bool):
        retention_mode (ApiLimitsRetentionMode):
        prepaid (ApiBalance):
        object_ (Literal['api_limits'] | Unset):  Default: 'api_limits'.
        rate_limit_scope (Literal['account'] | Unset):  Default: 'account'.
        window_seconds (int | Unset):  Default: 60.
        request_timeout_seconds (int | Unset):  Default: 110.
        idempotency_lifetime_seconds (int | Unset):  Default: 86400.
    """

    measured_at: datetime.datetime
    request_limit: int | None
    remaining_requests: int | None
    resets_at: datetime.datetime | None
    rate_limit_exempt: bool
    idempotency_supported: bool
    retention_mode: ApiLimitsRetentionMode
    prepaid: ApiBalance
    object_: Literal["api_limits"] | Unset = "api_limits"
    rate_limit_scope: Literal["account"] | Unset = "account"
    window_seconds: int | Unset = 60
    request_timeout_seconds: int | Unset = 110
    idempotency_lifetime_seconds: int | Unset = 86400
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measured_at = self.measured_at.isoformat()

        request_limit: int | None
        request_limit = self.request_limit

        remaining_requests: int | None
        remaining_requests = self.remaining_requests

        resets_at: None | str
        if isinstance(self.resets_at, datetime.datetime):
            resets_at = self.resets_at.isoformat()
        else:
            resets_at = self.resets_at

        rate_limit_exempt = self.rate_limit_exempt

        idempotency_supported = self.idempotency_supported

        retention_mode = self.retention_mode.value

        prepaid = self.prepaid.to_dict()

        object_ = self.object_

        rate_limit_scope = self.rate_limit_scope

        window_seconds = self.window_seconds

        request_timeout_seconds = self.request_timeout_seconds

        idempotency_lifetime_seconds = self.idempotency_lifetime_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "measured_at": measured_at,
                "request_limit": request_limit,
                "remaining_requests": remaining_requests,
                "resets_at": resets_at,
                "rate_limit_exempt": rate_limit_exempt,
                "idempotency_supported": idempotency_supported,
                "retention_mode": retention_mode,
                "prepaid": prepaid,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_
        if rate_limit_scope is not UNSET:
            field_dict["rate_limit_scope"] = rate_limit_scope
        if window_seconds is not UNSET:
            field_dict["window_seconds"] = window_seconds
        if request_timeout_seconds is not UNSET:
            field_dict["request_timeout_seconds"] = request_timeout_seconds
        if idempotency_lifetime_seconds is not UNSET:
            field_dict["idempotency_lifetime_seconds"] = idempotency_lifetime_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_balance import ApiBalance

        d = dict(src_dict)
        measured_at = datetime.datetime.fromisoformat(d.pop("measured_at"))

        def _parse_request_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        request_limit = _parse_request_limit(d.pop("request_limit"))

        def _parse_remaining_requests(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        remaining_requests = _parse_remaining_requests(d.pop("remaining_requests"))

        def _parse_resets_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resets_at_type_0 = datetime.datetime.fromisoformat(data)

                return resets_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resets_at = _parse_resets_at(d.pop("resets_at"))

        rate_limit_exempt = d.pop("rate_limit_exempt")

        idempotency_supported = d.pop("idempotency_supported")

        retention_mode = ApiLimitsRetentionMode(d.pop("retention_mode"))

        prepaid = ApiBalance.from_dict(d.pop("prepaid"))

        object_ = cast(Literal["api_limits"] | Unset, d.pop("object", UNSET))
        if object_ != "api_limits" and not isinstance(object_, Unset):
            raise ValueError(f"object must match const 'api_limits', got '{object_}'")

        rate_limit_scope = cast(Literal["account"] | Unset, d.pop("rate_limit_scope", UNSET))
        if rate_limit_scope != "account" and not isinstance(rate_limit_scope, Unset):
            raise ValueError(f"rate_limit_scope must match const 'account', got '{rate_limit_scope}'")

        window_seconds = d.pop("window_seconds", UNSET)

        request_timeout_seconds = d.pop("request_timeout_seconds", UNSET)

        idempotency_lifetime_seconds = d.pop("idempotency_lifetime_seconds", UNSET)

        api_limits = cls(
            measured_at=measured_at,
            request_limit=request_limit,
            remaining_requests=remaining_requests,
            resets_at=resets_at,
            rate_limit_exempt=rate_limit_exempt,
            idempotency_supported=idempotency_supported,
            retention_mode=retention_mode,
            prepaid=prepaid,
            object_=object_,
            rate_limit_scope=rate_limit_scope,
            window_seconds=window_seconds,
            request_timeout_seconds=request_timeout_seconds,
            idempotency_lifetime_seconds=idempotency_lifetime_seconds,
        )

        api_limits.additional_properties = d
        return api_limits

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
