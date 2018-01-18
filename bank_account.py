class BankAccount(object):
  def __init__(self):
    self.__transactions = []

  @property
  def transactions(self):
    return self.__transactions

  def add_transaction(self, thing):
    self.__transactions.append(thing)
