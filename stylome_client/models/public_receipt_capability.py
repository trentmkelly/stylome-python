from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicReceiptCapability")


@_attrs_define
class PublicReceiptCapability:
    """
    Attributes:
        id (str):
        share_token (str):
        public_share (bool | Unset):  Default: False.
    """

    id: str
    share_token: str
    public_share: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        share_token = self.share_token

        public_share = self.public_share

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "share_token": share_token,
            }
        )
        if public_share is not UNSET:
            field_dict["public_share"] = public_share

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        share_token = d.pop("share_token")

        public_share = d.pop("public_share", UNSET)

        public_receipt_capability = cls(
            id=id,
            share_token=share_token,
            public_share=public_share,
        )

        return public_receipt_capability
