student_heights = input("Enter a list of student heights: ").split()

total = 0

for x in student_heights:
    total = total + int(x)

print("The average is %f." % (total / len(student_heights)))
