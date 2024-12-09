import pytest
from banking import Account
from banking import Transaction
import datetime as dt
from datetime import datetime

account=Account()
account.deposit(500)

def test_account_deposit():
    assert account.get_balance== 500