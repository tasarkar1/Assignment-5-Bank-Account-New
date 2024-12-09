
import datetime as dt
from datetime import datetime


class Transaction:
    def __init__(self, amount, timestamp=None):
        self.amount= amount
        if timestamp is not None:
          self.amount=amount
          self.timestamp = timestamp
        else:
            self.amount=amount
            self.timestamp=dt.date.today()


    def __repr__(self):
        return 'Transaction(amount={}, timestamp={}'.format(
      repr(self.amount),
            repr(self.timestamp),

        )

    def __str__(self):
        return self.timestamp, self.amount


class Account:
    def __init__(self):
        self.transactions= []

    def deposit(self, amount):
        amount=(abs(amount))
        transaction1=(Transaction(amount))
        self.transactions.append(transaction1.amount)

    def withdraw(self, amount):
        amount=(-abs(amount))
        transaction1=(Transaction(amount))
        self.transactions.append(transaction1.amount)
    def get_balance(self):
        return sum(self.transactions)


#Examples

#1: Transaction, no timestamp entered
#assert transaction.timestamp=2024-11-18
transaction= Transaction(150)
print(transaction.timestamp)

#2: Transaction, timestamp entered
#assert transaction.timestamp=2005-01-10
transaction= Transaction(150,dt.date(2005, 1, 10))
print(transaction.timestamp)

#3: Account deposit
#assert account.get_balance == 500
account=Account()
account.deposit(500)
print(account.get_balance())

#4: Account withdrawal
#assert account.get_balance == 460
account.withdraw(40)
print(account.get_balance())