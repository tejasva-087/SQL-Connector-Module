"""Custom errors for sql_connection.py"""

class InvalidCredentials(Exception):
  """Raise when the user enters invaid credentials"""
  err_msg = 'The connection was not successful due to invalid credentials'

class ConnectionNotSuccessful(Exception):
  """Raise when the connection can not be established"""
  err_msg = 'The connection was not successful'

class DeletingNonExistingDatabase(Exception):
  """Raised when the database doesn't exist and the user tries to delete it"""
  err_msg = "Cant delete the database that doesn't exist"

class IncorrectName(Exception):
  """Raised when the table name is incorrect"""
  err_msg = "Table or column name can not have spaces and cannot begin from a number"

class TableAlreadyExists(Exception):
  """Raised when the table name is incorrect"""
  err_msg = "Table already exists in the database"
