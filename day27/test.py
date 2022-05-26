# *args = "unlimited positional arguments"
def add(*args):
  # args is a tuple
  print(args)
  sum = 0
  for n in args:
    sum += n

  return sum

print(f"The sum is {add(88, 50, 15, 75, 223, 303, 357)}")

def calculate(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # for key, value in kwargs.items(): ->>>
  print(kwargs.keys())


calculate(add=3, multiply=5)

def foo(*args, **kwargs):
  print(args)
  print(kwargs)

foo(1, 2, jack="shit", billy="bob")