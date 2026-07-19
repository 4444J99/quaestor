from conftest import load_fixture

from discover.runner import FREE_SOURCES, DiscoveryRunner


def _dispatch_fetch():
    """A fetch that returns the right fixture based on the URL host."""
    grants = load_fixture("grants_gov_search2.json")
    propub = load_fixture("propublica_search.json")

    def _fetch(url, *, payload=None, headers=None):
        if "api.grants.gov" in url:
            return grants
        if "propublica.org" in url:
            return propub
        raise AssertionError(f"unexpected url {url}")

    return _fetch


def _runner(tmp_path):
    return DiscoveryRunner(atoms_dir=tmp_path / "atoms", polite_delay=0, sleep=lambda _s: None)


def test_free_sources_registered():
    assert set(FREE_SOURCES) == {"grants.gov", "propublica"}


def test_run_polls_free_sources_and_writes(tmp_path):
    r = _runner(tmp_path)
    summary = r.run(fetch=_dispatch_fetch())
    assert summary["new_atoms"] == 4  # 2 grants.gov + 2 propublica
    assert summary["per_source"] == {"grants.gov": 2, "propublica": 2}
    assert not summary["errors"]
    assert r.store_path.exists()
    assert len(r.store_path.read_text().strip().splitlines()) == 4


def test_dedupe_across_runs(tmp_path):
    r = _runner(tmp_path)
    r.run(fetch=_dispatch_fetch())
    second = r.run(fetch=_dispatch_fetch())
    assert second["new_atoms"] == 0  # everything already seen
    assert len(r.store_path.read_text().strip().splitlines()) == 4


def test_dry_run_writes_nothing(tmp_path):
    r = _runner(tmp_path)
    summary = r.run(fetch=_dispatch_fetch(), dry_run=True)
    assert summary["new_atoms"] == 4
    assert len(summary["atoms"]) == 4
    assert not r.store_path.exists()


def test_paid_source_is_gated(tmp_path):
    r = _runner(tmp_path)
    summary = r.run(sources=["candid"], fetch=_dispatch_fetch())
    assert "candid" in summary["errors"]
    assert "QS-012" in summary["errors"]["candid"]
    assert summary["new_atoms"] == 0


def test_per_source_cap_bounds_results(tmp_path):
    r = DiscoveryRunner(atoms_dir=tmp_path / "atoms", per_source_cap=1, polite_delay=0, sleep=lambda _s: None)
    summary = r.run(fetch=_dispatch_fetch())
    assert summary["per_source"] == {"grants.gov": 1, "propublica": 1}
