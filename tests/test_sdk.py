"""Offline checks for every public operation, without private server imports."""
import asyncio
import importlib
import json
from datetime import UTC, datetime
from pathlib import Path

import httpx
import pytest

from stylome_client import AuthenticatedClient, Client
from stylome_client.api.default import score_text
from stylome_client.errors import UnexpectedStatus
from stylome_client.models import ApiErrorResponse, ApiLegacyScore, ApiScore12, ApiScoreRequest, ApiScoreRequestModel
from stylome_client.types import UNSET

SPEC = json.loads(Path(__file__).resolve().parents[1].joinpath('openapi/openapi.json').read_text())
TOKEN = 'offline-fixture-not-a-live-key'
DATE = '2026-01-01T00:00:00+00:00'
BODY = ApiScoreRequest(text='A synthetic integration fixture. ' * 12, model=ApiScoreRequestModel.STYLOME_1_2_LARGE)
MODULES = {
    '/api/v1/models': 'list_models', '/api/v1/score': 'score_text',
    '/api/v1/key': 'get_key', '/api/v1/limits': 'get_limits',
    '/api/v1/usage': 'get_usage', '/api/v1/status': 'get_status',
}


def example(schema, field=''):
    if '$ref' in schema:
        return example(SPEC['components']['schemas'][schema['$ref'].split('/')[-1]], field)
    if 'anyOf' in schema or 'oneOf' in schema:
        return example(next(s for s in schema.get('anyOf', schema.get('oneOf')) if s.get('type') != 'null'), field)
    if 'const' in schema:
        return schema['const']
    if 'enum' in schema:
        return schema['enum'][0]
    kind = schema.get('type')
    if kind == 'object' or 'properties' in schema:
        return {k: example(schema['properties'][k], k) for k in schema.get('required', [])}
    if kind == 'array':
        return []
    if kind == 'boolean':
        return False
    if kind in ('integer', 'number'):
        return 1
    if kind == 'null':
        return None
    if schema.get('format') == 'date-time':
        return DATE
    if field == 'cost_usd' or field.endswith('_usd'):
        return '0.001000'
    return 'fixture'


def response_body(path, status=200):
    operation = next(iter(SPEC['paths'][path].values()))
    schema = operation['responses'][str(status)]['content']['application/json']['schema']
    return example(schema)


def handler_for(path, body, status=200):
    def handle(request):
        assert request.url.path == path
        assert request.headers.get('authorization') == f'Bearer {TOKEN}'
        if path == '/api/v1/score':
            assert json.loads(request.content) == BODY.to_dict()
            assert request.headers['idempotency-key'] == 'offline-replay-key'
        return httpx.Response(status, json=body, headers={'X-Request-ID': 'req_fixture'})
    return handle


def call(path, mode, body, status=200):
    module = importlib.import_module('stylome_client.api.default.' + MODULES[path])
    kwargs = {'body': BODY, 'idempotency_key': 'offline-replay-key'} if path == '/api/v1/score' else {}
    transport = httpx.MockTransport(handler_for(path, body, status))
    if mode == 'sync':
        with AuthenticatedClient(base_url='https://example.invalid', token=TOKEN,
                                 raise_on_unexpected_status=True, httpx_args={'transport': transport}) as client:
            return module.sync_detailed(client=client, **kwargs)
    async def run():
        async with AuthenticatedClient(base_url='https://example.invalid', token=TOKEN,
                                       raise_on_unexpected_status=True, httpx_args={'transport': transport}) as client:
            return await module.asyncio_detailed(client=client, **kwargs)
    return asyncio.run(run())


@pytest.mark.parametrize('path', MODULES)
@pytest.mark.parametrize('mode', ['sync', 'async'])
def test_every_operation_success(path, mode):
    body = response_body(path)
    response = call(path, mode, body)
    assert response.status_code == 200
    assert response.headers['x-request-id'] == 'req_fixture'
    assert response.parsed.to_dict() == body


ERRORS = [(p, int(code)) for p, methods in SPEC['paths'].items()
          for op in methods.values() for code in op['responses'] if code != '200']


@pytest.mark.parametrize('path,status', ERRORS)
@pytest.mark.parametrize('mode', ['sync', 'async'])
def test_all_documented_errors_are_typed(path, status, mode):
    body = response_body(path, status)
    response = call(path, mode, body, status)
    assert response.status_code == status
    if path != '/api/v1/status' or status != 503:
        assert isinstance(response.parsed, ApiErrorResponse)
    assert response.parsed.to_dict() == body


@pytest.mark.parametrize('label', ['human_written', 'ai_edited', 'ai_generated'])
@pytest.mark.parametrize('point', ['0.01%', '0.1%'])
@pytest.mark.parametrize('mode', ['sync', 'async'])
def test_labels_points_and_usage_preserved(label, point, mode):
    body = response_body('/api/v1/score')
    body.update(label=label, operating_point=point)
    result = call('/api/v1/score', mode, body).parsed
    assert isinstance(result, ApiScore12)
    assert result.label.value == label
    assert result.operating_point.value == point
    assert result.usage.cost_usd == body['usage']['cost_usd']
    assert result.to_dict() == body


@pytest.mark.parametrize('mode', ['sync', 'async'])
def test_legacy_format(mode):
    body = example(SPEC['components']['schemas']['ApiLegacyScore'])
    body.update(detector_score=-2.0, threshold=8.0, margin=-10.0,
                probabilities={'human_written': 0.8, 'ai_edited': 0.1, 'ai_generated': 0.1})
    result = call('/api/v1/score', mode, body).parsed
    assert isinstance(result, ApiLegacyScore)
    assert result.to_dict() == body


@pytest.mark.parametrize('mode', ['sync', 'async'])
def test_unknown_status_is_inspectable(mode):
    with pytest.raises(UnexpectedStatus) as exc:
        call('/api/v1/score', mode, {}, 418)
    assert exc.value.status_code == 418


def test_timeout_is_not_retried():
    calls = []
    def fail(request):
        calls.append(request)
        raise httpx.ReadTimeout('offline timeout', request=request)
    with AuthenticatedClient(base_url='https://example.invalid', token=TOKEN,
                             httpx_args={'transport': httpx.MockTransport(fail)}) as client:
        with pytest.raises(httpx.ReadTimeout):
            score_text.sync_detailed(client=client, body=BODY)
    assert len(calls) == 1


def test_credentials_absent_from_client_repr_before_and_after_use():
    client = AuthenticatedClient(base_url='https://example.invalid', token=TOKEN)
    assert TOKEN not in repr(client)
    with client:
        assert client.get_httpx_client().headers['Authorization'] == f'Bearer {TOKEN}'
        assert TOKEN not in repr(client)
    plain = Client(base_url='https://example.invalid', headers={'Authorization': TOKEN}, cookies={'session': TOKEN})
    assert TOKEN not in repr(plain)


def test_unset_and_none_are_different_and_unknown_fields_roundtrip():
    a = ApiScoreRequest(text='fixture', model=ApiScoreRequestModel.STYLOME_1_2_LARGE)
    assert a.operating_point is UNSET and 'operating_point' not in a.to_dict()
    a.operating_point = None
    assert a.to_dict()['operating_point'] is None
    assert ApiScoreRequest.from_dict(a.to_dict()).to_dict() == a.to_dict()
    from stylome_client.models import ApiLimits
    result = ApiLimits.from_dict(response_body('/api/v1/limits'))
    result['future_field'] = {'nested': 1}
    assert ApiLimits.from_dict(result.to_dict()).to_dict() == result.to_dict()


def test_compatibility_imports():
    from stylome_client.api.default import authenticated_score_api_v1_score_post as old
    from stylome_client.models import LegacyScoreResponse, PublicScore12
    assert old.sync_detailed is score_text.sync_detailed
    assert PublicScore12 is ApiScore12 and LegacyScoreResponse is ApiLegacyScore


def test_usage_filters_are_serialized():
    from stylome_client.api.default import get_usage
    from stylome_client.models import GetUsageGroupBy
    observed = []
    def handle(request):
        observed.append(request)
        return httpx.Response(200, json=response_body('/api/v1/usage'))
    with AuthenticatedClient(base_url='https://example.invalid', token=TOKEN,
                             httpx_args={'transport': httpx.MockTransport(handle)}) as client:
        get_usage.sync_detailed(client=client, start=datetime(2026,1,1,tzinfo=UTC),
                               end=datetime(2026,1,2,tzinfo=UTC),
                               group_by=GetUsageGroupBy.KEY, key='0'*16, model='stylome-1.2-large')
    q = observed[0].url.params
    assert q['key'] == '0'*16 and q['group_by'] == 'key' and q['model'] == 'stylome-1.2-large'
    assert '2026-01-01' in q['start']


def test_complete_spec_is_public_developer_api_only():
    assert set(SPEC['paths']) == set(MODULES)
    assert not any('/admin' in path for path in SPEC['paths'])
