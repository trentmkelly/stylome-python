from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.api_legacy_score import ApiLegacyScore
from ...models.api_score_12 import ApiScore12
from ...models.api_score_request import ApiScoreRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ApiScoreRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/score",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiErrorResponse | ApiLegacyScore | ApiScore12 | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> ApiLegacyScore | ApiScore12:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ApiScore12.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ApiLegacyScore.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = ApiErrorResponse.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = ApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ApiErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ApiErrorResponse.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ApiErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ApiErrorResponse.from_dict(response.json())

        return response_500

    if response.status_code == 502:
        response_502 = ApiErrorResponse.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = ApiErrorResponse.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = ApiErrorResponse.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiErrorResponse | ApiLegacyScore | ApiScore12]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiScoreRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiErrorResponse | ApiLegacyScore | ApiScore12]:
    """Authenticated Score

    Args:
        idempotency_key (str | Unset): Standard-retention keys only. Project-wide, case-sensitive
            opaque key, 1–255 characters. Same text/model/operating point replays for 24 hours;
            different input returns 409. Replays consume the request-rate limit.
        body (ApiScoreRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorResponse | ApiLegacyScore | ApiScore12]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ApiScoreRequest,
    idempotency_key: str | Unset = UNSET,
) -> ApiErrorResponse | ApiLegacyScore | ApiScore12 | None:
    """Authenticated Score

    Args:
        idempotency_key (str | Unset): Standard-retention keys only. Project-wide, case-sensitive
            opaque key, 1–255 characters. Same text/model/operating point replays for 24 hours;
            different input returns 409. Replays consume the request-rate limit.
        body (ApiScoreRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorResponse | ApiLegacyScore | ApiScore12
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ApiScoreRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[ApiErrorResponse | ApiLegacyScore | ApiScore12]:
    """Authenticated Score

    Args:
        idempotency_key (str | Unset): Standard-retention keys only. Project-wide, case-sensitive
            opaque key, 1–255 characters. Same text/model/operating point replays for 24 hours;
            different input returns 409. Replays consume the request-rate limit.
        body (ApiScoreRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorResponse | ApiLegacyScore | ApiScore12]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ApiScoreRequest,
    idempotency_key: str | Unset = UNSET,
) -> ApiErrorResponse | ApiLegacyScore | ApiScore12 | None:
    """Authenticated Score

    Args:
        idempotency_key (str | Unset): Standard-retention keys only. Project-wide, case-sensitive
            opaque key, 1–255 characters. Same text/model/operating point replays for 24 hours;
            different input returns 409. Replays consume the request-rate limit.
        body (ApiScoreRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorResponse | ApiLegacyScore | ApiScore12
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
