"""CSV loading and validation."""

from collections.abc import Iterator
from pathlib import Path

from app.core.models import Transaction


def load_transactions(path: Path) -> Iterator[Transaction]:
    """Yield transactions from a CSV file."""

    raise NotImplementedError
