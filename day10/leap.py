from importlib.resources import as_file
from logging import makeLogRecord
from platform import freedesktop_os_release
from signal import SIG_DFL
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE


def is_leap(year):
  if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
    return True
  return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  ind = month - 1
  if is_leap(year) and month == 2:
    return (month, 29)
  else:
    return (month, month_days[ind])


while True:
  year = int(input("Enter year: "))
  month = int(input("Enter month: "))
  result = days_in_month(year, month)
  print("Month number %d has %d days." % (result[0], result[1]))