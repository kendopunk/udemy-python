score_input = input("Enter a list of student heights: ").split()
scores = []
for x in score_input:
    scores.append(int(x))

print("The max score is %d." % max(scores))
