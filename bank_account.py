class BankAccount(object):
  def __init__(self):
    self.__transactions = []
    self.__balance = 0

  @property
  def transactions(self):
    return self.__transactions

  @property
  def balance(self):
    return self.__balance

  def alter_balance(self, amount):
    self.__balance += amount

  def add_transaction(self, transaction):
    self.alter_balance(transaction)
    self.__transactions.append(transaction)
