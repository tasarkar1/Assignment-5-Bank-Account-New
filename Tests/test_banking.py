from banking import Account
from banking import Transaction
import datetime as dt
from datetime import datetime

transaction= Transaction(150,dt.date(2005, 1, 10))

def test_transaction_timestamp():
    assert Transaction.timestamp== 2005-01-10