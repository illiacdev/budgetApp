"""Daily and monthly statistics."""

from collections.abc import Iterable

from app.core.models import Transaction


def daily_statistics(
    transactions: Iterable[Transaction],
) -> dict[str, dict[str, int]]:
    """Aggregate transactions by day."""

    raise NotImplementedError


def monthly_statistics(
    transactions: Iterable[Transaction],
) -> dict[str, dict[str, int]]:
    """Aggregate transactions by month."""

    raise NotImplementedError
