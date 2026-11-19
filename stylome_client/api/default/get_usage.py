import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error_response import ApiErrorResponse
from ...models.api_usage import ApiUsage
from ...models.get_usage_group_by import GetUsageGroupBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    group_by: GetUsageGroupBy | Unset = GetUsageGroupBy.DAY,
    model: None | str | Unset = UNSET,
    key: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start: None | str | Unset
    if isinstance(start, Unset):
        json_start = UNSET
    elif isinstance(start, datetime.datetime):
        json_start = start.isoformat()
    else:
        json_start = start
    params["start"] = json_start

    json_end: None | str | Unset
    if isinstance(end, Unset):
        json_end = UNSET
    elif isinstance(end, datetime.datetime):
        json_end = end.isoformat()
    else:
        json_end = end
    params["end"] = json_end

    json_group_by: str | Unset = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = group_by.value

    params["group_by"] = json_group_by

    json_model: None | str | Unset
    if isinstance(model, Unset):
        json_model = UNSET
    else:
        json_model = model
    params["model"] = json_model

    json_key: None | str | Unset
    if isinstance(key, Unset):
        json_key = UNSET
    else:
        json_key = key
    params["key"] = json_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiErrorResponse | ApiUsage | None:
    if response.status_code == 200:
        response_200 = ApiUsage.from_dict(response.json())

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
) -> Response[ApiErrorResponse | ApiUsage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    group_by: GetUsageGroupBy | Unset = GetUsageGroupBy.DAY,
    model: None | str | Unset = UNSET,
    key: None | str | Unset = UNSET,
) -> Response[ApiErrorResponse | ApiUsage]:
    """Developer Usage

    Args:
        start (datetime.datetime | None | Unset): Inclusive UTC timestamp; timezone required.
            Default: seven days before end.
        end (datetime.datetime | None | Unset): Exclusive UTC timestamp; timezone required.
            Default: now.
        group_by (GetUsageGroupBy | Unset):  Default: GetUsageGroupBy.DAY.
        model (None | str | Unset): Optional model ID filter; retired IDs are accepted for
            history.
        key (None | str | Unset): Optional public key ID; never send a secret key here.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorResponse | ApiUsage]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        group_by=group_by,
        model=model,
        key=key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    group_by: GetUsageGroupBy | Unset = GetUsageGroupBy.DAY,
    model: None | str | Unset = UNSET,
    key: None | str | Unset = UNSET,
) -> ApiErrorResponse | ApiUsage | None:
    """Developer Usage

    Args:
        start (datetime.datetime | None | Unset): Inclusive UTC timestamp; timezone required.
            Default: seven days before end.
        end (datetime.datetime | None | Unset): Exclusive UTC timestamp; timezone required.
            Default: now.
        group_by (GetUsageGroupBy | Unset):  Default: GetUsageGroupBy.DAY.
        model (None | str | Unset): Optional model ID filter; retired IDs are accepted for
            history.
        key (None | str | Unset): Optional public key ID; never send a secret key here.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorResponse | ApiUsage
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        group_by=group_by,
        model=model,
        key=key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    group_by: GetUsageGroupBy | Unset = GetUsageGroupBy.DAY,
    model: None | str | Unset = UNSET,
    key: None | str | Unset = UNSET,
) -> Response[ApiErrorResponse | ApiUsage]:
    """Developer Usage

    Args:
        start (datetime.datetime | None | Unset): Inclusive UTC timestamp; timezone required.
            Default: seven days before end.
        end (datetime.datetime | None | Unset): Exclusive UTC timestamp; timezone required.
            Default: now.
        group_by (GetUsageGroupBy | Unset):  Default: GetUsageGroupBy.DAY.
        model (None | str | Unset): Optional model ID filter; retired IDs are accepted for
            history.
        key (None | str | Unset): Optional public key ID; never send a secret key here.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiErrorResponse | ApiUsage]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        group_by=group_by,
        model=model,
        key=key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime | None | Unset = UNSET,
    end: datetime.datetime | None | Unset = UNSET,
    group_by: GetUsageGroupBy | Unset = GetUsageGroupBy.DAY,
    model: None | str | Unset = UNSET,
    key: None | str | Unset = UNSET,
) -> ApiErrorResponse | ApiUsage | None:
    """Developer Usage

    Args:
        start (datetime.datetime | None | Unset): Inclusive UTC timestamp; timezone required.
            Default: seven days before end.
        end (datetime.datetime | None | Unset): Exclusive UTC timestamp; timezone required.
            Default: now.
        group_by (GetUsageGroupBy | Unset):  Default: GetUsageGroupBy.DAY.
        model (None | str | Unset): Optional model ID filter; retired IDs are accepted for
            history.
        key (None | str | Unset): Optional public key ID; never send a secret key here.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiErrorResponse | ApiUsage
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            group_by=group_by,
            model=model,
            key=key,
        )
    ).parsed
