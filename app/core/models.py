"""Domain models for transactions."""

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Transaction:
    """Single budget transaction."""

    date: date
    type: str
    category: str
    description: str
    amount: int
    memo: str = ""
