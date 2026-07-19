"""``python -m discover`` entrypoint — delegates to :func:`discover.cli.main`."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
