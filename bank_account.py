class BankAccount(object):
  def __init__(self):
    self.__transactions = []

  @property
  def transactions(self):
    return self.__transactions

  def add_transaction(self, transaction):
    self.__transactions.append(transaction)
