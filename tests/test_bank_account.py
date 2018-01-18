import unittest
from bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

  def test_add_transaction(self):
    account = BankAccount()
    account.add_transaction('test transaction value')
    self.assertEqual(1, len(account.transactions))
