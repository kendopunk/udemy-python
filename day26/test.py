name = "Angela"
letters_list = [x for x in name]
print(letters_list)

doubled = [x * 2 for x in range(1, 5)]
print(doubled)

maybe_tripled = [x * 3 for x in range(1, 10) if x > 5]
print(maybe_tripled)


def foo(value):
    if value > 5:
        return True
    return False


with_fn = [x * 3 for x in range(1, 10) if foo(x)]
print(with_fn)

squared = [x * x for x in range(1, 51)]
print(squared)

even = [x for x in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] if x % 2 == 0]
print(even)
