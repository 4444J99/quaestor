from unittest.mock import patch
import pytest

from conftest import load_fixture
from discover.runner import DiscoveryRunner


def _runner(tmp_path):
    return DiscoveryRunner(atoms_dir=tmp_path / "atoms", polite_delay=0, sleep=lambda _s: None)


def _dispatch_fetch():
    grants = load_fixture("grants_gov_search2.json")
    propub = load_fixture("propublica_search.json")

    def _fetch(url, *, payload=None, headers=None):
        if "api.grants.gov" in url:
            return grants
        if "propublica.org" in url:
            return propub
        raise AssertionError(f"unexpected url {url}")

    return _fetch


MIXED_STORE_LINES = [
    "",
    "   ",
    "{invalid json line",
    "null",
    "123",
    "45.67",
    "true",
    "false",
    "[1, 2, 3]",
    '"just a string"',
    '{"title": "Missing ID"}',
    '{"id": ""}',
    '{"id": 999}',
    '{"id": true}',
    '{"id": ["unhashable", "list"]}',
    '{"id": {"unhashable": "dict"}}',
    '{"id": "valid-id-1", "title": "Grant 1"}',
    '{"id": "valid-id-2", "title": "Grant 2"}',
    '{"id": "valid-id-1", "title": "Grant 1 Duplicate"}',
]


def test_seen_ids_validation_mixed_records(tmp_path):
    r = _runner(tmp_path)
    store_file = r.store_path
    store_file.parent.mkdir(parents=True, exist_ok=True)
    initial_content = "\n".join(MIXED_STORE_LINES) + "\n"
    store_file.write_text(initial_content, encoding="utf-8")

    # _load_seen_ids should extract only the valid string IDs without crashing.
    seen = r._load_seen_ids()
    assert seen == {"valid-id-1", "valid-id-2"}

    # Running discovery should not crash and should append new unseen atoms.
    summary = r.run(fetch=_dispatch_fetch())
    assert summary["new_atoms"] == 4  # 2 grants.gov + 2 propublica (none matched valid-id-1/2)

    # Check store content: initial prefix is preserved byte-for-byte.
    current_content = store_file.read_text(encoding="utf-8")
    assert current_content.startswith(initial_content)
    new_lines = current_content[len(initial_content) :].strip().splitlines()
    assert len(new_lines) == 4


def test_seen_ids_prevents_duplicate_append(tmp_path):
    r = _runner(tmp_path)
    store_file = r.store_path
    store_file.parent.mkdir(parents=True, exist_ok=True)

    # In fixture grants_gov_search2.json, atom IDs are "grants.gov:358126" and "grants.gov:349900".
    # Seed the store with "grants.gov:358126" along with invalid record lines.
    lines = [
        "null",
        '{"id": "grants.gov:358126", "title": "Existing Grant"}',
        '{"id": 12345}',
    ]
    initial_content = "\n".join(lines) + "\n"
    store_file.write_text(initial_content, encoding="utf-8")

    summary = r.run(sources=["grants.gov"], fetch=_dispatch_fetch())
    # Should only add 1 new atom ("grants.gov:349900")
    assert summary["new_atoms"] == 1
    assert summary["per_source"]["grants.gov"] == 1

    current_content = store_file.read_text(encoding="utf-8")
    assert current_content.startswith(initial_content)


def test_store_read_failure_raises(tmp_path):
    r = _runner(tmp_path)
    store_file = r.store_path
    store_file.parent.mkdir(parents=True, exist_ok=True)
    store_file.write_text('{"id": "valid-1"}\n', encoding="utf-8")

    def mock_read_text(*args, **kwargs):
        raise PermissionError("Permission denied")

    with patch.object(type(store_file), "read_text", side_effect=mock_read_text):
        with pytest.raises(PermissionError, match="Permission denied"):
            r._load_seen_ids()
