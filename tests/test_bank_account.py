import unittest
from bank_account import *

class BankAccountTest(unittest.TestCase):

  def test_add_transaction(self):
    account = BankAccount()
    transaction = 'test transaction value'
    account.add_transaction(transaction)
    self.assertEqual(1, len(account.transactions))
