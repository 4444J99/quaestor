"""Read-only source adapters (free sources first; paid sources gated on QS-012)."""

from .base import HttpError, PaidSourceGated, Source, default_fetch
from .grants_gov import GrantsGov
from .propublica import ProPublica

__all__ = ["GrantsGov", "HttpError", "PaidSourceGated", "ProPublica", "Source", "default_fetch"]
