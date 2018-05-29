class Transaction(object):
  def __init__(self, date, amount):
    self.__date = date
    self.__amount = amount

  @property
  def date(self):
    return self.__date

  @property
  def amount(self):
    return self.__amount
