"""Shared test helpers: hermetic fetchers that replay canned API JSON."""

from __future__ import annotations

import json
from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def canned_fetch(payload_by_default: dict):
    """Return a fetch(...) that ignores the URL and returns fixed JSON."""

    def _fetch(url, *, payload=None, headers=None):
        return payload_by_default

    return _fetch
