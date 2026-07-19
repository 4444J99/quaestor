from conftest import canned_fetch, load_fixture

from discover.sources.propublica import ProPublica


def test_search_maps_orgs_to_funder_atoms():
    src = ProPublica(fetch=canned_fetch(load_fixture("propublica_search.json")))
    atoms = src.search(keyword="mental health", limit=25)
    assert len(atoms) == 2

    robin = {a.id: a for a in atoms}["propublica:133433452"]
    assert robin.source == "propublica"
    assert robin.funder == "Robin Hood Foundation"
    assert robin.geography == ["NY"]
    assert robin.focus == ["P20"]
    assert "NTEE P20" in robin.eligibility_raw
    assert "501(c)(3)" in robin.eligibility_raw
    # Funder profile: no opportunity deadline / committed amount.
    assert robin.deadline is None
    assert robin.amount_min is None
    assert robin.url.endswith("/133433452")


def test_limit_is_respected():
    src = ProPublica(fetch=canned_fetch(load_fixture("propublica_search.json")))
    assert len(src.search(limit=1)) == 1
