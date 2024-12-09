import pytest
from banking import Account
from banking import Transaction
import datetime as dt
from datetime import datetime

account=Account()
account.deposit(500)
account.withdraw(40)
print(account.get_balance())

def test_account_withdraw():
    assert account.get_balance== 460