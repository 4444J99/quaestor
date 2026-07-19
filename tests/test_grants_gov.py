from conftest import canned_fetch, load_fixture

from discover.sources.grants_gov import GrantsGov, _iso_date


def test_iso_date_normalization():
    assert _iso_date("08/15/2024") == "2024-08-15"
    assert _iso_date("") is None
    assert _iso_date(None) is None
    assert _iso_date("not-a-date") is None


def test_search_maps_hits_to_atoms():
    src = GrantsGov(fetch=canned_fetch(load_fixture("grants_gov_search2.json")))
    atoms = src.search(keyword="mental health", limit=25)
    assert len(atoms) == 2

    first = {a.id: a for a in atoms}["grants.gov:358126"]
    assert first.source == "grants.gov"
    assert first.funder == "Substance Abuse and Mental Health Services Administration"
    assert first.title == "Community Mental Health Services Block Grant"
    assert first.deadline == "2024-08-15"
    assert first.geography == ["US"]
    assert first.url.endswith("/358126")

    # Forecasted opp with empty closeDate → deadline stays None (no guessing).
    forecast = {a.id: a for a in atoms}["grants.gov:349900"]
    assert forecast.deadline is None


def test_limit_is_respected():
    src = GrantsGov(fetch=canned_fetch(load_fixture("grants_gov_search2.json")))
    assert len(src.search(limit=1)) == 1
