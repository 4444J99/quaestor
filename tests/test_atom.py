from discover.atom import GrantAtom


def test_to_dict_matches_plan_schema():
    atom = GrantAtom(
        id="grants.gov:123",
        source="grants.gov",
        funder="HHS",
        title="Test Opportunity",
        url="https://example/123",
    )
    d = atom.to_dict()
    # Exact top-level keys from plans/10-discover.md
    assert set(d) == {
        "id", "source", "funder", "title", "url", "amount", "deadline",
        "eligibility_raw", "geography", "focus", "requires_501c3", "fetched_at", "fit_score",
    }
    assert d["amount"] == {"min": None, "max": None, "currency": "USD"}
    assert d["fit_score"] is None
    assert d["requires_501c3"] is None


def test_roundtrip_from_dict():
    atom = GrantAtom(
        id="propublica:99",
        source="propublica",
        funder="Foundation X",
        title="Profile",
        url="https://example/99",
        amount_min=1000.0,
        amount_max=50000.0,
        deadline="2025-01-01",
        geography=["CA"],
        focus=["P20"],
        requires_501c3=True,
        fit_score=0.7,
    )
    again = GrantAtom.from_dict(atom.to_dict())
    assert again == atom


def test_fetched_at_is_iso_utc():
    atom = GrantAtom(id="x:1", source="x", funder="", title="", url="")
    assert atom.fetched_at.endswith("Z")
    assert "T" in atom.fetched_at
