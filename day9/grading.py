scores = {
    "John": 81.5,
    "Fred": 100,
    "Chad": 50,
    "Wopper": 30,
    "Katie": 73
}


def calc_grade(score):
    if score >= 91:
        return "Outstanding"
    elif score >= 81:
        return "Exceeds Expectations"
    elif score >= 71:
        return "Acceptable"
    elif score >= 61:
        return "Needs Improvement"
    else:
        return "You're a fuck up."


for k in scores:
    print("%s has a grade of ---> %s" % (k, calc_grade(scores[k])))
