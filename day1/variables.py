a = 1
b = 5000
print("a is %d and b is %d" % (a, b))
print("Switching values...")

(a, b) = (b, a)

print("The new value of a is %d" % a)
print("The new value of b is %d" % b)
