from datetime import date
from pathlib import Path

import pytest

from app.core.csv_loader import load_transactions
from app.core.models import Transaction
from app.core.statistics import daily_statistics, monthly_statistics
from app.main import create_app
from app.web.routes import register_routes


def test_transaction_model_instantiates() -> None:
    transaction = Transaction(
        date=date(2026, 1, 5),
        type="지출",
        category="식비",
        description="점심식사",
        amount=-12000,
        memo="",
    )

    assert transaction.amount == -12000


def test_create_app_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        create_app()


def test_load_transactions_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        list(load_transactions(Path("data/step1_transactions.csv")))


def test_daily_statistics_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        daily_statistics([])


def test_monthly_statistics_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        monthly_statistics([])


def test_register_routes_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        register_routes(object())
