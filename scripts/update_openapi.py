"""Fetch only the public API schema; no credential or private server import."""
import json
from pathlib import Path
from urllib.request import urlopen

with urlopen("https://stylome.io/api/openapi.json", timeout=30) as response:
    spec = json.load(response)
assert spec.get("openapi", "").startswith("3.")
assert all(path.startswith("/api/v1/") for path in spec["paths"])
Path(__file__).resolve().parents[1].joinpath("openapi/openapi.json").write_text(
    json.dumps(spec, indent=2, ensure_ascii=False) + "\n"
)
