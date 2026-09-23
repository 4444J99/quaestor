"""quaestor.discover — QS-010 read-only grant-discovery source adapters.

Poll funding sources **read-only** and emit one normalized grant atom per
opportunity (see ``plans/10-discover.md``). Free sources only; paid sources
(Candid, Instrumentl) are gated on the QS-012 cost decision and are not wired.

Hard rules (enforced here):
  1. Read-only — adapters search/read; they never submit, register, or pay.
  2. Respect terms + rate limits — official APIs, polite pacing, bounded caps.
  3. Secrets stay out of git — free sources need no key; any optional key is
     read from the environment and never committed.
  4. Cost is gated — paid sources raise ``PaidSourceGated`` until QS-012.
  5. No accounts — nothing here creates a funder/portal/API account.
"""

from .atom import GrantAtom
from .runner import FREE_SOURCES, DiscoveryRunner

__all__ = ["FREE_SOURCES", "DiscoveryRunner", "GrantAtom"]
