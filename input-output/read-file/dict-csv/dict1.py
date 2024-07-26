students = [] # we create an empty list called students 

with open("students.csv") as file: # we use a with statement to open the file students.csv
    for line in file: # we iterate over the lines in the file
        name, house = line.rstrip().split(",") # we split the line into two variables name and house
        student = {"name": name, "house": house} # the student variable is a dictionary in one line rather than 3
        student.append(student) # we append the name and house to the students list

# we create a function whose sole purpose is to return the name of the students
def get_name(student):
    return student["name"]

for student in students:
    print(f"student ['name'] is in {student['house']}") # print the name and house of the student


# this is not sorted correctly look for the sorted version on dict2.py