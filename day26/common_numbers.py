# Day 26 -> list comprehension 3

# numbers common to both files
fh1 = open("./file1.txt", "r")
fh1_data = fh1.readlines()
d1 = list(map(lambda x: int(x.strip()), fh1_data))
fh1.close()

fh2 = open("./file2.txt", "r")
fh2_data = fh2.readlines()
d2 = list(map(lambda x: int(x.strip()), fh2_data))
fh2.close()

common_list = [x for x in d1 if x in d2]
print(f"d1 = {d1}")
print(f"d2 = {d2}")
print(f"common list = {sorted(common_list)}")
