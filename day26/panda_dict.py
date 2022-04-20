import pandas as p

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 88]
}

df = p.DataFrame(student_dict)

for (index, row) in df.iterrows():
    print(index, row)  # row is a pandas series object
    print(row.student)
