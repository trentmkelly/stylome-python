from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.api_score_request_model import ApiScoreRequestModel
from ..models.api_score_request_operating_point_type_0 import ApiScoreRequestOperatingPointType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiScoreRequest")


@_attrs_define
class ApiScoreRequest:
    """
    Attributes:
        text (str): Text to analyze. For stylome-1.2-large, whitespace is collapsed without Unicode compatibility
            normalization; the result must contain 200–10,000 Unicode characters. Inputs are never silently truncated.
        model (ApiScoreRequestModel): Required public model ID. Use stylome-1.2-large for ternary classification, or
            stylome-1.0-large for the 1.0 response contract.
        operating_point (ApiScoreRequestOperatingPointType0 | None | Unset): stylome-1.2-large only. Omission selects
            0.01%; 0.1% is also available. These are calibration false-positive-rate targets, not confidence levels or
            guarantees of the false-positive rate on new data. Omit this field for stylome-1.0-large.
    """

    text: str
    model: ApiScoreRequestModel
    operating_point: ApiScoreRequestOperatingPointType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        model = self.model.value

        operating_point: None | str | Unset
        if isinstance(self.operating_point, Unset):
            operating_point = UNSET
        elif isinstance(self.operating_point, ApiScoreRequestOperatingPointType0):
            operating_point = self.operating_point.value
        else:
            operating_point = self.operating_point

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "text": text,
                "model": model,
            }
        )
        if operating_point is not UNSET:
            field_dict["operating_point"] = operating_point

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        model = ApiScoreRequestModel(d.pop("model"))

        def _parse_operating_point(data: object) -> ApiScoreRequestOperatingPointType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operating_point_type_0 = ApiScoreRequestOperatingPointType0(data)

                return operating_point_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiScoreRequestOperatingPointType0 | None | Unset, data)

        operating_point = _parse_operating_point(d.pop("operating_point", UNSET))

        api_score_request = cls(
            text=text,
            model=model,
            operating_point=operating_point,
        )

        return api_score_request
