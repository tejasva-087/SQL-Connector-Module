"""Custom errors for sql_connection.py"""

class InvalidCredentials(Exception):
  """Raise when the user enters invaid credentials"""
  err_msg = 'The connection was not successful due to invalid credentials'

class ConnectionNotSuccessful(Exception):
  """Raise when the connection can not be established"""
  err_msg = 'The connection was not successful'