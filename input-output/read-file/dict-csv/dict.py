students = [] # we create an empty list called students 

with open("students.csv") as file: # we use a with statement to open the file students.csv
    for line in file: # we iterate over the lines in the file
        name, house = line.rstrip().split(",") # we split the line into two variables name and house
        student = {} # the student variable is a dictionary
        student["name"] = name
        student["house"] = house
        student.append(student) # we append the name and house to the students list

for student in students:
    print(f"student ['name'] is in {student['house']}") # print the name and house of the student
    