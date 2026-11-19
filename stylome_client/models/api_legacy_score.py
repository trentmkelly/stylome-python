from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_legacy_score_confidence_type_0 import ApiLegacyScoreConfidenceType0
from ..models.verdict import Verdict
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_legacy_score_confidence_evidence_type_0 import ApiLegacyScoreConfidenceEvidenceType0
    from ..models.api_legacy_score_knn_decision_type_0 import ApiLegacyScoreKnnDecisionType0
    from ..models.api_legacy_score_operating_points_type_0 import ApiLegacyScoreOperatingPointsType0
    from ..models.api_legacy_score_probabilities_type_0 import ApiLegacyScoreProbabilitiesType0
    from ..models.api_legacy_score_uncertainty_type_0 import ApiLegacyScoreUncertaintyType0
    from ..models.receipt_capability import ReceiptCapability
    from ..models.score_usage import ScoreUsage


T = TypeVar("T", bound="ApiLegacyScore")


@_attrs_define
class ApiLegacyScore:
    """Stylome 1.0 Large's existing score/probability response. No 1.2 confidence is computed.

    Example:
        {'content_hash': '0000000000000000000000000000000000000000000000000000000000000000', 'created_at':
            '2026-09-20T12:00:00Z', 'detector_score': -2.0, 'id': 'scan_example', 'label': 'human_written', 'margin': -10.0,
            'model_version': 'stylome-1.0-large', 'probabilities': {'ai_edited': 0.1, 'ai_generated': 0.1, 'human_written':
            0.8}, 'threshold': 8.0, 'verdict': 'human_typical'}

    Attributes:
        id (str):
        verdict (Verdict):
        content_hash (str):
        model_version (Literal['stylome-1.0-large']):
        created_at (datetime.datetime):
        detector_score (float):
        threshold (float):
        margin (float):
        label (str):
        usage (None | ScoreUsage): Committed normalized-character usage and cost; null only for a replay from before
            prepaid billing.
        mock (bool | Unset):  Default: False.
        score (float | None | Unset): Legacy 1.0 result only; omitted for 1.2.
        probabilities (ApiLegacyScoreProbabilitiesType0 | None | Unset): Legacy 1.0 probabilities only; omitted for 1.2.
        binary_label (None | str | Unset):
        operating_point (None | str | Unset):
        operating_points (ApiLegacyScoreOperatingPointsType0 | None | Unset):
        confidence (ApiLegacyScoreConfidenceType0 | None | Unset): 1.2 relative KNN support for the returned class,
            based on neighbor agreement, proximity, and decision margin against calibration examples. Not a probability of
            correctness. Not provided for 1.0.
        confidence_evidence (ApiLegacyScoreConfidenceEvidenceType0 | None | Unset):
        classification_contract (None | str | Unset):
        confidence_contract (None | str | Unset):
        confidence_artifact_sha256 (None | str | Unset):
        uncertainty (ApiLegacyScoreUncertaintyType0 | None | Unset):
        knn_decision (ApiLegacyScoreKnnDecisionType0 | None | Unset):
        scoring_contract (None | str | Unset):
        model_revision (None | str | Unset):
        receipt (None | ReceiptCapability | Unset):
    """

    id: str
    verdict: Verdict
    content_hash: str
    model_version: Literal["stylome-1.0-large"]
    created_at: datetime.datetime
    detector_score: float
    threshold: float
    margin: float
    label: str
    usage: None | ScoreUsage
    mock: bool | Unset = False
    score: float | None | Unset = UNSET
    probabilities: ApiLegacyScoreProbabilitiesType0 | None | Unset = UNSET
    binary_label: None | str | Unset = UNSET
    operating_point: None | str | Unset = UNSET
    operating_points: ApiLegacyScoreOperatingPointsType0 | None | Unset = UNSET
    confidence: ApiLegacyScoreConfidenceType0 | None | Unset = UNSET
    confidence_evidence: ApiLegacyScoreConfidenceEvidenceType0 | None | Unset = UNSET
    classification_contract: None | str | Unset = UNSET
    confidence_contract: None | str | Unset = UNSET
    confidence_artifact_sha256: None | str | Unset = UNSET
    uncertainty: ApiLegacyScoreUncertaintyType0 | None | Unset = UNSET
    knn_decision: ApiLegacyScoreKnnDecisionType0 | None | Unset = UNSET
    scoring_contract: None | str | Unset = UNSET
    model_revision: None | str | Unset = UNSET
    receipt: None | ReceiptCapability | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_legacy_score_confidence_evidence_type_0 import ApiLegacyScoreConfidenceEvidenceType0
        from ..models.api_legacy_score_knn_decision_type_0 import ApiLegacyScoreKnnDecisionType0
        from ..models.api_legacy_score_operating_points_type_0 import ApiLegacyScoreOperatingPointsType0
        from ..models.api_legacy_score_probabilities_type_0 import ApiLegacyScoreProbabilitiesType0
        from ..models.api_legacy_score_uncertainty_type_0 import ApiLegacyScoreUncertaintyType0
        from ..models.receipt_capability import ReceiptCapability
        from ..models.score_usage import ScoreUsage

        id = self.id

        verdict = self.verdict.value

        content_hash = self.content_hash

        model_version = self.model_version

        created_at = self.created_at.isoformat()

        detector_score = self.detector_score

        threshold = self.threshold

        margin = self.margin

        label = self.label

        usage: dict[str, Any] | None
        if isinstance(self.usage, ScoreUsage):
            usage = self.usage.to_dict()
        else:
            usage = self.usage

        mock = self.mock

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        probabilities: dict[str, Any] | None | Unset
        if isinstance(self.probabilities, Unset):
            probabilities = UNSET
        elif isinstance(self.probabilities, ApiLegacyScoreProbabilitiesType0):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities

        binary_label: None | str | Unset
        if isinstance(self.binary_label, Unset):
            binary_label = UNSET
        else:
            binary_label = self.binary_label

        operating_point: None | str | Unset
        if isinstance(self.operating_point, Unset):
            operating_point = UNSET
        else:
            operating_point = self.operating_point

        operating_points: dict[str, Any] | None | Unset
        if isinstance(self.operating_points, Unset):
            operating_points = UNSET
        elif isinstance(self.operating_points, ApiLegacyScoreOperatingPointsType0):
            operating_points = self.operating_points.to_dict()
        else:
            operating_points = self.operating_points

        confidence: None | str | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        elif isinstance(self.confidence, ApiLegacyScoreConfidenceType0):
            confidence = self.confidence.value
        else:
            confidence = self.confidence

        confidence_evidence: dict[str, Any] | None | Unset
        if isinstance(self.confidence_evidence, Unset):
            confidence_evidence = UNSET
        elif isinstance(self.confidence_evidence, ApiLegacyScoreConfidenceEvidenceType0):
            confidence_evidence = self.confidence_evidence.to_dict()
        else:
            confidence_evidence = self.confidence_evidence

        classification_contract: None | str | Unset
        if isinstance(self.classification_contract, Unset):
            classification_contract = UNSET
        else:
            classification_contract = self.classification_contract

        confidence_contract: None | str | Unset
        if isinstance(self.confidence_contract, Unset):
            confidence_contract = UNSET
        else:
            confidence_contract = self.confidence_contract

        confidence_artifact_sha256: None | str | Unset
        if isinstance(self.confidence_artifact_sha256, Unset):
            confidence_artifact_sha256 = UNSET
        else:
            confidence_artifact_sha256 = self.confidence_artifact_sha256

        uncertainty: dict[str, Any] | None | Unset
        if isinstance(self.uncertainty, Unset):
            uncertainty = UNSET
        elif isinstance(self.uncertainty, ApiLegacyScoreUncertaintyType0):
            uncertainty = self.uncertainty.to_dict()
        else:
            uncertainty = self.uncertainty

        knn_decision: dict[str, Any] | None | Unset
        if isinstance(self.knn_decision, Unset):
            knn_decision = UNSET
        elif isinstance(self.knn_decision, ApiLegacyScoreKnnDecisionType0):
            knn_decision = self.knn_decision.to_dict()
        else:
            knn_decision = self.knn_decision

        scoring_contract: None | str | Unset
        if isinstance(self.scoring_contract, Unset):
            scoring_contract = UNSET
        else:
            scoring_contract = self.scoring_contract

        model_revision: None | str | Unset
        if isinstance(self.model_revision, Unset):
            model_revision = UNSET
        else:
            model_revision = self.model_revision

        receipt: dict[str, Any] | None | Unset
        if isinstance(self.receipt, Unset):
            receipt = UNSET
        elif isinstance(self.receipt, ReceiptCapability):
            receipt = self.receipt.to_dict()
        else:
            receipt = self.receipt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "verdict": verdict,
                "content_hash": content_hash,
                "model_version": model_version,
                "created_at": created_at,
                "detector_score": detector_score,
                "threshold": threshold,
                "margin": margin,
                "label": label,
                "usage": usage,
            }
        )
        if mock is not UNSET:
            field_dict["mock"] = mock
        if score is not UNSET:
            field_dict["score"] = score
        if probabilities is not UNSET:
            field_dict["probabilities"] = probabilities
        if binary_label is not UNSET:
            field_dict["binary_label"] = binary_label
        if operating_point is not UNSET:
            field_dict["operating_point"] = operating_point
        if operating_points is not UNSET:
            field_dict["operating_points"] = operating_points
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if confidence_evidence is not UNSET:
            field_dict["confidence_evidence"] = confidence_evidence
        if classification_contract is not UNSET:
            field_dict["classification_contract"] = classification_contract
        if confidence_contract is not UNSET:
            field_dict["confidence_contract"] = confidence_contract
        if confidence_artifact_sha256 is not UNSET:
            field_dict["confidence_artifact_sha256"] = confidence_artifact_sha256
        if uncertainty is not UNSET:
            field_dict["uncertainty"] = uncertainty
        if knn_decision is not UNSET:
            field_dict["knn_decision"] = knn_decision
        if scoring_contract is not UNSET:
            field_dict["scoring_contract"] = scoring_contract
        if model_revision is not UNSET:
            field_dict["model_revision"] = model_revision
        if receipt is not UNSET:
            field_dict["receipt"] = receipt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_legacy_score_confidence_evidence_type_0 import ApiLegacyScoreConfidenceEvidenceType0
        from ..models.api_legacy_score_knn_decision_type_0 import ApiLegacyScoreKnnDecisionType0
        from ..models.api_legacy_score_operating_points_type_0 import ApiLegacyScoreOperatingPointsType0
        from ..models.api_legacy_score_probabilities_type_0 import ApiLegacyScoreProbabilitiesType0
        from ..models.api_legacy_score_uncertainty_type_0 import ApiLegacyScoreUncertaintyType0
        from ..models.receipt_capability import ReceiptCapability
        from ..models.score_usage import ScoreUsage

        d = dict(src_dict)
        id = d.pop("id")

        verdict = Verdict(d.pop("verdict"))

        content_hash = d.pop("content_hash")

        model_version = cast(Literal["stylome-1.0-large"], d.pop("model_version"))
        if model_version != "stylome-1.0-large":
            raise ValueError(f"model_version must match const 'stylome-1.0-large', got '{model_version}'")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        detector_score = d.pop("detector_score")

        threshold = d.pop("threshold")

        margin = d.pop("margin")

        label = d.pop("label")

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

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_probabilities(data: object) -> ApiLegacyScoreProbabilitiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = ApiLegacyScoreProbabilitiesType0.from_dict(data)

                return probabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiLegacyScoreProbabilitiesType0 | None | Unset, data)

        probabilities = _parse_probabilities(d.pop("probabilities", UNSET))

        def _parse_binary_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        binary_label = _parse_binary_label(d.pop("binary_label", UNSET))

        def _parse_operating_point(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operating_point = _parse_operating_point(d.pop("operating_point", UNSET))

        def _parse_operating_points(data: object) -> ApiLegacyScoreOperatingPointsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operating_points_type_0 = ApiLegacyScoreOperatingPointsType0.from_dict(data)

                return operating_points_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiLegacyScoreOperatingPointsType0 | None | Unset, data)

        operating_points = _parse_operating_points(d.pop("operating_points", UNSET))

        def _parse_confidence(data: object) -> ApiLegacyScoreConfidenceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confidence_type_0 = ApiLegacyScoreConfidenceType0(data)

                return confidence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiLegacyScoreConfidenceType0 | None | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_confidence_evidence(data: object) -> ApiLegacyScoreConfidenceEvidenceType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                confidence_evidence_type_0 = ApiLegacyScoreConfidenceEvidenceType0.from_dict(data)

                return confidence_evidence_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiLegacyScoreConfidenceEvidenceType0 | None | Unset, data)

        confidence_evidence = _parse_confidence_evidence(d.pop("confidence_evidence", UNSET))

        def _parse_classification_contract(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        classification_contract = _parse_classification_contract(d.pop("classification_contract", UNSET))

        def _parse_confidence_contract(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confidence_contract = _parse_confidence_contract(d.pop("confidence_contract", UNSET))

        def _parse_confidence_artifact_sha256(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confidence_artifact_sha256 = _parse_confidence_artifact_sha256(d.pop("confidence_artifact_sha256", UNSET))

        def _parse_uncertainty(data: object) -> ApiLegacyScoreUncertaintyType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                uncertainty_type_0 = ApiLegacyScoreUncertaintyType0.from_dict(data)

                return uncertainty_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiLegacyScoreUncertaintyType0 | None | Unset, data)

        uncertainty = _parse_uncertainty(d.pop("uncertainty", UNSET))

        def _parse_knn_decision(data: object) -> ApiLegacyScoreKnnDecisionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                knn_decision_type_0 = ApiLegacyScoreKnnDecisionType0.from_dict(data)

                return knn_decision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiLegacyScoreKnnDecisionType0 | None | Unset, data)

        knn_decision = _parse_knn_decision(d.pop("knn_decision", UNSET))

        def _parse_scoring_contract(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scoring_contract = _parse_scoring_contract(d.pop("scoring_contract", UNSET))

        def _parse_model_revision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_revision = _parse_model_revision(d.pop("model_revision", UNSET))

        def _parse_receipt(data: object) -> None | ReceiptCapability | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                receipt_type_0 = ReceiptCapability.from_dict(data)

                return receipt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReceiptCapability | Unset, data)

        receipt = _parse_receipt(d.pop("receipt", UNSET))

        api_legacy_score = cls(
            id=id,
            verdict=verdict,
            content_hash=content_hash,
            model_version=model_version,
            created_at=created_at,
            detector_score=detector_score,
            threshold=threshold,
            margin=margin,
            label=label,
            usage=usage,
            mock=mock,
            score=score,
            probabilities=probabilities,
            binary_label=binary_label,
            operating_point=operating_point,
            operating_points=operating_points,
            confidence=confidence,
            confidence_evidence=confidence_evidence,
            classification_contract=classification_contract,
            confidence_contract=confidence_contract,
            confidence_artifact_sha256=confidence_artifact_sha256,
            uncertainty=uncertainty,
            knn_decision=knn_decision,
            scoring_contract=scoring_contract,
            model_revision=model_revision,
            receipt=receipt,
        )

        api_legacy_score.additional_properties = d
        return api_legacy_score

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
