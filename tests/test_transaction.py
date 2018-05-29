import unittest
from transaction import *

class TransactionTest(unittest.TestCase):

  def test_create_transaction(self):
    transaction = Transaction()
    self.assertEqual(0, transaction.amount)
