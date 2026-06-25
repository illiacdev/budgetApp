"""Core transaction handling for the budget CLI app."""

import csv
from pathlib import Path
from collections.abc import Sequence
from typing import Union


def add_transaction(transactions: Sequence[dict], transaction: dict) -> list[dict]:
    """Add a transaction to the transaction list and return a new list."""

    return [*transactions, transaction]


def get_balance(transactions: Sequence[dict]) -> float:
    """Return the sum of transaction amounts as the account balance."""

    if not transactions:
        return 0.0

    return float(sum(transaction["amount"] for transaction in transactions))


def filter_by_category(transactions: Sequence[dict], category: str) -> list[dict]:
    """Return transactions whose category matches the given category."""

    return [
        transaction
        for transaction in transactions
        if transaction["category"].lower() == category.lower()
    ]


def load_transactions_from_csv(path: Union[str, Path]) -> list[dict]:
    """Load transactions from a UTF-8-sig CSV file."""

    csv_path = Path(path)
    with csv_path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return [
            {
                "date": row["date"],
                "type": row["type"],
                "category": row["category"],
                "description": row["description"],
                "amount": int(row["amount"]),
                "memo": row["memo"],
            }
            for row in reader
        ]


def monthly_summary(transactions: Sequence[dict]) -> dict[str, dict[str, int]]:
    """Return monthly income, expense, and net totals."""

    summary: dict[str, dict[str, int]] = {}
    for transaction in transactions:
        month = transaction["date"][:7]
        amount = transaction["amount"]
        if month not in summary:
            summary[month] = {"income": 0, "expense": 0, "net": 0}
        if amount >= 0:
            summary[month]["income"] += amount
        else:
            summary[month]["expense"] += amount
        summary[month]["net"] += amount

    return summary
