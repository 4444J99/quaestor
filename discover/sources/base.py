"""Source adapter base: the read-only contract + a stdlib HTTP fetcher.

The HTTP layer is injectable (``fetch``) so adapters are unit-testable without
touching the network. The default fetcher uses only ``urllib`` — zero
dependencies — and is deliberately minimal: GET or a JSON POST, a polite
User-Agent, a timeout, and JSON decoding. It exposes no write verbs.
"""

from __future__ import annotations

import abc
import json
import urllib.error
import urllib.request
from typing import Any, Callable, Protocol

from ..atom import GrantAtom

USER_AGENT = "quaestor-discover/0.1 (+https://github.com/organvm/quaestor; read-only grant discovery)"
DEFAULT_TIMEOUT = 20


class PaidSourceGated(Exception):
    """Raised when a paid source is requested before the QS-012 cost decision."""


class HttpError(Exception):
    """Any transport-level failure fetching a source (never fatal to a run)."""


class Fetch(Protocol):
    def __call__(
        self,
        url: str,
        *,
        payload: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> dict[str, Any]: ...


def default_fetch(
    url: str,
    *,
    payload: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Fetch ``url`` and return decoded JSON.

    ``payload`` present → JSON POST; otherwise GET. Read-only by construction:
    there is no code path here that submits an application, registers, or pays.
    """
    hdrs = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        hdrs["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=hdrs, method="POST" if data else "GET")
    try:
        with urllib.request.urlopen(req, timeout=DEFAULT_TIMEOUT) as resp:  # noqa: S310 (fixed https hosts)
            raw = resp.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:  # pragma: no cover - network
        raise HttpError(f"fetch failed for {url}: {exc}") from exc
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise HttpError(f"non-JSON response from {url}: {exc}") from exc


class Source(abc.ABC):
    """A read-only funding source adapter.

    Subclasses implement :meth:`search`, returning normalized atoms. A subclass
    sets ``paid = True`` to declare it is gated on QS-012; the runner refuses to
    poll it until the cost decision is made.
    """

    name: str = "abstract"
    paid: bool = False

    def __init__(self, fetch: Fetch | None = None) -> None:
        self._fetch: Fetch = fetch or default_fetch

    @abc.abstractmethod
    def search(self, *, keyword: str = "", limit: int = 25) -> list[GrantAtom]:
        """Return up to ``limit`` normalized atoms for ``keyword`` (read-only)."""
        raise NotImplementedError


AtomFactory = Callable[[dict[str, Any]], GrantAtom]
