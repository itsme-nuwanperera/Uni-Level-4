class OutOfRange(Exception):
  """This exception raised for the given value is out of range.
  
  message - "Error message!" 
  """

  def __init__(self, message="Input is out of range!"):
    self.message = message
    super().__init__(self.message)

class NotSameValue(Exception):
  """This exception raised for the given value is not same.
  
  message - "Error message!" 
  """

  def __init__(self, message="input is not same!"):
    self.message = message
    super().__init__(self.message)