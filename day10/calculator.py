# What's the first number
# Pick an operation
# What's the second number?
# Type 'y' to continue calculating with {val} or 'n' to start a new calculation.  'q' to quit.

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def print_available_operations(d):
  for x in d:
    print(x)

def continue_statement(result):
  cont = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation.  'q' to quit: ")
  return cont


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
op = False
quit = False
a = False

while not quit:
  if not a:
    a = float(input("What's the first number?: "))
  print_available_operations(operations )
  while not op in operations.keys():
    op = input("Pick your operation: ")
  b = float(input("What's the second number? "))
  result = operations[op](a, b)
  print("%f %s %f = %f" % (a, op, b, result))

  op = ''
  cont = ''

  while not cont in ['n', 'q', 'y']:
    cont = continue_statement(result)

  if cont == 'q':
    exit(1)
  if cont == 'y':
    a = result
  if cont == 'n':
    a = False



