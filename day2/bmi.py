print("BMI Calculator")
print("=" * 20)
height = input("Enter height (m): ")
weight = input("Enter weight (kg): ")

try:
    height = float(height)
    weight = float(weight)
except ValueError:
    print("One or more invalid values entered.")
    exit(1)

print("Your BMI is %d." % int((weight / (height ** 2))))

# 35.5
#
# 1.8288
# 96.615096
# 81.64656 (180 pounds)
