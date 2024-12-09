from banking import Account
from banking import Transaction
import datetime as dt
from datetime import datetime

transaction= Transaction(150)

def test_transaction_no_timestamp():
    assert Transaction.timestamp== 2024-12-09