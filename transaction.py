class Transaction(object):
  def __init__(self):
    self.__date = "01/01/1900"
    self.__amount = 0

  @property
  def date(self):
    return self.__date

  @property
  def amount(self):
    return self.__amount
