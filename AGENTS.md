# Stylome Python SDK

This is the canonical public Python SDK. Keep it usable without private Stylome
repositories, model assets, credentials, or server access.

Generate code with `bash scripts/generate.sh`. Edit the public OpenAPI snapshot,
generator config, or deterministic post-processing rather than generated files.
Update the spec only from the public API. Keep generator versions pinned.

Run offline tests, lint, regeneration checks, and wheel/sdist builds before a
release. Test supported Python versions and both HTTPX dependency bounds. Live
scoring is a separate opt-in check; it spends API credit. Never put credentials,
real customer text, private responses, or internal deployment details in Git.
Preserve native labels and exact usage; client tests do not measure accuracy.
