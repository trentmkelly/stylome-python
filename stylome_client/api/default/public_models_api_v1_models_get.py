"""Compatibility import; new integrations should import list_models."""
from .list_models import asyncio, asyncio_detailed, sync, sync_detailed

__all__ = ["asyncio", "asyncio_detailed", "sync", "sync_detailed"]
