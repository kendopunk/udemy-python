def format_name(fname, lname):
  str = fname + ' ' + lname
  return ' '.join(x for x in [fname.title(), lname.title()] if not x.isspace())

print(format_name(
  input("What is your first name? "),
  input("What is your last name? ")
))