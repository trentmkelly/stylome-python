"""Deterministic compatibility aliases and credential-safe client repr."""
import sys
from pathlib import Path

root = Path(sys.argv[1])
for name, target in (("public_score_12", "api_score_12"), ("legacy_score_response", "api_legacy_score")):
    alias, original = ("PublicScore12", "ApiScore12") if name == "public_score_12" else ("LegacyScoreResponse", "ApiLegacyScore")
    (root / "models" / f"{name}.py").write_text(f"from .{target} import {original} as {alias}\n\n__all__ = [\"{alias}\"]\n")
with (root / "models/__init__.py").open("a") as f:
    f.write("\nfrom .public_score_12 import PublicScore12 as PublicScore12\nfrom .legacy_score_response import LegacyScoreResponse as LegacyScoreResponse\n")
for old, new in (("authenticated_score_api_v1_score_post", "score_text"), ("public_models_api_v1_models_get", "list_models")):
    (root / "api/default" / f"{old}.py").write_text(
        f'"""Compatibility import; new integrations should import {new}."""\n'
        f"from .{new} import asyncio, asyncio_detailed, sync, sync_detailed\n\n"
        '__all__ = ["asyncio", "asyncio_detailed", "sync", "sync_detailed"]\n'
    )
p = root / "client.py"
s = p.read_text()
assert s.count("    token: str\n") == 1
s = s.replace("    token: str\n", "    token: str = field(repr=False)\n")
for alias in ("headers", "cookies", "httpx_args"):
    before = f'field(factory=dict, kw_only=True, alias="{alias}")'
    assert s.count(before) == 2
    s = s.replace(before, f'field(factory=dict, kw_only=True, alias="{alias}", repr=False)')
p.write_text(s)
