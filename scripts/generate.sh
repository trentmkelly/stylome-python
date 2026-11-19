#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
uv tool run --from openapi-python-client==0.29.0 openapi-python-client generate \
  --path openapi/openapi.json --config openapi/config.yaml \
  --output-path "$work/generated" --overwrite
"${PYTHON:-python3}" scripts/postprocess.py "$work/generated/stylome_client"
uv tool run --from ruff==0.17.6 ruff check --select I --fix "$work/generated/stylome_client/models/__init__.py"
rm -rf stylome_client
cp -R "$work/generated/stylome_client" stylome_client
