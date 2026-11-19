from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.api_score_12_confidence import ApiScore12Confidence
from ..models.api_score_12_label import ApiScore12Label
from ..models.api_score_12_operating_point import ApiScore12OperatingPoint
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_receipt_capability import PublicReceiptCapability
    from ..models.score_usage import ScoreUsage


T = TypeVar("T", bound="ApiScore12")


@_attrs_define
class ApiScore12:
    """
    Example:
        {'confidence': 'medium', 'content_hash': '0000000000000000000000000000000000000000000000000000000000000000',
            'created_at': '2026-09-18T12:00:00Z', 'evaluation_version': 'eval_12_001', 'id': 'scan_0123456789ab', 'label':
            'ai_edited', 'mock': False, 'model_version': 'stylome-1.2-large', 'operating_point': '0.01%',
            'response_version': 'stylome-public-v2'}

    Attributes:
        id (str):
        label (ApiScore12Label):
        confidence (ApiScore12Confidence):
        content_hash (str):
        model_version (Literal['stylome-1.2-large']):
        created_at (datetime.datetime):
        operating_point (ApiScore12OperatingPoint):
        evaluation_version (str):
        usage (None | ScoreUsage): Committed normalized-character usage and cost; null only for a replay from before
            prepaid billing.
        mock (bool | Unset):  Default: False.
        response_version (Literal['stylome-public-v2'] | Unset):  Default: 'stylome-public-v2'.
        receipt (None | PublicReceiptCapability | Unset):
    """

    id: str
    label: ApiScore12Label
    confidence: ApiScore12Confidence
    content_hash: str
    model_version: Literal["stylome-1.2-large"]
    created_at: datetime.datetime
    operating_point: ApiScore12OperatingPoint
    evaluation_version: str
    usage: None | ScoreUsage
    mock: bool | Unset = False
    response_version: Literal["stylome-public-v2"] | Unset = "stylome-public-v2"
    receipt: None | PublicReceiptCapability | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.public_receipt_capability import PublicReceiptCapability
        from ..models.score_usage import ScoreUsage

        id = self.id

        label = self.label.value

        confidence = self.confidence.value

        content_hash = self.content_hash

        model_version = self.model_version

        created_at = self.created_at.isoformat()

        operating_point = self.operating_point.value

        evaluation_version = self.evaluation_version

        usage: dict[str, Any] | None
        if isinstance(self.usage, ScoreUsage):
            usage = self.usage.to_dict()
        else:
            usage = self.usage

        mock = self.mock

        response_version = self.response_version

        receipt: dict[str, Any] | None | Unset
        if isinstance(self.receipt, Unset):
            receipt = UNSET
        elif isinstance(self.receipt, PublicReceiptCapability):
            receipt = self.receipt.to_dict()
        else:
            receipt = self.receipt

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "label": label,
                "confidence": confidence,
                "content_hash": content_hash,
                "model_version": model_version,
                "created_at": created_at,
                "operating_point": operating_point,
                "evaluation_version": evaluation_version,
                "usage": usage,
            }
        )
        if mock is not UNSET:
            field_dict["mock"] = mock
        if response_version is not UNSET:
            field_dict["response_version"] = response_version
        if receipt is not UNSET:
            field_dict["receipt"] = receipt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_receipt_capability import PublicReceiptCapability
        from ..models.score_usage import ScoreUsage

        d = dict(src_dict)
        id = d.pop("id")

        label = ApiScore12Label(d.pop("label"))

        confidence = ApiScore12Confidence(d.pop("confidence"))

        content_hash = d.pop("content_hash")

        model_version = cast(Literal["stylome-1.2-large"], d.pop("model_version"))
        if model_version != "stylome-1.2-large":
            raise ValueError(f"model_version must match const 'stylome-1.2-large', got '{model_version}'")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        operating_point = ApiScore12OperatingPoint(d.pop("operating_point"))

        evaluation_version = d.pop("evaluation_version")

        def _parse_usage(data: object) -> None | ScoreUsage:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_type_0 = ScoreUsage.from_dict(data)

                return usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ScoreUsage, data)

        usage = _parse_usage(d.pop("usage"))

        mock = d.pop("mock", UNSET)

        response_version = cast(Literal["stylome-public-v2"] | Unset, d.pop("response_version", UNSET))
        if response_version != "stylome-public-v2" and not isinstance(response_version, Unset):
            raise ValueError(f"response_version must match const 'stylome-public-v2', got '{response_version}'")

        def _parse_receipt(data: object) -> None | PublicReceiptCapability | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                receipt_type_0 = PublicReceiptCapability.from_dict(data)

                return receipt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublicReceiptCapability | Unset, data)

        receipt = _parse_receipt(d.pop("receipt", UNSET))

        api_score_12 = cls(
            id=id,
            label=label,
            confidence=confidence,
            content_hash=content_hash,
            model_version=model_version,
            created_at=created_at,
            operating_point=operating_point,
            evaluation_version=evaluation_version,
            usage=usage,
            mock=mock,
            response_version=response_version,
            receipt=receipt,
        )

        return api_score_12
