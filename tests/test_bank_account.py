import unittest
from bank_account import *

class BankAccountTest(unittest.TestCase):

  def test_zero_starting_balance(self):
    account = BankAccount()
    self.assertEqual(0, account.balance)

  def test_add_transaction(self):
    account = BankAccount()
    transaction = 5
    account.add_transaction(transaction)
    self.assertEqual(1, len(account.transactions))
