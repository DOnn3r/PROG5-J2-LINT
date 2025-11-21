import pytest
from wallet import Wallet


@pytest.fixture
def new_wallet():
    return Wallet("marron", "petit", 100.0)


def test_initial_amount(new_wallet):
    assert new_wallet.checkVola() == 100.0
    assert new_wallet.isOpen is False


def test_add_money(new_wallet):
    new_wallet.addVola(50.0)
    assert new_wallet.checkVola() == 150.0


def test_add_negative_money(new_wallet):
    new_wallet.addVola(-10.0)
    assert new_wallet.checkVola() == 100.0


def test_get_money_success(new_wallet):
    amount_retrieved = new_wallet.getVola(25.0)
    assert amount_retrieved == 25.0
    assert new_wallet.checkVola() == 75.0


def test_get_money_insufficient_funds(new_wallet):
    amount_retrieved = new_wallet.getVola(200.0)
    assert amount_retrieved == 0.0
    assert new_wallet.checkVola() == 100.0


def test_open_close(new_wallet):
    new_wallet.open()
    assert new_wallet.isOpen is True
    new_wallet.close()
    assert new_wallet.isOpen is False
