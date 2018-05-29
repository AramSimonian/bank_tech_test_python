import unittest
from transaction import *

class TransactionTest(unittest.TestCase):

  def test_transaction_amount(self):
    transaction = Transaction("01/01/1900", 0)
    self.assertEqual(0, transaction.amount)

  def test_transaction_date(self):
    transaction = Transaction("01/01/1900", 0)
    self.assertEqual("01/01/1900", transaction.date)
