"""Compatibility import; new integrations should import score_text."""
from .score_text import asyncio, asyncio_detailed, sync, sync_detailed

__all__ = ["asyncio", "asyncio_detailed", "sync", "sync_detailed"]
