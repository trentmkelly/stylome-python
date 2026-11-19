# Stylome Python SDK

Typed synchronous and asynchronous client for the [Stylome API](https://stylome.io/api/docs), generated from its public OpenAPI specification. Python 3.11+.

```bash
pip install "stylome-client @ git+https://github.com/trentmkelly/stylome-python.git@v0.3.0"
```

Set `STYLOME_API_KEY` to your developer API key:

```python
import os
import httpx
from stylome_client import AuthenticatedClient
from stylome_client.api.default import score_text
from stylome_client.models import ApiScore12, ApiScoreRequest, ApiScoreRequestModel

with AuthenticatedClient(
    base_url="https://stylome.io",
    token=os.environ["STYLOME_API_KEY"],
    timeout=httpx.Timeout(150, connect=10),
    raise_on_unexpected_status=True,
) as client:
    response = score_text.sync_detailed(
        client=client,
        body=ApiScoreRequest(text=("This is an artificial SDK example for checking service integration. "
                                  "The library committee met on Tuesday to discuss the reading room. "
                                  "The members reviewed repair estimates and arranged another meeting "
                                  "to compare the costs before making a decision."),
                             model=ApiScoreRequestModel.STYLOME_1_2_LARGE),
    )
    if response.status_code == 200 and isinstance(response.parsed, ApiScore12):
        print(response.parsed.label.value, response.parsed.confidence.value)
    else:
        raise RuntimeError(f"Stylome returned HTTP {response.status_code}")
```

Replace the example text with a complete document. For async calls, use `async with` and `await score_text.asyncio_detailed(...)`. The package also supports model discovery, key identity, limits, usage, status, and the legacy 1.0 model.

For 1.2, set `operating_point=ApiScoreRequestOperatingPointType0("0.1%")` on the request to use the other point (import the enum from `stylome_client.models`). The default is `0.01%`. These are calibration FPR targets, not guarantees on your documents; confidence is relative support, not a probability of correctness.

Scoring errors are returned as `ApiErrorResponse`; inspect `status_code` and `parsed`. Unexpected statuses can raise `UnexpectedStatus`; transport failures raise HTTPX exceptions. Requests are not retried automatically. Use `idempotency_key=` for safe replay with standard-retention keys; zero-content keys do not support it. Avoid logging credentials, raw responses, or receipt share tokens. Input constraints are enforced by the API, not the generated dataclasses.

## Development

```bash
uv sync --extra dev
uv run pytest -q
bash scripts/generate.sh
```

Generation uses the committed public spec and pinned `openapi-python-client==0.29.0`. Update it explicitly with `python scripts/update_openapi.py`. Change the spec/config or deterministic post-processing, not generated files. CI checks regeneration, builds, and Python 3.11–3.14. MIT licensed. GitHub installation is supported; no PyPI release is required.
